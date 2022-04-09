LTC2984 Object Usage
=====================

LTC2984 Object Purpose
-----------------------

This objects purpose exists to provide a simple interface to the LTC2984. There are many different functions of the LTC2984, but for this class, we focus on it's ability to measure thermocouples and RTD's. 



Code Examples
+++++++++++++

The first examples shows how to initialize the object. The user must provide a Chip Select (:math:`\bar{CS}`) pin, and the common pins for SPI communication (MISO, MOSI, SCK). There is an optional interrupt pin, and for the purposes of this object, it is used.  

.. code-block:: python
   :caption: Example initilization of object

   import board
   import busio
   import ltc2984

   #LTC2984 Chip Select Pin
   ltc_cs = digitalio.DigitalInOut(board.D10)
   ltc_cs.direction = digitalio.Direction.OUTPUT
   ltc_cs.value = True #Set high for active low chip select

   ltc_interrupt = digitalio.DigitalInOut(board.D37)
   ltc_interrupt.direction = digitalio.Direction.INPUT
   
   ltcspi = busio.SPI(board.SCK, board.MOSI, board.MISO)
   
   # Initialize the input object
   ltc_obj = ltc2984.ltc2984(ltcspi, ltc_cs, ltc_interrupt)


There are a couple of helper functions to create assignment data for the LTC2984. These assignments assume that the LTC2984 has a cold junction reference on channel 20 for thermocouples, and a sense resistor on channel 2 for RTD's. Please reference the LTC2984 Users Manual for more information on the assignment data if these channels are different for your use. 

For Thermocouples, the ltc2984.generate_thermocouple_assignment_data() function can be used to create the assigment data. The function takes in a value from 1-8 that relates to thermocouple type. 

.. code-block:: python
   :caption: Using the same ltc2984 object from above
  
   """
   Type J = 1
   Type K = 2
   Type E = 3
   Type N = 4
   Type R = 5
   Type S = 6
   Type T = 7
   Type B = 8
   """

   channel3_assignment = ltc_obj.generate_thermocouple_assignment_data(2)

For RTD's, the ltc2984.generate_rtd_assignment_data() function can be used to create the assigment data. The function takes in a value from 10-17 that relates to RTD type, as well as a wire count should it be a 2, 3, or 4 wire device.


.. code-block:: python
   :caption: Using the same ltc2984 object from above
   
   """
   PT 10 = 10
   PT 50 = 11
   PT 100 = 12
   PT 200 = 13
   PT 500 = 14
   PT 1000 = 15
   PT 1000 375 = 16
   NI 120 = 17
   """

   channel8_assignment = ltc_obj.generate_rtd_assignment_data(5,3)


.. note:: Only channels 4, 8, 12, and 16 are available for RTD assignment if the LTC2984 is being configured the same as the hardware documents reference. 


There is a channel assignment function that can be called, which needs to be passed a valid channel number (1-20) as well as valid data. The function can be called with the ltc2984.chan_assignment() function.

.. code-block:: python
   :caption: Using the same ltc9284 object from above and channel assignment data.
   

   ltc_obj.chan_assignment(3, channel3_assignment)
   ltc_obj.chan_assignment(8, channel8_assignment)
   
If the user has a 2k sense resistor and a cold junction diode, these are the configuration values necessary as well as the assignment channels. 

.. code-block:: python
   :caption: Using the same ltc9284 object from above and channel assignment data.

   sense_resistor_constant = (0x1d) | (0x1F4000 << 0) 
   ltc_obj.chan_assignment(2, sense_resistor_constant)

   cold_junction = (0x1c << 27) | (0x1 << 26) | (0x1 << 25) | (0x0 << 24) | (0x1 << 22) | (0x100c49 << 0) 
   ltc_obj.chan_assignment(20, cold_junction)

Once the user has set the channels, conversion requests can be made to the LTC2984. There are multiple functions that will allow the user to request a conversion, and depending on the pins used, the user can request the data in multiple ways. 

The first option is if the user chooses not to wire the interrupt pin. The ltc2984.check_conv() function will return false until the conversion is complete. It will send a request to the LTC2984 and wait for the conversion complete bit to be set. 

.. code-block:: python
   :caption: Using the same ltc9284 object from above and channel assignment data.
   
   #Request conversion for channels 3 and 8
   ltc_obj.chan_conv(3)
   ltc_obj.chan_conv(8)
   #Wait for conversion to complete
   while (not ltc_obj.check_conv()):
      ltc_obj.check_conv()
   #Read the conversion results
   channel3_data = ltc_obj.read_chan(3)
   channel8_data = ltc_obj.read_chan(8)

Another option, using the interrupt pin, lets the user set a hardware interrupt that signifies when the results are ready to be read, allowing the user to do other things but recieve the data as soon as it's ready. The interrupt pin is pulled low when the device is busy, high when it is ready. 

.. code-block:: python
   :caption: Using the same ltc9284 object from above and channel assignment data.
   
   #Request conversion for channels 3 and 8
   ltc_obj.chan_conv(3)
   ltc_obj.chan_conv(8)
   #Wait for conversion to complete
   if (ltc_obj.check_interrupt):
      #Read the conversion results
      channel3_data = ltc_obj.read_chan(3)
      channel8_data = ltc_obj.read_chan(8)
   
The last function will request and convert the channel when it is ready. This function is use to verify functionality but is not reccomended for use in a system. It is only setup to do one channel at a time. 

.. code-block:: python
   :caption: Using the same ltc9284 object from above and channel assignment data.


   channel3_data = convert_and_read(3)
   
