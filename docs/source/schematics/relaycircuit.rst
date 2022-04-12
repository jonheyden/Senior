Relay and Digital Out Circuits
==============================


Role of the Shift Register
---------------------------
For both the relay and digital output circuits, a CD74HC595 is used to expand the outputs from the Teensy 4.1. 

The shift registers allow the user to take 4 output pins and turn them into 8 at the cost of time required to shift.
 
These shift registers were seperated but if the microcontroller is short on outputs, the QH' from one could be fed into the SER of the other. Further, the OE, SRCLK, and CLK can be tied which would reduce the required number of pins from 8 to 4. This means that 4 output pins would effectively become 16, again at the cost of the time it takes to shift through the two registers. 

Relay Circuits
---------------
The relay circuits simply allow for a signal to be sent into one end and output through to act as a dry contact relay. They have a 700mA rating, but should be derated to 500mA for precaution and efficiency. 

Digital Output Circuit
----------------------
The Digital Outputs drain is connected to the 24VDC potential supplied to the board. When the OptoMos is turned on, it allows 24VDC to pass and supply voltage. Again, these have a 700mA rating but should be derated to 500mA for precaution and efficiency. 

Parts
-----

All resistors are the same 470:math:`\Omega` value.


:download:`CD74HC595 <../datasheets/Relays/CD74.pdf>`

.. image:: ../images/relay_dig_cir.jpg
   :width: 500
   :alt: Relay and Ditigal Out Circuit
   :align: center