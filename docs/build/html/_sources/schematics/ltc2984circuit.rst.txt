LTC2984 Circuit
===============


LTC2984
-------
The LTC2984 is a multi-sensor high accuracy digital temperature measurement system. It is capable of measuring a range of temperature instruments (TI) too broad to cover in this documentation. 

The focus of this project is on Thermocouples and RTD's. THe configuration of the circuit is such that it allows for 4 universal banks of a mixture of thermocouples and RTD's.

The LTC2984 itself has 20 channels of temperature measurement. This is reduced to 19 when considering the need for a dedicated cold-reference junction. It is possible, if the user knows exactly what configurations are going to be used, to disregard the cold-reference in favor of using one of the measurement channels as a cold-reference as well. 

The capacitors attached to the LTC2984 are the recommendations of the manufacturer which can be found in the datasheet below. 

Each channel has an input resistor of :math:`100{\Omega}` as protection and current-limiting. Further, each channel has input filter capcitors based on manufacturer recommendations and reference schematics. 


Cold Junction Reference
------------------------
The working principle of a thermocouple is based on the Peltier Effect. In layman's terms, two dissimilar metals are joined together to form a junction. This junction is then heated, which produces a voltage. The voltage across the junction is then used to relate back to a temperature, as the voltage can be related back with the material properties of the two metals. 

A cold junction reference is necessary as the thermocouples create a second and third junction at the terminals of the PCB. Another reference has to be taken near the terminals to ensure the unintended junctions don't interfere with the temperature measurement. 

A cold junction reference was created with a simple 2N3904 BJT that ties it's base to the collector. 


Parts
-----
:download:`LTC2984 <../datasheets/LTC2984/LTC2984Datasheet.pdf>`

:download:`PZT3904 <../datasheets/LTC2984/PZT3904.pdf>`

.. image:: ../images/ltc_cir.jpg
   :width: 500
   :alt: LTC2984 Circuit
   :align: center