Input Object Usage
==================


Input Object Purpose
--------------------

The purpose of the input object is to provide a container that takes care of scaling for input into the PID Object. There is an analog conversion on the hardware taking place that will map the values of 4-20mA to a range of roughly 1-3.3VDC.(Mode 0)

For the 0-5VDC range the mapped voltage will be between 0-1.65VDC. (Mode 1)

For the 0-10VDC range the mapped voltage will be between 0-3.3VDC. (Mode 2)

For values of 0VDC and 24VDC, the value will be either 0 or 3.3VDC. (Mode 3)

Code Examples
+++++++++++++

The first examples shows how to initialize the object. The user must provide the input that's already been declared as analogio.AnalogIn, scaling units, and the mode. 

.. code-block:: python
   :caption: Example initilization of object

   import board
   import analogio
   import input_obj

   input0 = analogio.AnalogIn(board.A9)
   engHigh = 300 
   engLow = 20
   mode = 0
   
   # Initialize the input object
   input_object0 = input_obj.input_container(input0, engHigh, engLow, mode)

Using the input_object.value() function will return a value in engineering units based on the scaling. For example, if the unit was recieving 12mA:

.. code-block:: python
   :caption: Using the same input object from above

   >>input_object0.value()
   160.0

If the user changes the input sensor, they can update the object with new engineering values using the input_object.update() function.

.. code-block:: python
   :caption: Using the same input object from above

   enghigh = 500
   englow = 0
   mode = 0
   input_object0.update(enghigh,englow,mode)
   
