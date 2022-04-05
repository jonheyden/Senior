
class input_container:
   def __init__(self, input, eng_high, eng_low, mode) -> None:
      """__init__ Initializes the input container object.

      :param input: The input pin
      :type input: analogio.AnalogIn
      :param eng_high: Engineering unit high value
      :type eng_high: float
      :param eng_low: Engineering unit low value
      :type eng_low: float
      :param mode: The mode of the input (0-3)
      :type mode: int
      """      
      self.__input = input

      self.__eng_high = eng_high
      self.__eng_low = eng_low
      self.__absolute_high = 65535
      self.__absolute_low = 0
      if 0 <= mode <= 3:
         self.__mode = mode
      else:
         self.__mode = 0
      self.__c_span = self.__absolute_high - 13107
      self.__v_span = self.__absolute_high//2

   def update(self, eng_high, eng_low, mode) -> None:
      """update Updates the input container object.

      :param input: The input pin
      :type input: analogio.AnalogIn
      :param eng_high: Engineering unit high value
      :type eng_high: float
      :param eng_low: Engineering unit low value
      :type eng_low: float
      :param mode: The mode of the input (0-3)
      :type mode: int
      """  
      self.__eng_high = eng_high
      self.__eng_low = eng_low
      if 0 <= mode <= 3:
         self.__mode = mode
      else:
         self.__mode = 0

   def get_mode(self) -> int:
      """get_mode Returns the mode of the input

      :return: The mode of the input
      :rtype: int
      """
      return self.__mode
      
   def value(self) -> float:
      """value Returns the input value

      :return: The input value
      :rtype: float
      """
      raw = self.__input.value
      ret_value = 0
      if self.__mode == 0: #Current 4-20mA
         if raw < 13107:
            return self.__eng_low
         elif raw >= self.__absolute_high:
            return self.__eng_high
         ret_value = ((raw - 13107)/self.__c_span) * (self.__eng_high - self.__eng_low) + self.__eng_low

      if self.__mode == 1: #Voltage 0-5V
         if raw > 32768:
            return self.__eng_high
         ret_value = (raw)/self.__v_span * (self.__eng_high - self.__eng_low) + self.__eng_low

      if self.__mode == 2: #Voltage 0-10V
         ret_value = raw/self.__absolute_high * (self.__eng_high - self.__eng_low) + self.__eng_low
         
      if self.__mode == 3: #0 or 24VDC
         if raw > 55000:
            return self.__eng_high
         else:
            return self.__eng_low

      return ret_value