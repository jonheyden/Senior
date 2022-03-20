import time

class shiftregister:
   
   def __init__(self, store, enable, shift, serial_out, outputs) -> None:
      """__init__ initializes the shift register object.

      :param store: Storage Register clock pin
      :type store: DigitalInOut
      :param enable: OE pin
      :type enable: DigitalInOut
      :param shift: Shift Register clock pin
      :type shift: DigitalInOut
      :param data: Data Pin
      :type data: DigitalInOut
      :param outputs: Number of outputs (8 or 16)
      :type outputs: Integer
      """      
      self.__store = store
      self.__enable = enable
      self.__shift = shift
      self.__serial_out = serial_out
      self.__outputs = outputs
      self.__flag = 0
      self.__new_data = 0
      self.__current_data = 0
      #initialize pins to 0
      self.__enable.value = False
      self.__shift.value = False
      self.__serial_out.value = False
      self.__store.value = False


   def enable(self) -> None:
      """enable Enables the OE pin.
      :returns: None
      """
      if self.__enable.value == False:
         self.__enable.value = True

   def disable(self) -> None:
      """disable Disables the OE pin.
      :returns: None
      """      
      if self.__enable.value == True:
         self.__enable.value = False
      
   def __shift_data(self, data) -> None: 
      """__shift_data Private Method used to shift data into the shift register.

      :param data: Data to be shifted
      :type data: Integer
      :returns: None
      """
      for i in range(self.__outputs):
         self.__serial_out.value = bool((data >> i) & 1)
         time.sleep(200e-9)
         self.__shift.value = True
         time.sleep(200e-9)
         self.__shift.value = False
      
   def __store_data(self) -> None:
      """__store_data Stores data from the shift register into the storage register.
      :returns: None
      """
      self.__store.value = True
      time.sleep(200e-9)
      self.__store.value = False


   def update(self, data) -> None:
      """update Checks if data is new, sets a flag.
      
      :param data: Data to be checked and used to update the shift register
      :type data: Integer
      :returns: None
      """      
      if data != self.__current_data:
         self.__new_data = data
         self.__flag = 1
      if self.__flag == 1:
         self.__shift_data(self.__new_data)
         self.__store_data()
         self.__current_data = self.__new_data
         self.__serial_out.value = False
         self.__flag = 0

   def zero(self) -> None:
      """zero Sets the shift register to 0.
      :returns: None
      """      
      if self.__outputs == 8:
         self.update(0b00000000)
      else:
         self.update(0b0000000000000000)

   def data(self) -> int:
      """data Returns the current data in the shift register.
      :returns: Integer
      """      
      return self.__current_data

   