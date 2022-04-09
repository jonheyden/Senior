Code on Onion Omega
======================


There are two main programs that can be run on the Onion Omega. The first is a simple python script that will send the information located in the settings.txt file. 

The configuration information can be found in the "How to Format Data for UART" section under "API Examples."


The other program is for CIP control through the ethernet port avaialble on the board. This program will create a CIP link to the targetted controller and start to read/write values based on the values of the PLC. 

This is possible by leveraging the pycomm3 library by ottowayi. The Onion is capable of both python 2 and python 3. In order to use this library, the user must call python3 on the command line.

The code on available through github is using a dummy IP, the address will need to be configured by the user. Further, the tags will need to be made available in the PLC by the user, either through an AOI or manually. The program will fail if it can not find the tags at the address expected. 

The first code block is an example of generating the tag names in an array for accessing multiple tags at once.  


.. code-block:: python
   :caption: Generating Tag Names

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



This next code block are the arrays that will hold our read/write values until they can be written to a text file. 

.. code-block::python

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


Below are two helper functions that will be used to read and write values to the PLC.

.. code-block::python

   def read_settings(plcad, array):
      with pycomm3.LogixDriver(plcad) as plc:
         return plc.read_multiple(array)
         

   def write_values(plcad, tagarray, valuearray):
      with pycomm3.LogixDriver(plcad) as plc:
         plc.write_multiple(tagarray, valuearray)


This code block is the Main Loop of the program. The first section starts by reading the different tag values, held as custom structures in the PLC with the tag name associated in the array.

.. code-block::python

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


For ease of use with the existing comm.py program, we write the settings to the settings.txt file. 

.. code-block::python

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

Once this is done, we will then call the subprocess.call() function on our existing comm.py script. This function will not return until the script is done running. 

.. code-block::python
      process = subprocess.call(['python', 'comm.py'], shell=True)


Below is the script being called by the subprocess.call() function. The script will read the settings.txt file and then write the values to the Teensy. After this, it will request the output information from the Teensy and write it to the values.txt file.

.. code-block::python

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



Once back in the main program, we will now open our values.txt and read the data into their proper arrays. 

.. code-block::python

      inputfile = open('values.txt', 'r')
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



The final piece is writing the values back to the PLC. 

For the input array, it is the scaled values.

For the output array, it is the output percentage.

For the PID array, it is the output percentage of the PID. 

For the relay array, it is the value of each relay (on/off).

For the digital array, it is the value of each digital output (on/off).

For the LTC Array, it is the returned value of each of the active channels, 0 otherwise. 

.. code-block::python

      write_values(plc_address, input_array_tags, inputarray)
      write_values(plc_address, output_array_tags, outputvalue)
      write_values(plc_address, pid_array_tags, pidarray)
      write_values(plc_address, relay_array_tags, relayarr)
      write_values(plc_address, digital_array_tags, digitalarr)
      write_values(plc_address, ltc_array_tags, ltcarr)



Below are some examples of how to create structures to send to the PLC, which have to match the structure of the PLC.

.. code-block::python


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

   input0 = input_struct('0',0,0,0)
   input1 = input_struct('1',0,0,0)
   input2 = input_struct('2',0,0,0)
   input3 = input_struct('3',0,0,0)
   input4 = input_struct('4',0,0,0)
   input5 = input_struct('5',0,0,0)
   input6 = input_struct('6',0,0,0)
   input7 = input_struct('7',0,0,0)

   output0 = output_struct('0',0,0,0)
   output1 = output_struct('1',0,0,0)
   output2 = output_struct('2',0,0,0)
   output3 = output_struct('3',0,0,0)
   output4 = output_struct('4',0,0,0)
   output5 = output_struct('5',0,0,0)
   output6 = output_struct('6',0,0,0)
   output7 = output_struct('7',0,0,0)

   pid0 = pid_struct('0',0,0,0,0,0,0,0,0,0,0,0)
   pid1 = pid_struct('1',0,0,0,0,0,0,0,0,0,0,0)
   pid2 = pid_struct('2',0,0,0,0,0,0,0,0,0,0,0)
   pid3 = pid_struct('3',0,0,0,0,0,0,0,0,0,0,0)
   pid4 = pid_struct('4',0,0,0,0,0,0,0,0,0,0,0)
   pid5 = pid_struct('5',0,0,0,0,0,0,0,0,0,0,0)
   pid6 = pid_struct('6',0,0,0,0,0,0,0,0,0,0,0)
   pid7 = pid_struct('7',0,0,0,0,0,0,0,0,0,0,0)

   relay0 = {'relay0' : 0}
   relay1 = {'relay1' : 0}
   relay2 = {'relay2' : 0}
   relay3 = {'relay3' : 0}
   relay4 = {'relay4' : 0}
   relay5 = {'relay5' : 0}
   relay6 = {'relay6' : 0}
   relay7 = {'relay7' : 0}

   digital0 = {'digital0' : 0}
   digital1 = {'digital1' : 0}
   digital2 = {'digital2' : 0}
   digital3 = {'digital3' : 0}
   digital4 = {'digital4' : 0}
   digital5 = {'digital5' : 0}
   digital6 = {'digital6' : 0}
   digital7 = {'digital7' : 0}

   ltc0 = ltc_struct('0',0,0,0,0)
   ltc1 = ltc_struct('1',0,0,0,0)
   ltc2 = ltc_struct('2',0,0,0,0)
   ltc3 = ltc_struct('3',0,0,0,0)