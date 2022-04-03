
class output_container:
   def __init__(self,output, mode) -> None:
      """__init__ Initializes output container object.

      :param output: The pin to output to
      :type output: PWMIO.PWMOUT
      :param mode: Value from 0-2
      :type mode: int
      """      
      self.__output = output
      if 0 <= mode <= 3:
         self.__mode = mode
      else:
         self.__mode = 0    
      self.__absolute_high = 65535
      self.__absolute_low = 0
      self.__c_low = 13107
      self.__v_high = 32768
      self.__value = 0
      self.__enablebit = 0
      self.disable()
      
   def disable(self) -> None:
      """disable Disables the output pin"""
      self.__output.duty_cycle = 0
      self.__enablebit = 0

   def enable(self) -> None:
      """enable Enables the output pin"""
      self.__enablebit = 1
      self.value(self.__value)
   
   def update_mode(self, mode) -> None:
      """update_mode Updates mode of the controller

      :param mode: Value from 0-2
      :type mode: int
      """
      if mode == self.__mode:
         return

      if 0 <= mode <= 2:
         self.__mode = mode
      else:
         self.__mode = 0

      if self.__enablebit == 1:
         self.value(self.__value)

   def value(self, input):
      """value Updates values of the output pin

      :param input: Value from 0-100
      :type input: float
      """      
      retvalue = 0
      if self.__enablebit == 1:
         if self.__mode == 0: #Current 4-20mA
            retvalue = (self.__absolute_high-self.__c_low) * (input/100) + 13107
         if self.__mode == 1: #Voltage 0-5V
            retvalue = (self.__absolute_high-self.__v_high) * (input/100)
         if self.__mode == 2: #Voltage 0-10V
            retvalue = (self.__absolute_high) * (input/100)
         self.__output.duty_cycle = int(retvalue)

      self.__value = input
      

