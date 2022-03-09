

class output_container:
   def __init__(self,output, mode) -> None:
      """__init__ Initializes output container object.

      :param output: The pin to output to
      :type output: PWMIO.PWMOUT
      :param mode: Value from 0-3
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
      
   def update_mode(self, mode) -> None:
      """update_mode Updates mode of the controller

      :param mode: Value from 0-3
      :type mode: int
      """      
      if 0 <= mode <= 3:
         self.__mode = mode
      else:
         self.__mode = 0

   def value(self, input):
      """value Updates values of the output pin

      :param input: Value from 0-100
      :type input: float
      """      
      retvalue = 0
      if self.__mode == 0: #Current 4-20mA
         retvalue = (self.__absolute_high-self.__c_low) * (input/100) + 13107
      if self.__mode == 1: #Voltage 0-5V
         retvalue = (self.__absolute_high-self.__v_high) * (input/100)

      if self.__mode == 2: #Voltage 0-10V
         retvalue = (self.__absolute_high) * (input/100)
         
      if self.__mode == 3: #0 or 24VDC      
         if input == 100:
            retvalue = self.__absolute_high - 1
         else:
            retvalue = 0
      self.__output.value = int(retvalue)

