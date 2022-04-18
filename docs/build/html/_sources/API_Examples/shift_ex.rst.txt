Shift Register Object Usage
============================

Shift Object Purpose
--------------------

The purpose of the shift object is to allow for easy shifting of data into up to 2 cascaded shift registers. The shift object is specifically setup for the CD74HC595 and tested exclusively with this model. Functions may need to be altered to allow for other shift registers. 

Code Examples
+++++++++++++

The first examples shows how to initialize the object. The user must provide the inputs for the Storage Register Clock (RCLK), Output Enable (:math:`\overline{OE}`), Shift Register Clock (SRCLK), Serial Data Input (SER), and the number of outputs (8 or 16).

The overriding clear (:math:`\overline{SRCLR}`) pin is assumed to be connected to VCC. 

.. code-block:: python
   :caption: Example initilization of object

   import board
   import digitalio
   import shift_object

   #Digital Selection Shift Register
   digital_store = digitalio.DigitalInOut(board.D34)
   digital_enable = digitalio.DigitalInOut(board.D35)
   digital_shift = digitalio.DigitalInOut(board.D33)
   digital_data = digitalio.DigitalInOut(board.D36)
   
   #Declare Pin Direction
   digital_store.direction = digitalio.Direction.OUTPUT
   digital_enable.direction = digitalio.Direction.OUTPUT
   digital_shift.direction = digitalio.Direction.OUTPUT
   digital_data.direction = digitalio.Direction.OUTPUT
   
   #Ensure the shift register starts out in High Impedance mode
   digital_enable.value = True

   # Initialize the input object
   digital_shiftreg = shift_object.shiftregister(digital_store, digital_enable, digital_shift, digital_data, 8)

The shift register must be enabled through the input_container.enable() function. This function will set the :math:`\overline{OE}` pin to low.

.. code-block:: python
   :caption: Using the declared object from above.

   #Enable the shift register
   digital_shiftreg.enable()

The shift register object can shift data while disabled, or enabled. If disabled, the outputs will not reflect the value of the shift register until the shift register is enabled again.

.. code-block:: python
   :caption: Using the declared object from above.

   #Disable the shiftregister
   digital_shiftreg.disable()

   #Shift data into the shift register
   digital_shiftreg.shift(0xFF) #Turns all outputs on

   #Enable the shift register
   digital_shiftreg.enable() 

There is also a function to zero the shift register, which will set all outputs to low.

.. code-block:: python
   :caption: Using the declared object from above.

   #Zero the shift register
   digital_shiftreg.zero()

Finally, there is a function that will return the last value passed to the shift register.

.. code-block:: python
   :caption: Using the declared object from above.

   #Get the last value passed to the shift register
   last_value = digital_shiftreg.data()

   