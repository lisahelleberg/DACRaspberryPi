import smbus
import time
import socket

UDP_IP = "169.254.59.53"
UDP_PORT = 7000
bus = smbus.SMBus(1)
MESSAGE = "Hello, World!"
print ("UDP target IP: ", UDP_IP)
print ("UDP target port: ", UDP_PORT)
print ("message: ", MESSAGE)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("169.254.28.200", UDP_PORT))
running = True
delay = 0.5

print("Read from analog to digital converter")
print("Ctrl+c to stop")

#choose to read from onboard light sensor

bus.write_byte(0x48, 0x00)

last_reading = -1

while(True):
 reading = bus.read_byte(0x48)
 if (abs(last_reading - reading) > 2):
  print(reading)
  time.sleep(4)
last_reading = reading

