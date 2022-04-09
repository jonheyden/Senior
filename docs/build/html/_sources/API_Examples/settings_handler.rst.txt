Setting Handler
================

Setting Handler Purpose
-------------------------

The purpose of the setting handler is to configure all of the available inputs, outputs, and PID's when configuration is sent over uart from the uart_container object. 


Code Examples
++++++++++++++

The Setting Handler needs to be initialized with an array of input_containers, output_containers, input_shiftregister, output_shiftregister, relay_shiftregister, digital_shiftregiser, an array of PID containers, and a uart_container. 

This object will then be able to configure each group of objects based on the recieved data from the UART object. 