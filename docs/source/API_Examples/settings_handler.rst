Setting Handler
================

Setting Handler Purpose
-------------------------

The purpose of the setting handler is to configure all of the available inputs, outputs, and PID's when configuration is sent over uart from the uart_container object. 


Code Examples
++++++++++++++

The Setting Handler needs to be initialized with an array of input_containers, output_containers, input_shiftregister, output_shiftregister, relay_shiftregister, digital_shiftregiser, an array of PID containers, and a uart_container. 

This object will then be able to configure each group of objects based on the recieved data from the UART object. 

An example for initializing the setting_container

.. code-block:: python
   :caption: Initializing the setting_container
   
   def init():
   """ Initializes objects from classes
   """
   global input_shiftreg
   input_shiftreg = shift_object.shiftregister(c.input_store, c.input_enable, c.input_shift, c.input_data, 8)

   global output_shiftreg
   output_shiftreg = shift_object.shiftregister(c.output_store, c.output_enable, c.output_shift, c.output_data, 16)

   global relay_shiftreg
   relay_shiftreg = shift_object.shiftregister(c.relay_store, c.relay_enable, c.relay_shift, c.relay_data, 8)

   global digital_shiftreg
   digital_shiftreg = shift_object.shiftregister(c.digital_store, c.digital_enable, c.digital_shift, c.digital_data, 8)

   global uart_obj
   uart_obj = uart_obj.uart_container(c.onionuart)

   global ltc_obj
   ltc_obj = ltc2984.ltc2984(c.ltcspi, c.ltc_cs, c.ltc_interrupt)
   sense_resistor_constant = (0x1d) | (0x1F4000 << 0) 
   ltc_obj.chan_assignment(2, sense_resistor_constant)
   cold_junction = (0x1c << 27) | (0x1 << 26) | (0x1 << 25) | (0x0 << 24) | (0x1 << 22) | (0x100c49 << 0) 
   ltc_obj.chan_assignment(20, cold_junction)

   global output0_obj
   output0_obj = output_obj.output_container(c.output0,0)

   global output1_obj
   output1_obj = output_obj.output_container(c.output1,0)

   global output2_obj
   output2_obj = output_obj.output_container(c.output2,0)

   global output3_obj
   output3_obj = output_obj.output_container(c.output3,0)

   global output4_obj
   output4_obj = output_obj.output_container(c.output4,0)

   global output5_obj
   output5_obj = output_obj.output_container(c.output5,0)

   global output6_obj
   output6_obj = output_obj.output_container(c.output6,0)

   global output7_obj
   output7_obj = output_obj.output_container(c.output7,0)

   global input0_obj
   input0_obj = input_obj.input_container(c.input0,0)

   global input1_obj
   input1_obj = input_obj.input_container(c.input1,0)

   global input2_obj
   input2_obj = input_obj.input_container(c.input2,0)

   global input3_obj
   input3_obj = input_obj.input_container(c.input3,0)

   global input4_obj
   input4_obj = input_obj.input_container(c.input4,0)

   global input5_obj
   input5_obj = input_obj.input_container(c.input5,0)

   global input6_obj
   input6_obj = input_obj.input_container(c.input6,0)

   global input7_obj
   input7_obj = input_obj.input_container(c.input7,0)

   global in_container
   in_container = [input0_obj, input1_obj, input2_obj, input3_obj, input4_obj, input5_obj, input6_obj, input7_obj]

   global out_container
   out_container = [output0_obj, output1_obj, output2_obj, output3_obj, output4_obj, output5_obj, output6_obj, output7_obj]

   global pid_obj0
   pid_obj0 = pid_object.PID_Object(0,0,0,0,100,0,100,500)

   global pid_obj1
   pid_obj1 = pid_object.PID_Object(0,0,0,0,100,0,100,500)

   global pid_obj2
   pid_obj2 = pid_object.PID_Object(0,0,0,0,100,0,100,500)

   global pid_obj3
   pid_obj3 = pid_object.PID_Object(0,0,0,0,100,0,100,500)

   global pid_obj4
   pid_obj4 = pid_object.PID_Object(0,0,0,0,100,0,100,500)

   global pid_obj5
   pid_obj5 = pid_object.PID_Object(0,0,0,0,100,0,100,500)

   global pid_obj6
   pid_obj6 = pid_object.PID_Object(0,0,0,0,100,0,100,500)

   global pid_obj7
   pid_obj7 = pid_object.PID_Object(0,0,0,0,100,0,100,500)

   global pid_container
   pid_container = [pid_obj0, pid_obj1, pid_obj2, pid_obj3, pid_obj4, pid_obj5, pid_obj6, pid_obj7]

   global settings_obj
   settings_obj = settings_handler.setting_container(in_container, out_container, input_shiftreg, output_shiftreg, relay_shiftreg, digital_shiftreg, pid_container, ltc_obj)

   return