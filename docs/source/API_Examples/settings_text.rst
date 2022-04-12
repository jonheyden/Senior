How To Format Data for UART
============================

The data needs to be written to a simple txt file, but the formatting is critical to get expected results. 

The order that the data is sent is less critical, so long as all of the data is sent with it's corresponding header. 


Format for Data
----------------



Input Data Format
++++++++++++++++++

The input data is formatted as such:

Mode, Engineering High, Engineering Low

.. code-block:: text
   :caption: input text

   input
   0,0,0
   0,0,0
   0,0,0
   0,0,0
   0,0,0
   0,0,0
   0,0,0
   0,0,0



Output Data Format
++++++++++++++++++

The output data is formatted as such:

Mode, Output Value, Enable

.. code-block:: text
   :caption: output text

   output
   0,0,0
   0,0,0
   0,0,0
   0,0,0
   0,0,0
   0,0,0
   0,0,0
   0,0,0


PID Data Format
++++++++++++++++

The PID data is formatted as such:

kp, ki, kd, min output, max output, min input, max input, sample time, setpoint, mode, enable

.. code-block:: text
   :caption: pid text

   pid
   0,0,0,0,0,0,0,0,0,0,0
   0,0,0,0,0,0,0,0,0,0,0
   0,0,0,0,0,0,0,0,0,0,0
   0,0,0,0,0,0,0,0,0,0,0
   0,0,0,0,0,0,0,0,0,0,0
   0,0,0,0,0,0,0,0,0,0,0
   0,0,0,0,0,0,0,0,0,0,0
   0,0,0,0,0,0,0,0,0,0,0



Relay Data Format
++++++++++++++++++

The relay data is formatted as such:

Off = 0, On = 1

.. code-block:: text
   :caption: relay text


   relay
   0
   0
   0
   0
   0
   0
   0
   0


Digital Data Format
+++++++++++++++++++

The digital data is formatted as such:

Off = 0, On = 1

.. code-block:: text
   :caption: digital text

   digital
   0
   0
   0
   0
   0
   0
   0
   0

LTC2984 Data Format
+++++++++++++++++++

The LTC data is formatted as such:

Sensor Type, Sensor Type, Sensor Type, Sensor Type


.. code-block:: text
   :caption: ltc text

   ltc
   0,0,0,0
   0,0,0,0
   0,0,0,0
   0,0,0,0

.. note:: The channels start from 3 and go to 18. All the channels can be configured for thermocouples or RTD's. If a bank is set for RTD's, the first value in the bank will be the type of RTD, and the second the wire count. 


Examples of Configuration Values:
---------------------------------


Input Configuration Example
+++++++++++++++++++++++++++


The input data has three inputs. The first is the mode, the second is the low engineering value related to the low of the input, and the third is the high engineering value related to the high of the sensor.

The example below is configuring Input 0 and input 5 with the following configurations:

Input 0 - 4-20mA, 20, 400

Input 5 - 0-10VDC, -30, 120

.. code-block:: text
   :caption: input text

   input
   0,20,400
   0,0,0
   0,0,0
   0,0,0
   0,0,0
   2,-30,120
   0,0,0
   0,0,0


Output Configuration Example
++++++++++++++++++++++++++++

The output data has three inputs. The first is the mode, the second is the manually commanded output value from 0-100 (if this value is less than 0, the PID is expected to update the output value), and the third is the enable. The output data is configured as follows:

The example below is configuring Output 1 and Output 7 with the following configurations:

Output 1 - 0-10VDC, PID control, enabled

Output 7 - 0-5VDC, Manual Control, disabled

.. code-block:: text
   :caption: output text

   output
   0,0,0
   2,-1,1
   0,0,0
   0,0,0
   0,0,0
   0,0,0
   0,0,0
   1,50,0


PID Configuration Example
+++++++++++++++++++++++++

The PID data is formatted as such:

kp, ki, kd, min output, max output, min input, max input, sample time, setpoint, mode, enable

The example below is configuring PID 3 with the following configuration:

PID 3 - 1, .1, .1, 10, 90, -30, 120, .5, 60, Auto, Enabled

.. code-block:: text
   :caption: pid text

   pid
   0,0,0,0,0,0,0,0,0,0,0
   0,0,0,0,0,0,0,0,0,0,0
   0,0,0,0,0,0,0,0,0,0,0
   1,.1,.1,10,90,-30,120,.5,60,1,1
   0,0,0,0,0,0,0,0,0,0,0
   0,0,0,0,0,0,0,0,0,0,0
   0,0,0,0,0,0,0,0,0,0,0
   0,0,0,0,0,0,0,0,0,0,0


Relay Configuration Example
++++++++++++++++++++++++++++

The example below is configuring relay 3 and 4 to be turned on.

.. code-block:: text
   :caption: relay text


   relay
   0
   0
   0
   1
   1
   0
   0
   0


Digital Output Configuration Example
++++++++++++++++++++++++++++++++++++

The example below is configuring the digital outputs 2 and 6 to be on. 

.. code-block:: text
   :caption: digital text

   digital
   0
   0
   1
   0
   0
   0
   1
   0



LTC2984 Configuration Example
++++++++++++++++++++++++++++++

The example below is configuring Bank 0 and Bank 2:

Bank 0 - type k, type j, none, none

Bank 2 - PT 1000, 3 wire, n/a, n/a

.. code-block:: text
   :caption: ltc text

   ltc
   2,1,0,0
   0,0,0,0
   15,3,0,0
   0,0,0,0

