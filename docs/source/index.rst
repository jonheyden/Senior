.. Loop Controller and Remote I/O documentation master file, created by
   sphinx-quickstart on Tue Feb 22 21:09:23 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Loop Controller and Remote I/O's documentation!
==========================================================





Hardware and Schematics Overview
=================================

.. toctree::
   :maxdepth: 1
   :glob:
   :caption: Schematics

   schematics/inputcircuit
   schematics/outputcircuit
   schematics/ltc2984circuit
   schematics/powercircuit
   schematics/relaycircuit



Overview of Controller Function
=================================

.. toctree::
   :maxdepth: 1
   :glob:
   :caption: Placeholder

   contfunction




API Examples
=============

.. toctree::
   :maxdepth: 1
   :glob:
   :caption: API Examples

   API_Examples/input_ex
   API_Examples/output_ex
   API_Examples/pid_ex
   API_Examples/ltc_ex
   API_Examples/shift_ex
   API_Examples/uart_ex
   API_Examples/settings_handler
   API_Examples/settings_text
   API_Examples/in_pid_out


API References
=================

.. toctree::
   :maxdepth: 1
   :glob:
   :caption: API References

   
   API_References/inputob
   API_References/outputob
   API_References/pidob
   API_References/ltc
   API_References/shift
   API_References/uart
   API_References/setting_ob


Function of Onion Omega
=========================

.. toctree::
   :maxdepth: 1
   :glob:
   :caption: Placeholder

   Onion_Omega/*


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
