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

   def check_conv(self):
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

      while (process_finished == 0):
         time.sleep(0.1)
         owned = self.__spi.try_lock()
         while owned:
            self.__spi.configure(baudrate=1000000, phase=0, polarity=0)
            self.__cs.value = False
            self.__spi.write_readinto(datatowrite, return_data)
            self.__cs.value = True
            process_finished = return_data[0] & 0x40
            print(process_finished)
      
         self.__spi.unlock()

   def read_data(self, channel) -> None:
      """read_data reads the data from the channel

      :param channel: channel to be read
      :type channel: int
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






      
      


