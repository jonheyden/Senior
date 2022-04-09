import time


class ltc2984:
   
   def __init__(self, spi_ob, cs, interrupt) -> None:
      """__init__ initalizes the ltc2984 object

      :param spi_ob: spi object
      :type spi_ob: busio.SPI
      :param cs: digital pin for CS
      :type cs: digitalio.DigitalInOut
      :param interrupt: digital pin for interrupt
      :type interrupt: digitalio.DigitalInOut
      """      
      self.__spi = spi_ob
      self.__cs = cs
      self.__interrupt = interrupt
      self.__read = 3
      self.__write = 2

   def generate_thermocouple_assignment(self, value) -> int:
      """generate_thermocouple_assignment Generates values to assign thermocouple


      :param value: Thermocouple Type
      :type value: int
      :return: 32 bit data
      :rtype: int
      """      
      if value >= 1 and value <= 8:
         return (value << 27) | (0x14 << 22) | (0x1 << 21) | (0x0 << 21) | (0x0 << 18)
      

   def generate_RTD_assignment(self, value, wire_count) -> int:
      """generate_RTD_assignment Generates values to assign RTD

      :param value: type of RTD
      :type value: int
      :param wire_count: wire count 2-4
      :type wire_count: int
      :return: 32 bit data
      :rtype: int
      """      

      if wire_count == 2:
         return (value << 27 ) | (0x0 << 22) | (0x1 << 20) | (0x1 << 18) | (0x7 << 14) | (0x1 << 12)
      if wire_count == 3:
         return (value << 27 ) | (0x1 << 22) | (0x1 << 20) | (0x1 << 18) | (0x7 << 14) | (0x1 << 12)
      if wire_count == 4:
         return (value << 27 ) | (0x2 << 22) | (0x1 << 20) | (0x1 << 18) | (0x7 << 14) | (0x1 << 12)      

   def chan_assignment(self, channel, data) -> None:
      """chan_assignment assigns channel

      :param channel: Channel number from 1-20
      :type channel: int
      :param data: 32 bit data
      :type data: long
      """      
      address = 0x0200 + (channel-1)*4
      address_high = (address >> 8) & 0xFF
      address_low = (address & 0xFF)
      datatowrite = bytearray(7)
      datatoreturn = bytearray(7)

      # datatowrite[6] = self.__write
      # datatowrite[5] = address_high
      # datatowrite[4] = address_low
      # datatowrite[3] = (data >> 24) & 0xFF
      # datatowrite[2] = (data >> 16) & 0xFF
      # datatowrite[1] = (data >> 8) & 0xFF
      # datatowrite[0] = (data >> 0) & 0xFF
      
      datatowrite[0] = self.__write
      datatowrite[1] = address_high
      datatowrite[2] = address_low
      datatowrite[3] = (data >> 24) & 0xFF
      datatowrite[4] = (data >> 16) & 0xFF
      datatowrite[5] = (data >> 8) & 0xFF
      datatowrite[6] = (data >> 0) & 0xFF      

      owned = self.__spi.try_lock()

      if owned:
         if (self.__interrupt.value == True):
            self.__spi.configure(baudrate=1000000, phase=0, polarity=0)
            self.__cs.value = False
            self.__spi.write_readinto(datatowrite, datatoreturn)
            self.__cs.value = True
         else:
            print("Interrupt busy")
            self.__spi.unlock()
            return
      else:
         print("SPI Not Locked")
         return
      self.__spi.unlock()

      
   def chan_conv(self, channel) -> None:
      """chan_conv requests a channel conversion

      :param channel: channel to be converted
      :type channel: int
      """      

      address = 0x0000
      address_high = (address >> 8) & 0xFF
      address_low = (address & 0xFF)

      datatowrite = bytearray(4)
      # datatowrite[3] = self.__write
      # datatowrite[2] = address_high
      # datatowrite[1] = address_low
      # datatowrite[0] = (0x80 | channel) & 0xFF
      
      datatowrite[0] = self.__write
      datatowrite[1] = address_high
      datatowrite[2] = address_low
      datatowrite[3] = (0x80 | channel) & 0xFF

      owned = self.__spi.try_lock()

      if owned:
         if (self.__interrupt.value == True):
            self.__spi.configure(baudrate=1000000, phase=0, polarity=0)
            self.__cs.value = False
            self.__spi.write(datatowrite)
            self.__cs.value = True
         else:
            print("Interrupt busy")
            self.__spi.unlock()
            return
      else:
         print("SPI Not Locked")
         return
      self.__spi.unlock()

   def check_interrupt(self) -> bool:
      """check_interrupt Checks if interrupt high or low

      :return: True if interrupt not busy, False if interrupt busy
      :rtype: bool
      """      
      return self.__interrupt.value

   def check_conv(self):
      """check_conv Checks if conversion is complete
      """      
      process_finished = 0
      return_data = bytearray(4)
      datatowrite = bytearray(4)

      address = 0x0000
      address_high = (address >> 8) & 0xFF
      address_low = (address & 0xFF)

      # datatowrite[3] = self.__read
      # datatowrite[2] = address_high
      # datatowrite[1] = address_low
      # datatowrite[0] = 0x00

      datatowrite[0] = self.__read
      datatowrite[1] = address_high
      datatowrite[2] = address_low
      datatowrite[3] = 0x00

      counttoescape = 0
      while (process_finished == 0 and counttoescape < 10):
         time.sleep(0.1)
         owned = self.__spi.try_lock()
         if owned:
            self.__spi.configure(baudrate=1000000, phase=0, polarity=0)
            self.__cs.value = False
            self.__spi.write_readinto(datatowrite, return_data)
            self.__cs.value = True
            process_finished = return_data[3] & 0x40
            if (process_finished == 0x40):
               self.__spi.unlock()
               return True
         else:
            print("SPI Not Locked or Conversion incomplete")
            self.__spi.unlock()
            return False

   def read_data(self, channel) -> float:
      """read_data Reads data from the requested ram location

      :param channel: Channel to be checked
      :type channel: int (0-20)
      :return: Data from requested ram location
      :rtype: float
      """

      address = 0x0010 + (channel-1)*4
      address_high = (address >> 8) & 0xFF
      address_low = (address & 0xFF)
      datatowrite = bytearray(7)
      datatoreturn = bytearray(7)

      # datatowrite[6] = self.__read
      # datatowrite[5] = address_high
      # datatowrite[4] = address_low
      # datatowrite[3] = 0
      # datatowrite[2] = 0
      # datatowrite[1] = 0
      # datatowrite[0] = 0

      datatowrite[0] = self.__read
      datatowrite[1] = address_high
      datatowrite[2] = address_low
      datatowrite[3] = 0
      datatowrite[4] = 0
      datatowrite[5] = 0
      datatowrite[6] = 0      

      owned = self.__spi.try_lock()

      if owned:
         if (self.__interrupt.value == True):
            self.__spi.configure(baudrate=1000000, phase=0, polarity=0)
            self.__cs.value = False
            self.__spi.write_readinto(datatowrite, datatoreturn)
            self.__cs.value = True
         else:
            print("Interrupt busy")
            self.__spi.unlock()
            return
      else:
         print("SPI Not Locked")
         return
      self.__spi.unlock()

      return_data = (datatoreturn[3] << 24) | (datatoreturn[4] << 16) | (datatoreturn[5] << 8) | (datatoreturn[6] << 0)

      
      return return_data & 0xFFFFFF

   def convert_and_read(self, channel) -> float:
      """convert_and_read Performs a channel conversion and reads the data

      :param channel: Channel to be checked
      :type channel: int (0-20)
      :return: Data from requested ram location
      :rtype: float
      """
      self.chan_conv(channel)
      while(not self.check_interrupt()):
         time.sleep(0.1)

      temp = ((self.read_data(channel)/1024)*(9/5))+32
      return temp







      
      


