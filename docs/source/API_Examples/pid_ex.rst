PID Object Usage
=================

The PID Object is used to generate a simple PID algorithm that can autocorrect a system to a setpoint. Once the PID object is initiliazed, there are a handful of setter functions that allow the user to set the gains, setpoint, and other parameters.

.. note:: The PID Object was heavily inspired by the simple-pid library located at: https://github.com/m-lundberg/simple-pid . 


.. code-block:: python
   :caption: Example initilization of object

   import pid_object


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

This only initializes the PID object. By default, the object is disabled and the setpoint is set to 0. The PID object can be enabled by calling the pid_object.enable() function, and the setpoint can be set by calling the pid_object.set_setpoint() function.

.. code-block:: python
   :caption: Using the same PID object from above

   >>PID_0.set_setpoint(150)
   >>PID_0.enable()

The PID Object has both a manual mode and auto mode. By default, the PID object starts in manual mode. The output can be set with the pid_object.set_output() function. To return the value of the output, the pid_object.get_output() function can be used.

.. code-block:: python
   :caption: Using the same PID object from above

   >>PID_0.set_output(80)
   >>PID_0.get_output()
   80

Auto mode can be set by calling the pid_object.set_auto() function. The PID will then require a different function to be called to update the PID. The pid_object.update() which needs to be passed the current value of the system. This can be done with a static value or the return of another object. 

.. code-block:: python
   :caption: Using the same PID object from above

   >>PID_0.set_auto()
   >>PID_0.update(150)

Manual mode can be turned back on by calling the pid_object.set_manual() function.

.. code-block:: python
   :caption: Using the same PID object from above

   >>PID_0.set_manual()

Further, the ki, kp, and kd parameters can all be set with their own setter functions. The sampleing time can also be updated with it's setter parameter, in case the PID needs to be faster or slower in updating the algorithm.

.. code-block:: python
   :caption: Using the same PID object from above

   >>PID_0.set_kp(5)
   >>PID_0.set_ki(1)
   >>PID_0.set_kd(.4)
   >>PID_0.set_sample_time(1000) #in terms of milliseconds