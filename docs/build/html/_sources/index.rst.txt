.. Loop Controller and Remote I/O documentation master file, created by
   sphinx-quickstart on Tue Feb 22 21:09:23 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Loop Controller and Remote I/O's documentation!
==========================================================

Purpose of the project
++++++++++++++++++++++

The purpose of this project is to create a cost effective solution to expensive industrial controls. Industrial I/O is generally overly priced for what the hardware can actually do. Oftentimes the end-user is paying a premium for the brand name. While other solutions exist in other brands, their markdown is oftentimes not worth the price of trying to integrate another brand. 

This documentation is broken into multiple parts starting with the Hardware.


Hardware and Schematics Overview
+++++++++++++++++++++++++++++++++

Links to the hardware can be found below. These are the schematics that were used to build the intial protoboard for proof-of-concept. These schematics provide a base for circuits with multi-fucntionality in processing and creating analog and digital signals for industrial I/O. 

.. toctree::
   :maxdepth: 1
   :glob:
   :caption: Schematics

   schematics/inputcircuit
   schematics/outputcircuit
   schematics/ltc2984circuit
   schematics/powercircuit
   schematics/relaycircuit



Function of the Teensy
++++++++++++++++++++++++

The Teensy is the heart of the board. It controls all of the I/O as well as the PID calculations. It also handles the SPI communication to the LTC2984, and communicates through UART with the Onion Omega. 

The Teensy 4.1 is capable of 600MHz, as well as being programmable through Circuit Python which was used almost exclusively. 

Besides this, the Teensy 4.1 has a plethora of I/O available that was crucial to the project. Below is an image of the available I/O and a link to `PJRC <https://www.pjrc.com/store/teensy41.html>`_ for more information.

.. image:: images/teensy_side.jpg
   :scale: 50 %
   :alt: Teensy Pins
   :align: center




Function of Onion Omega
++++++++++++++++++++++++

This link provide information relative to the Onion Omega Controller. The Onion Omega is used as a data aggregate and can act as a wifi hotspot capable of allowing wireless access to the controller functionality. 

The Omega was used because it runs an OS in the form of Linux, specifically a distribution called OpenWRT. This was necessary to utilize libraries that can access PLC's, specifically the `pycomm3 library <https://docs.pycomm3.dev/en/latest/>`_ which was used to communicate with the PLC for testing purposes. There are other libraries capable of handling the same functionality, but the pycomm3 library was very simple to use. 

It is also capable of hosting a webpage, which with more work could simplify the users ability to adjust settings. For now, settings are adjusted by connecting to the Omega through the terminal. 


.. toctree::
   :maxdepth: 1
   :glob:
   :caption: Onion Omega Function

   Onion_Omega/*
   API_Examples/settings_text


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
   API_Examples/in_pid_out



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



