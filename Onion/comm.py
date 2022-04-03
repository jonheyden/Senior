











import serial
import time
import subprocess
#ser = serial.Serial('/dev/ttyS0', 9600)
ser = serial.Serial('/dev/ttyS1', 9600,timeout=None)


'''

with open("settings.txt") as data:
   lines = data.readlines()
   for line in lines:
      ser.write(str.encode(line))
      ser.read_until(expected = b'recieved')
      print("recieved return")

ser.close()
'''

while(1):
   if ser.in_waiting > 0:
      y = ''
      x = ser.readline()
      if x == b'temp\n':
         y = ser.readline()
         print(y)
         f = open("temp.txt","wb")
         f.write(y)
         f.close()
      elif x == b'input\n':
         y = ser.readline()
         f = open("input.txt","wb")
         f.write(y)
         f.close()
   process = subprocess.call("./startMqtt_runMain.sh",shell=True)
   time.sleep(.1)




'''
import serial

#ser = serial.Serial('/dev/ttyS0', 9600)
ser = serial.Serial('/dev/ttyS1', 9600)

data = open('settings.txt')

ser.write(data.read())

data.close()
ser.close()


import serial

#ser = serial.Serial('/dev/ttyS0', 9600)
ser = serial.Serial('/dev/ttyS1', 500000,timeout=None)

with open("settings.txt") as data:
   lines = data.readlines()
   for line in lines:
      ser.write(str.encode(line))
      ser.read_until(expected = b'recieved')
      print("recieved return")

ser.close()


import board
import busio
import digitalio
import time

# For most CircuitPython boards:
led = digitalio.DigitalInOut(board.LED)
# For QT Py M0:
# led = digitalio.DigitalInOut(board.SCK)
led.direction = digitalio.Direction.OUTPUT

uart = busio.UART(board.TX1, board.RX1, baudrate=500000)

while True:
    time.sleep(.01)
    #print(uart.in_waiting)

    while uart.in_waiting > 0:
        print(uart.in_waiting)
        led.value = True
        data = uart.read(uart.in_waiting)
        #print(data)
        #print(data)
        # convert bytearray to string
        #data_string = ''.join([chr(b) for b in data])
        #data_string = data_string.strip()
        #data_string = data_string.split(',')
        #print(data_string, end="")
        print(data.decode().strip())
        uart.write(b'recieved')
        time.sleep(.01)
        led.value = False
'''