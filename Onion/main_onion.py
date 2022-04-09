import pycomm3
import serial
import time
import subprocess


def input_struct(inputnum,mode, enghigh, englow):
   
   input_struct ={
      'Input' : inputnum,
      'Mode' : mode,
      'EngHigh' : enghigh,
      'EngLow' : englow
   }
   return input_struct

def output_struct(outputnum,mode, outputvalue,enable):
   output_struct ={
      'Output' : outputnum,
      'Mode' : mode,
      'OutputValue' : outputvalue,
      'Enable' : enable
   }
   return output_struct

def pid_struct(pidnum,kp,ki,kd,minout,maxout,minin,maxin,sampletime,setpoint,mode,enable):
   pid_struct ={
      'PID' : pidnum,
      'Kp' : kp,
      'Ki' : ki,
      'Kd' : kd,
      'MinOut' : minout,
      'MaxOut' : maxout,
      'MinIn' : minin,
      'MaxIn' : maxin,
      'SampleTime' : sampletime,
      'SetPoint' : setpoint,
      'Mode' : mode,
      'Enable' : enable
   }
   return pid_struct

def ltc_struct(banknum,sensortype0,sensortype1,sensortype2,sensortype3):
   ltc_struct ={
      'Bank' : banknum,
      'Sensor0' : sensortype0,
      'Sensor1' : sensortype1,
      'Sensor2' : sensortype2,
      'Sensor3' : sensortype3
   }
   return ltc_struct





#Initialization Variables to be set by user
plc_address = "10.20.30.100"


input_array_tags = ['input0', 'input1', 'input2', 'input3', 'input4', 'input5', 'input6', 'input7']
output_array_tags = ['output0', 'output1', 'output2', 'output3', 'output4', 'output5', 'output6', 'output7']
pid_array_tags = ['pid0', 'pid1', 'pid2', 'pid3', 'pid4', 'pid5', 'pid6', 'pid7']
relay_array_tags = ['relay0', 'relay1', 'relay2', 'relay3', 'relay4', 'relay5', 'relay6', 'relay7']
digital_array_tags = ['digital0', 'digital1', 'digital2', 'digital3', 'digital4', 'digital5', 'digital6', 'digital7']
ltc_array_tags = ['ltc0', 'ltc1', 'ltc2', 'ltc3']

input_array_values = ['input0value', 'input1value', 'input2value', 'input3value', 'input4value', 'input5value', 'input6value', 'input7value']

output_array_values = ['output0value', 'output1value', 'output2value', 'output3value', 'output4value', 'output5value', 'output6value', 'output7value']

pid_array_values = ['pid0value', 'pid1value', 'pid2value', 'pid3value', 'pid4value', 'pid5value', 'pid6value', 'pid7value']

relay_array_values = ['relay0value', 'relay1value', 'relay2value', 'relay3value', 'relay4value', 'relay5value', 'relay6value', 'relay7value']

digital_array_values = ['digital0value', 'digital1value', 'digital2value', 'digital3value', 'digital4value', 'digital5value', 'digital6value', 'digital7value']

ltc_array_values = ['ltc3value', 'ltc4value', 'ltc5value', 'ltc6value', 'ltc7value', 'ltc8value', 'ltc9value', 'ltc10value', 'ltc11value', 'ltc12value', 'ltc13value', 'ltc14value', 'ltc15value', 'ltc16value']


pidarr = [
   [0,0,0,0,0,0,0,0,0,0,0], 
   [0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0]          
]
#input [mode, eng high, eng low]
inputarr = [
   [0,0,0],
   [0,0,0],
   [0,0,0],
   [0,0,0],
   [0,0,0],
   [0,0,0], 
   [0,0,0],
   [0,0,0]
]
#output [mode,output_value,enable]
outputarr = [
   [0,0,0],
   [0,0,0],
   [0,0,0],
   [0,0,0],
   [0,0,0],
   [0,0,0], 
   [0,0,0],
   [0,0,0]
]
#Relay [on/off]
relayarr = [
   [0],
   [0],
   [0],
   [0],
   [0],
   [0], 
   [0],
   [0]
]
digitalarr = [
   [0],
   [0],
   [0],
   [0],
   [0],
   [0], 
   [0],
   [0]
]      
#LTC [Sensor Type, Sensor Type, Sensor Type, Sensor Type]
ltcarr = [
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0]
]

inputarray = [0,0,0,0,0,0,0,0]
pidarray = [0,0,0,0,0,0,0,0]
outputvalue = [0,0,0,0,0,0,0,0]
ltcvalue = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


def read_settings(plcad, array):
   with pycomm3.LogixDriver(plcad) as plc:
      return plc.read_multiple(array)
      

def write_values(plcad, tagarray, valuearray):
   with pycomm3.LogixDriver(plcad) as plc:
      plc.write_multiple(tagarray, valuearray)



while(1):

   inputs = read_settings(plc_address, input_array_tags)
   for input_num in inputs:
      for k in input_num.keys():
         inputarr[input_num][k] = input_num[k]

   outputs = read_settings(plc_address, output_array_tags)
   for output_num in outputs:
      for k in output_num.keys():
         outputarr[output_num][k] = output_num[k]

   pids = read_settings(plc_address, pid_array_tags)
   for pid_num in pids:
      for k in pid_num.keys():
         pidarr[pid_num][k] = pid_num[k]

   relays = read_settings(plc_address, relay_array_tags)
   for relay_num in relays:
      for k in relay_num.keys():
         relayarr[relay_num][k] = relay_num[k]

   digitals = read_settings(plc_address, digital_array_tags)
   for digital_num in digitals:
      for k in digital_num.keys():
         digitalarr[digital_num][k] = digital_num[k]

   ltcs = read_settings(plc_address, ltc_array_tags)
   for ltc_num in ltcs:
      for k in ltc_num.keys():
         ltcarr[ltc_num][k] = ltc_num[k]

   settingsfile = open('settings.txt', 'w')
   
   settingsfile.write('input\n')
   for i in range(len(inputarr)):
      for k in range(len(inputarr[i])):
         if k < 2:
            settingsfile.write(inputarr[i][k] + ',\n')
         else:
            settingsfile.write(inputarr[i][k] + '\n')
   settingsfile.write('output\n')
   for i in range(len(outputarr)):
      for k in range(len(outputarr[i])):
         if k < 2:
            settingsfile.write(outputarr[i][k] + ',\n')
         else:
            settingsfile.write(outputarr[i][k] + '\n')
   
   settingsfile.write('pid\n')
   for i in range(len(pidarr)):
      for k in range(len(pidarr[i])):
         if k < 10:
            settingsfile.write(pidarr[i][k] + ',\n')
         else:
            settingsfile.write(pidarr[i][k] + '\n')

   settingsfile.write('relay\n')
   for i in range(len(relayarr)):
      for k in range(len(relayarr[i])):
         settingsfile.write(relayarr[i][k] + '\n')
   
   settingsfile.write('digital\n')
   for i in range(len(digitalarr)):
      for k in range(len(digitalarr[i])):
         settingsfile.write(digitalarr[i][k] + '\n')
   
   settingsfile.write('ltc\n')
   for i in range(len(ltcarr)):
      for k in range(len(ltcarr[i])):
         if k < 3:
            settingsfile.write(ltcarr[i][k] + ',\n')
         else:
            settingsfile.write(ltcarr[i][k] + '\n')

   settingsfile.close()

   process = subprocess.call(['python3', 'comm.py'], shell=True)

   inputfile = open('input.txt', 'r')
   for i in range(len(inputarray)):
      y = inputfile.readline()
      y = y.decode('utf-8').strip()
      inputarray[i] = y
   for i in range(len(outputvalue)):
      y = inputfile.readline()
      y = y.decode('utf-8').strip()
      outputvalue[i] = y
   for i in range(len(pidarray)):
      y = inputfile.readline()
      y = y.decode('utf-8').strip()
      pidarray[i] = y
   for i in range(len(ltcvalue)):
      y = inputfile.readline()
      y = y.decode('utf-8').strip()
      ltcvalue[i] = y

   inputfile.close()

   write_values(plc_address, input_array_tags, inputarray)
   write_values(plc_address, output_array_tags, outputvalue)
   write_values(plc_address, pid_array_tags, pidarray)
   write_values(plc_address, relay_array_tags, relayarr)
   write_values(plc_address, digital_array_tags, digitalarr)
   write_values(plc_address, ltc_array_tags, ltcarr)



   

   





   

   


   



         