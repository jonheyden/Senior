UART Object Usage
==================

Uart Object Purpose
--------------------
The purpose of the Uart object is to catch the data from the Onion Omega before it is passed to the Setting Handler which actually will configure the other container objects. 

Code Examples
+++++++++++++

The first examples shows how to initialize the object. All the user must do is provide a declared busio.uart object. 

.. code-block:: python
   :caption: Example initilization of object

   import board
   import busio

   onionuart = busio.UART(board.TX1, board.RX1, baudrate=115200)
   
   # Initialize the uart object
   uart_obj = uart_obj.uart_container(onionuart)

The only function available for the user is the uart_container.check_buffer() function. This functions allows the user to check if there is data, convert the data, and pass it along for further processing. 
This allows for more dynamic programming as the user won't have to wait for all of the data to be recieved at once. 

.. code-block:: python
   :caption: Using the object from above

   
   #Check buffer and write to arrays.
   uart_obj.check_buffer()
