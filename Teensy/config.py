""" This File is used to initialize the hardware. 
   --------------------------------------------------

"""

import board
import busio
import pwmio
import digitalio
import pwmio
import analogio

#Inputs
input0 = analogio.AnalogIn(board.A9)
input1 = analogio.AnalogIn(board.A8)
input2 = analogio.AnalogIn(board.A7)
input3 = analogio.AnalogIn(board.A6)
input4 = analogio.AnalogIn(board.A5)
input5 = analogio.AnalogIn(board.A4)
input6 = analogio.AnalogIn(board.A3)
input7 = analogio.AnalogIn(board.A2)

#Outputs
output0 = pwmio.PWMOut(board.D2)
output1 = pwmio.PWMOut(board.D3)
output2 = pwmio.PWMOut(board.D4)
output3 = pwmio.PWMOut(board.D5)
output4 = pwmio.PWMOut(board.D6)
output5 = pwmio.PWMOut(board.D7)
output6 = pwmio.PWMOut(board.D8)
output7 = pwmio.PWMOut(board.D9)

#Input Selection Shift Register
input_store = digitalio.DigitalInOut(board.D14)
input_enable = digitalio.DigitalInOut(board.D41)
input_shift = digitalio.DigitalInOut(board.D15)
input_data = digitalio.DigitalInOut(board.D40)

#Output Selection Shift Register
output_store = digitalio.DigitalInOut(board.D26)
output_enable = digitalio.DigitalInOut(board.D25)
output_shift = digitalio.DigitalInOut(board.D27)
output_data = digitalio.DigitalInOut(board.D24)


#Relay Selection Shift Register
relay_store = digitalio.DigitalInOut(board.D31)
relay_enable = digitalio.DigitalInOut(board.D30)
relay_shift = digitalio.DigitalInOut(board.D32)
relay_data = digitalio.DigitalInOut(board.D29)

#Digital Selection Shift Register
digital_store = digitalio.DigitalInOut(board.D34)
digital_enable = digitalio.DigitalInOut(board.D35)
digital_shift = digitalio.DigitalInOut(board.D33)
digital_data = digitalio.DigitalInOut(board.D36)

#Onion RX/TX
onionuart = busio.UART(board.TX1, board.RX1, baudrate=9600)

#LTCSPI
ltc_cs = digitalio.DigitalInOut(board.D10)
ltc_cs = digitalio.Direction.OUTPUT
ltcspi = busio.SPI(board.SCK, board.MOSI, board.MISO)

#digitalio direction declarations
input_store.direction = digitalio.Direction.OUTPUT
input_enable.direction = digitalio.Direction.OUTPUT
input_shift.direction = digitalio.Direction.OUTPUT
input_data.direction = digitalio.Direction.OUTPUT

output_store.direction = digitalio.Direction.OUTPUT
output_enable.direction = digitalio.Direction.OUTPUT
output_shift.direction = digitalio.Direction.OUTPUT
output_data.direction = digitalio.Direction.OUTPUT

relay_store.direction = digitalio.Direction.OUTPUT
relay_enable.direction = digitalio.Direction.OUTPUT
relay_shift.direction = digitalio.Direction.OUTPUT
relay_data.direction = digitalio.Direction.OUTPUT

digital_store.direction = digitalio.Direction.OUTPUT
digital_enable.direction = digitalio.Direction.OUTPUT
digital_shift.direction = digitalio.Direction.OUTPUT
digital_data.direction = digitalio.Direction.OUTPUT

#Input Shift Register Configuration Constants
'''
input0_420 = 0b10000000
input1_420 = 0b01000000
input2_420 = 0b00100000
input3_420 = 0b00010000
input4_420 = 0b00001000
input5_420 = 0b00000100
input6_420 = 0b00000010
input7_420 = 0b00000001
'''

input_currentMode = [
   0b10000000, 
   0b01000000, 
   0b00100000, 
   0b00010000,
   0b00001000, 
   0b00000100, 
   0b00000010, 
   0b00000001]

#Output Shift Register Configuration Constants
'''
output0_420 = 0b0000000000000001
output1_420 = 0b0000000000000100
output2_420 = 0b0000000000010000
output3_420 = 0b0000000001000000
output4_420 = 0b0000000100000000
output5_420 = 0b0000010000000000
output6_420 = 0b0001000000000000
output7_420 = 0b0100000000000000
'''
output_currentMode = [
   0b0000000000000001, 
   0b0000000000000100, 
   0b0000000000010000, 
   0b0000000001000000, 
   0b0000000100000000, 
   0b0000010000000000, 
   0b0001000000000000,
   0b0100000000000000]

'''
output0_vcc = 0b0000000000000010
output1_vcc = 0b0000000000001000
output2_vcc = 0b0000000000100000
output3_vcc = 0b0000000010000000
output4_vcc = 0b0000001000000000
output5_vcc = 0b0000100000000000
output6_vcc = 0b0010000000000000
output7_vcc = 0b1000000000000000
'''

output_vccMode = [0b0000000000000010, 0b0000000000001000, 0b0000000000100000, 0b0000000010000000, 0b0000001000000000, 0b0000100000000000, 0b0010000000000000, 0b1000000000000000]

