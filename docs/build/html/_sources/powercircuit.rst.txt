Power Circuit
=============

5V and 3.3V Power Supply
------------------------
The Teensy 4.1 takes a 5V power supply, as the Teensy 4.1 is normally powered by USB which provides 5V from a computer or wall outlet. 

Both the Onion Omega 2+ and the LTC2984 are powered from 3.3VDC. Because of this, it was necessary to provide power supplies for both voltage levels. 

The recommendations for capcitors, inductors, and layout were all directly taken from the Traco Power Datasheets which can be found below. 

Fuse blocks were used to easily protect the power supplies, as well as the digital output circuits. 

Parts
-----
:download:`TSR2-2433 and TSR2-2450 <datasheets/Power/TSR.pdf>`

:download:`Fuse Blocks <datasheets/Power/Fuse.pdf>`


.. image:: images/power_cir.jpg
   :width: 500
   :alt: Power Circuit
   :align: center