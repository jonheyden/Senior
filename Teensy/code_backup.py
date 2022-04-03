'''
Variables for Teensy 4.1
#Inputs
Input0 = A9
Input1 = A8
Input2 = A7
Input3 = A6
Input4 = A5
Input5 = A4
Input6 = A3
Input7 = A2

#Outputs
Output0 = D2
Output1 = D3
Output2 = D4
Output3 = D5
Output4 = D6
Output5 = D7
Output6 = D8
Output7 = D9


@Todo: Check syntax/numbers in REPL
#Input Selection Shift Register
Input_Store = D14
Input_Enable = D41
Input_Shift = D15
Input_Data = D40

@Todo: Check syntax/numbers in REPL
#Output Selection Shift Register
Output_Store = D26
Output_Enable = D25
Output_Shift = D27
Output_Data = D24

@Todo: Check syntax/numbers in REPL
#Relay Selection Shift Register
Relay_Store = D31
Relay_Enable = D30
Relay_Shift = D32
Relay_Data = D29

@Todo: Check syntax/numbers in REPL
@Todo: Build Function for Shift Registers
#Digital Selection Shift Register
Digital_Store = D34
Digital_Enable = D35
Digital_Shift = D33
Digital_Data = D36

Built in function
#Onion RX/TX
Onion_RX = (RX1 UART1)
Onion_TX = (TX1 UART1)

Built in function
#LTCSPI
LTC_CS = D10 (SPI0)
LTC_MOSI = D11 (SPI0)
LTC_MISO = D12 (SPI0)
LTC_SCK = D13 (SPI0)
LTC_Interrupt = D37





"""CircuitPython Essentials: PWM with Fixed Frequency example."""
import time
import board
import pwmio
import digitalio
import shift_object
#import input_obj
import output_obj
#import pid_object
import config as c

# LED setup for most CircuitPython boards:
#led = pwmio.PWMOut(board.LED, frequency=3411, duty_cycle=0)
# LED setup for QT Py M0:
# led = pwmio.PWMOut(board.SCK, frequency=5000, duty_cycle=0)


def init():
   """ Initializes objects from classes
   """
   global input_shiftreg
   input_shiftreg = shift_object.shiftregister(c.input_store, c.input_enable, c.input_shift, c.input_data, 8)

   global output_shiftreg
   output_shiftreg = shift_object.shiftregister(c.output_store, c.output_enable, c.output_shift, c.output_data, 16)

   global relay_shiftreg
   relay_shiftreg = shift_object.shiftregister(c.relay_store, c.relay_enable, c.relay_shift, c.relay_data, 8)

   global digital_shiftreg
   digital_shiftreg = shift_object.shiftregister(c.digital_store, c.digital_enable, c.digital_shift, c.digital_data, 8)

   global output0_obj
   output0_obj = output_obj.output_container(c.output0,0)

   return


def main():
   print("before init")
   init()
   print("after init")
   output_shiftreg.enable()
   b1 = 0
   print("before while")
   while (1):
      time.sleep(10)
      if b1 == 0:
         output_shiftreg.update(0b00000001)
         b1 = 1
      output0_obj.value(50)





poweron():
initialize everything necessary


PID object gets passed 

loop():
   check uart
   if uart.read()
      store into new_settings array
      check if new_settings != current_settings
      if so, update settings
      store new_settings to current settings
   spi update values (if necessary)
   update PID values (function)
      if settings for particular input are from input_obj or from LTC2984, check value in settings to determine what to pass to PID object

   update outputs (may need to update output container to handle relays)



while(1):
   loop()

import config
import ltc2984
import time
ltcob = ltc2984.ltc2984(config.ltcspi, config.ltc_cs, config.ltc_interrupt)
chan20 = (0x1c << 27) | (0x1 << 26) | (0x1 << 25) | (0x0 << 24) | (0x1 << 22) | (0x100c49 << 0)
ltcob.chan_assignment(20,chan20)
time.sleep(.1)
ltcob.chan_conv(20)
time.sleep(.5)
x = ltcob.read_data(20)
print(float(x)/1024)



'''
import config
import output_obj
import time

c_output0 = output_obj.output_container(config.output0, 0)

while(1):
    c_output0.value(0)
