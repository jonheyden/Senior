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

If the user wants to change the values on the fly, they can do so by inserting the uart_container.check_buffer() function into the loop. This function will check the buffer for any new values and update each element as necessary.

.. code-block:: python
   :caption: Using the same objects from above

   import busio
   import uart_object

   uart = busio.UART(board.TX, board.RX, baudrate=9600)
   uart_object = uart_object.uart_container(uart)


   while True:
      uart_object.check_buffer()
      output_object0.value(PID_0.update(input_object0.get_input()))