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



'''

# Write your code here :-)
# Write your code here :-)
"""CircuitPython Essentials: PWM with Fixed Frequency example."""
import time
import board
import pwmio
import digitalio
import shift_object
# LED setup for most CircuitPython boards:
#led = pwmio.PWMOut(board.LED, frequency=3411, duty_cycle=0)
# LED setup for QT Py M0:
# led = pwmio.PWMOut(board.SCK, frequency=5000, duty_cycle=0)






input_store = digitalio.DigitalInOut(board.D14)
input_store.direction = digitalio.Direction.OUTPUT

input_enable = digitalio.DigitalInOut(board.D41)
input_enable.direction = digitalio.Direction.OUTPUT

input_shift = digitalio.DigitalInOut(board.D15)
input_shift.direction = digitalio.Direction.OUTPUT

input_data = digitalio.DigitalInOut(board.D40)
input_data.direction = digitalio.Direction.OUTPUT


input_shiftreg = shift_object.shiftregister(input_store, input_enable, input_shift, input_data, 8)

input_shiftreg.enable()




while True:
   time.sleep(10)
   input_shiftreg.update(0b11111111)
   time.sleep(10)
   input_shiftreg.update(0b00000000)
   time.sleep(10)
   input_shiftreg.update(0b01010101)
   time.sleep(10)
   input_shiftreg.update(0b00000000)
   time.sleep(10)
   input_shiftreg.update(0b10101010)

