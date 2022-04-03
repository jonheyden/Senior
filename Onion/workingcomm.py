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
   y = ''
   x = ser.readline()
   if x == b'temp\n':
      y = ser.readline()
      f = open("temp.txt","wb")
      f.write(y)
      f.close()
   elif x == b'input\n':
      y = ser.readline()
      f = open("input.txt","wb")
      f.write(y)
      f.close()
   process = subprocess.call("./startMqtt_runMain.sh",shell=True)

   