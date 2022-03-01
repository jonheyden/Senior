""" This File is used to initialize the hardware. 
   --------------------------------------------------

"""

import board
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
