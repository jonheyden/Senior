'''
This code is selective and for the purpose of Demo Day. 

'''


import config as c
import shift_object
import output_obj
import ltc2984
import time

def init():
   """ Initializes objects from classes
   """
   global input_shiftreg
   input_shiftreg = shift_object.shiftregister(c.input_store, c.input_enable, c.input_shift, c.input_data, 8)

   global output_shiftreg
   output_shiftreg = shift_object.shiftregister(c.output_store, c.output_enable, c.output_shift, c.output_data, 16)
   output_shiftreg.enable()
   output_shiftreg.update(c.output_currentMode[1])

   global relay_shiftreg
   relay_shiftreg = shift_object.shiftregister(c.relay_store, c.relay_enable, c.relay_shift, c.relay_data, 8)
   
   global digital_shiftreg
   digital_shiftreg = shift_object.shiftregister(c.digital_store, c.digital_enable, c.digital_shift, c.digital_data, 8)
   digital_shiftreg.enable()
   digital_shiftreg.update(0b00000000)
   digital_shiftreg.update(0b00000001)
   digital_shiftreg.update(0b00000000)
   digital_shiftreg.disable()

   global output0_obj
   output0_obj = output_obj.output_container(c.output0,2)

   global output1_obj
   output1_obj = output_obj.output_container(c.output1,0)
   
   global ltcob
   ltcob = ltc2984.ltc2984(c.ltcspi, c.ltc_cs, c.ltc_interrupt)

   chan20 = (0x1c << 27) | (0x1 << 26) | (0x1 << 25) | (0x0 << 24) | (0x1 << 22) | (0x100c49 << 0)
   chan1 = (0x2 << 27) | (0x14 << 22) | (0x1 << 21) | (0x0 << 21) | (0x0 << 18)
   ltcob.chan_assignment(20,chan20)
   time.sleep(.5)
   ltcob.chan_assignment(1,chan1)

   return



old_time = time.monotonic_ns()
init()
temp = "temp" + '\n'
temp = bytes(temp, 'utf-8')
inputword = "input" + '\n'
inputword = bytes(inputword, 'utf-8')

tempsend = 0
convbit = 0
x = 0
updown = 0
temptocheck = 0
tempsend = str(tempsend)
tempsend = tempsend + '\r' + '\n'
tempsend = bytes(tempsend, 'utf-8')
output1_obj.enable()

countbit = 0

while(1):
   current_time = time.monotonic_ns()
   if (current_time - old_time) > 500000000:
      old_time = current_time
      countbit = 1

   if ltcob.check_interrupt() and convbit == 0:
      ltcob.chan_conv(1)
      convbit = 1
   if countbit == 1:
      if updown == 0:
         x += 1
         if x == 100:
            updown = 1
      else:
         x -= 1
         if x == 0:
            updown = 0 
      countbit = 0
   
   output1_obj.value(x)

   if convbit == 1 and ltcob.check_interrupt():
      tempsend = (ltcob.read_data(1)/1024)*(9/5)+32
      temptocheck = tempsend
      convbit = 0
      tempsend = int(tempsend)
      tempsend = str(tempsend)
      tempsend = tempsend + '\r' + '\n'
      tempsend = bytes(tempsend, 'ascii')

   if temptocheck > 80:
      digital_shiftreg.update(0b00000001)
      digital_shiftreg.enable()
   else:
      digital_shiftreg.update(0b00000000)
      digital_shiftreg.disable()

   if temptocheck > 94:
      relay_shiftreg.update(0b00000001)
      relay_shiftreg.enable()
   elif temptocheck < 75:
      relay_shiftreg.update(0b00000000)
      relay_shiftreg.disable()

   xsend = str(x//10)
   xsend = xsend + '\r'+ '\n'
   xsend = bytes(xsend, 'ascii')
   #print(temptocheck)


   c.onionuart.write(temp)
   #time.sleep(.1)
   c.onionuart.write(tempsend)
   #time.sleep(.1)
   c.onionuart.write(inputword)
   #time.sleep(.1)
   c.onionuart.write(xsend)
   #time.sleep(.1)

'''
import config as c
import shift_object
import output_obj




output_shiftreg = shift_object.shiftregister(c.output_store, c.output_enable, c.output_shift, c.output_data, 16)
#output_shiftreg.enable()
#output_shiftreg.update(c.output_currentMode[1])



output1_obj = output_obj.output_container(c.output1,0)
#output1_obj.enable()
#output1_obj.value(50)


x = 0
updown = 0


while(1):

   time.sleep(.5)
      if updown == 0:
         x += 1
         if x == 100:
            updown = 1
      else:
         x -= 1
         if x == 0:
            updown = 0 
      countbit = 0
   
   output1_obj.value(x)
   time.sleep(.1)







'''