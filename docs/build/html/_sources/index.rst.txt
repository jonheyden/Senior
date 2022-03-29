.. Loop Controller and Remote I/O documentation master file, created by
   sphinx-quickstart on Tue Feb 22 21:09:23 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Loop Controller and Remote I/O's documentation!
==========================================================

.. toctree::
   :maxdepth: 2
   :glob:

   
   shift
   pidob
   inputob
   outputob
   ltc
   uart
   schematics



General Flow of the Program on the Teensy
=========================================

Input Container -> PID Object -> Output Container


Jobs of the classes
-------------------

Input Container
+++++++++++++++

- Converts the raw input from the inputs (0-65535) to a value in engineering units.


PID Object
+++++++++++++++

- Takes the engineering unit value from the input container and returns a value from 0-100 which is the value of the output in terms of percent.


Output Container
++++++++++++++++

- Sets the mode of the output pin (4-20mA, 0-10VDC, 0-5VDC).
- Takes the value from 0-100 and ouputs the value to the outputs (0-65535) with regard to the mode it is in.


General Flow of the Program on the Onion Omega
==============================================
