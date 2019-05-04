# import RPi.GPIO as gpio
import smbus
import time

bus = smbus.SMBus(1)
address = 0x04

bus.write_byte(address, value)
bus.read_byte(address)
time.sleep(1)
