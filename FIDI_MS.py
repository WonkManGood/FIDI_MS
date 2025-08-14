'''
"But Peter, you're going to die doing this! You're going to die in that stupid costume!"
'''

from machine import Pin, unique_id, freq
import time
freq(80000000)

class __mapping__():
    def __init__(self) -> None:
        self.map = {
            'A': '0000000',     'R': '0010001',     '8': '0100010',
            'B': '0000001',     'S': '0010010',     '9': '0100011',
            'C': '0000010',     'T': '0010011',     '.': '0100100',
            'D': '0000011',     'U': '0010100',     ',': '0100101',
            'E': '0000100',     'V': '0010101',     '@': '0100110',
            'F': '0000101',     'W': '0010110',     ' ': '0100111',
            'G': '0000110',     'X': '0010111',     ':': '0101000',
            'H': '0000111',     'Y': '0011000',
            'I': '0001000',     'Z': '0011001',
            'J': '0001001',     '0': '0011010',
            'K': '0001010',     '1': '0011011',
            'L': '0001011',     '2': '0011100',
            'M': '0001100',     '3': '0011101',
            'N': '0001101',     '4': '0011110',
            'O': '0001110',     '5': '0011111',
            'P': '0001111',     '6': '0100000',
            'Q': '0010000',     '7': '0100001',     
        }

class TwoWire(__mapping__):
    def __init__(self, com, clk, speed_scale: float=0.06):
        super().__init__()
        self.com = com
        self._clk = clk
        self.clk = Pin(self._clk, Pin.OUT, value=0)
        
        self.speed_scale = 0.06
    
    def _reverseDict_(self, arg1):
        for i in self.map:
            if self.map.get(i) == arg1:
                return i
        
    def listen(self):
        clk = Pin(self._clk, Pin.IN)
        com = Pin(self.com, Pin.IN)
        if not clk.value():
            return None
        
        clk_state = 0
        timing = 0
        data = []
        if clk.value():
            while timing < 10:
                _clk = clk.value()
                if clk_state != _clk:
                    data.insert(9999, str(com.value()))
                    print(com.value(), end='')
                    clk_state = _clk
                    timing = 0
                else:
                    timing = timing + 1
                time.sleep(self.speed_scale * 0.025)
        data.pop(0)
        data.pop(-1)
        posi = 0
        _data = []
        formated_data = []
        for i in data:
            if posi == 7:
                formated_data.insert(9999, self._reverseDict_(''.join(_data)))
                _data = []
                posi = 0
            posi = posi + 1
            _data.insert(9999, i)
        print(formated_data)
        data = []
        for i in formated_data:
            if not i:
                pass
            else:
                data.insert(9999, i)
        return ''.join(data)

    def write(self, data: str):
        clk = Pin(self._clk, Pin.OUT, value=1)
        com = Pin(self.com, Pin.OUT)
        data = data.upper()
        for i in range(len(data)):
            binary = self.map.get(data[i])
            for b in range(len(binary)):    
                com.value(int(binary[b]))             # type: ignore
                print(com.value(), end='')
                clk.toggle()
                time.sleep(self.speed_scale * 0.05)
            print('', end=' ')
        clk.off()
        com.off()

if __name__ == '__main__':
    # 3c8a1f5da6fc
    # 3728c000 C1
    write_speed = 0.5
    if unique_id().hex() == '3c8a1f5da6fc':
        tw = TwoWire(16, 17, 45)
        tw.write("mhm, i cant stay awake")
    if unique_id().hex() == '3728c000':
        tw = TwoWire(13, 12, 2)
        data = []
        old_data = []
        time_start = time.time()
        while True:
            byte = tw.listen()
            if byte:
                print(f'\n{byte}', end='')
                #time.sleep(write_speed * 0.01)