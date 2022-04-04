Output Object Usage
====================

Output Object Purpose
----------------------

The purpose of the output object is to provide a container that can take a value of 0-100 from the PID Object and translate it to the appropriate scaling for the PWM duty cycle which is from 0 - 65535.

For the 4-20mA output, the value is tranlated from 13107-65535. (Mode 0)

For the 0-5VDC output, the value is translated from 0-32768. (Mode 1)

For the 0-10VDC output, the value is translated from 0-65535. (Mode 2)


Code Examples
++++++++++++++

