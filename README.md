# FIDI_MS
(Fine, I'll do it _ my self)\n
Simple Two-Wire bus protocol for ESP to ESP communication. 

> Now before you go and look at the source code, hear me out. For my own lack of knowledge, this is in Python. I'd much rather a faster and more reliable language for this, but out of laziness, here I am. And while yes, I'm sure there's other libraries out there for this and implimented much better, I enjoy figuring things out myself. This file may not fit your needs, but it serves its purpose in mine. Do what you will with that.

As the name implies, this is a two wire communcations protocol derived of laziness and necessity between two ESP32's. While not as abstract as other, I'd like to think this is more simple and bareboned than the other methods. All you need is one clock and one stream wire. Power and ground shouldn't play into effect.

I believe speeds can reach up to 100 bit/s, but I haven't done the calculations. Feel free to fork, modify, and critique as much as you want.