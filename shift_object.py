import time

class shiftregister:
   
   def __init__(self, store, enable, shift, data, outputs) -> None:
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
      self.enable = enable
      self.shift = shift
      self.data = data
      self.outputs = outputs
      self.flag = 0
      self.shift_data = 0

   def enable(self) -> None:
      self.enable.value = True

   def disable(self) -> None:
      self.enable.value = False

   def update(self, new_data) -> None:
      if new_data != shift_data:
         shift_data = new_data
         self.flag = 1
         for k in range(self.outputs):
            i = self.shift_data >> i & 1
            if i == 1:
               self.data.value = True
            else:
               self.data.value = False
            time.sleep(200e-9)
            self.shift.value = True
            time.sleep(200e-9)
            self.shift.value = False
         self.store.value = True
         time.sleep(200e-9)
         self.store.value = False
            

