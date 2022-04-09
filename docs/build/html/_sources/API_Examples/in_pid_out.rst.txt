Putting It All Together
========================

This is a simple example of how to use the input_container, output_container, and pid_object in a simple program loop.

.. code-block:: python
   :caption: Example initilization of objects

   import board
   import pwmio
   import analogio
   import input_obj
   import output_obj
   import pid_object

   #Input Declarations
   input0 = analogio.AnalogIn(board.A9)
   engHigh = 300 
   engLow = 20
   mode = 0
   
   # Initialize the input object
   input_object0 = input_obj.input_container(input0, engHigh, engLow, mode)


   #Output Declarations
   output0 = pwmio.PWMOut(board.D2)
   mode = 0
   
   # Initialize the input object
   output_object0 = output_obj.output_container(output0, mode)



   # Initialize the PID object variables
   kp = 1
   ki = 2
   kd = 3
   minOutput = 0 #value from 0 to 100, must be less than maxOutput
   maxOutput = 100 #value from 0 to 100, must be greater than minOutput
   min_input = 20 #must be less than max_input
   max_input = 300 #must be greater than min_input
   sample_time = 500 #must be greater than 0, used to check if PID should be updated. In terms of milliseconds.
   
   # Initialize the input object
   PID_0 = pid_object.pid_object(kp, ki, kd, minOutput, maxOutput, min_input, max_input, sample_time)

   PID_0.set_setpoint(150)
   PID_0.enable()
   PID_0.set_auto()

This next code-block shows the main loop of the program after the objects have been initialized.

.. code-block:: python
   :caption: Using the same objects from above

   while True:
      pid_input = input_object0.value()
      output_input = PID_0.update(pid_input)
      output_object0.value(output_input)



This loop can be simplified to one line of code to continously run the PID loop.

.. code-block:: python
   :caption: Using the same objects from above

   while True:
      output_object0.value(PID_0.update(input_object0.get_input()))

If the user wants to change the values on the fly, they can do so by inserting the uart_container.check_buffer() function into the loop. This function will check the buffer for any new values. Once this is updated, the setting_container can be called to update the values. The uart_container can be used with the uart port, but the values can be written manually as the data arrays are not private. 




.. code-block:: python
   :caption: Using the same objects from above

   import busio
   import uart_object
   import settings_handler
   
   uart = busio.UART(board.TX, board.RX, baudrate=9600)
   uart_object = uart_object.uart_container(uart)



   while True:
      uart_object.check_buffer()
      settings_obj.check_update(uart_object)
      output_object0.value(PID_0.update(input_object0.get_input()))



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

