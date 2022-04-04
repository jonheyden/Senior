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

The first examples shows how to initialize the object. The user must provide the output that's already been declared as pwmio.PWMOut, and the mode. 

.. code-block:: python
   :caption: Example initilization of object

   import board
   import pwmio
   import output_obj

   output0 = pwmio.PWMOut(board.D2)
   mode = 0
   
   # Initialize the input object
   output_object0 = output_obj.output_container(output0, mode)




Using the output_container.value() function will generate an output relative to the mapping of the mode. I.E. if the mode is 2 (0-10VDC) and the value is 50, then the output will be 5VDC. Similarly, if the mode is 0 (4-20mA) and the value is 50, then the output will be 12mA.

.. code-block:: python
   :caption: Using the same output object from above

   >>output_object0.value(50)
   12mA
   

The output object has a output_container.disable() and output_container.enable() function. The disable() function will disable the output by setting the pwmio.PWMOut.duty_cycle() to 0 and set a private __enablebit to 0. 
The output_container.enable() function will set the __enablebit to 1 and call the output_container.value() function, passing in the last value that was set when the output was last enabled. 

.. code-block:: python
   :caption: Using the same output object from above

   >>output_object0.value(50)
   12mA
   >>output_object0.disable()
   0mA
   >>output_object0.value(100)
   0mA
   >>output_object0.enable()
   12mA

The output object has an output_container.update_mode() function. This will check if the mode is actually being changed, and if not, it will update the mode and call the output_container.value() function to update the output with the new the correct scaling.

.. code-block:: python
   :caption: Using the same output object from above

   >>output_object0.value(50)
   12mA
   >>output_object0.update_mode(2) #Change the mode to 0-10VDC
   5VDC

