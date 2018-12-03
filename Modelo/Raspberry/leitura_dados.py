import spidev
import time
import os
import math

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

def ReadChannel(channel):
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

light_channel = 0
temp_channel  = 1

def read():
    leituraLuz = ReadChannel(light_channel)
    voltLuz = leituraLuz*5.0/1023.0
    light = math.exp(1/leituraLuz)*12932.99 - 12954.9 
    light /= 0.248
    light = round(light, 2)
    temp = round(ReadChannel(temp_channel)*5.0/1023.0*100, 2)
    return([light, temp])
