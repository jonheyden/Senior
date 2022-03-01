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
      self.store = store
      self.__enable = enable
      self.shift = shift
      self.__serial_out = serial_out
      self.outputs = outputs
      self.flag = 0
      self.new_data = 0
      self.__current_data = 0
   


   def enable(self) -> None:
      """enable Enables the OE pin.
      :returns: None
      """
      self.__enable.value = True

   def disable(self) -> None:
      """disable Disables the OE pin.
      :returns: None
      """      
      self.__enable.value = False
      
   def __shift_data(self, data) -> None: 
      """__shift_data Private Method used to shift data into the shift register.

      :param data: Data to be shifted
      :type data: Integer
      :returns: None
      """
      for i in range(self.outputs):
         self.__serial_out.value = data >> i & 1
         time.sleep(200e-9)
         self.shift.value = True
         time.sleep(200e-9)
         self.shift.value = False
      
   def __store_data(self) -> None:
      """__store_data Stores data from the shift register into the storage register.
      :returns: None
      """
      self.store.value = True
      time.sleep(200e-9)
      self.store.value = False


   def update(self, data) -> None:
      """update Checks if data is new, sets a flag.
      
      :param data: Data to be checked and used to update the shift register
      :type data: Integer
      :returns: None
      """      
      if data != self.__current_data:
         self.new_data = data
         self.flag = 1
      if self.flag == 1:
         self.__shift_data(self.new_data)
         self.__store_data()
         self.__current_data = self.new_data
         self.__serial_out.value = False
         self.flag = 0

