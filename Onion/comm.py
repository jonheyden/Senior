import serial
import time
import subprocess
#ser = serial.Serial('/dev/ttyS0', 9600)
ser = serial.Serial('/dev/ttyS1', 115200,timeout=None)

inputarray = [0,0,0,0,0,0,0,0]
pidarray = [0,0,0,0,0,0,0,0]
outputvalue = [0,0,0,0,0,0,0,0]
ltcvalue = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

with open("settings.txt") as data:
   lines = data.readlines()
   for line in lines:
      ser.write(str.encode(line))
      ser.read_until(expected = b'recieved')

ser.write(str.encode('Input Data'))
for i in inputarray:
   y = ser.readline()
   inputarray[i] = list(map(int,y))

ser.write(str.encode('Output Data'))
for i in outputvalue:
   y = ser.readline()
   outputvalue[i] = list(map(int,y))

ser.write(str.encode('PID Data'))
for i in pidarray:
   y = ser.readline()
   pidarray[i] = list(map(int,y))

ser.write(str.encode('LTC Data'))
for i in ltcvalue:
   y = ser.readline()
   ltcvalue[i] = list(map(int,y))

with open("values.txt") as d2:
   for i in range(len(inputarray)):
      d2.write(str(inputarray[i]) + '\n')
   
   for i in range(len(outputvalue)):
      d2.write(str(outputvalue[i]) + '\n')

   for i in range(len(pidarray)):
      d2.write(str(pidarray[i]) + '\n')

   for i in range(len(ltcvalue)):
      d2.write(str(ltcvalue[i]) + ',\n')

ser.close()
