import time
import supervisor

class PID_Object:
   
   def __init__(self, kp, ki, kd, min_output, max_output, min_input, max_input, sample_time):
      """__init__ Initializes the PID Object and starts disabled, in manual mode.

      :param kp: Proportional Gain
      :type kp: float
      :param ki: Integral Gain
      :type ki: float
      :param kd: Derivative Gain
      :type kd: float
      :param min_output: Boundary for the minimum value of the output, minimum is 0.0
      :type min_output: float
      :param max_output: Boundary for the maximum value of the output, maximum is 1.0
      :type max_output: float
      :param min_input: Boundary for the input, unbounded
      :type min_input: float
      :param max_input: Boundary for the max input, unbounded
      :type max_input: float
      :param sample_time: The time in milliseconds that the PID output should be updated
      :type sample_time: float
      """      

      if 0 <= min_output <= max_output: 
         self.__min_output = min_output
      else:
         self.__min_output = 0

      if min_output <= max_output <= 100:
         self.__max_output = max_output
      else:
         self.__max_output = 100

      self.__min_input = min_input
      self.__max_input = max_input

      self.__kp = kp
      self.__ki = ki
      self.__kd = kd

      if sample_time > 0:
         self.__sample_time = sample_time
      else:
         self.__sample_time = 500
      
      self.__enable = False
      self.__auto_mode = False
      self.__output = min_output
      self.clear()

   def clear(self):
      """clear Sets all values to 0 upon initialization
      """      
      self.__pterm = 0.0
      self.__iterm = 0.0
      self.__dterm = 0.0

      self.__error = 0.0
      self.__current_time = 0

      self.__last_input = 0
      self.__last_error = 0
      self.__delta_error = 0
      self.__last_time = 0
      self.__dt = 0
      self.__enable = False

      self.__setpoint = 0

   def enable(self):
      """enable Enables the PID Object
      """      
      self.__enable = True

   def disable(self):
      """disable Dusable the PID Object
      """      
      self.__enable = False
   
   def __check_time(self):
      """__check_time Checks if the PID should be updated and updates local variable time

      :return: True if the PID should be updated, False if not
      :rtype: bool
      """      
      self.__current_time = supervisor.ticks_ms()
      
      if self.__last_time == 0:
         self.__last_time = supervisor.ticks_ms()
         return False

      self.__dt = self.__current_time - self.__last_time

      if self.__dt > self.__sample_time:
         self.__last_time = self.__current_time
         return True
      else:
         return False

   def __error_update(self, input):
      """__error_update Updates the error and delta error

      :param input: Input value to be checked against the setpoint
      :type input: float
      """      
      self.__error = self.__setpoint - input
      self.__delta_error = self.__error - self.__last_error
      self.__last_error = self.__error

   def update(self, input):
      """update Updates the PID Output

      :param input: The input value to be checked against the setpoint
      :type input: float
      :return: The output value from 0-100
      :rtype: float
      """

      if input < self.__min_input:
         input = self.__min_input
      if input > self.__max_input:
         input = self.__max_input

      if self.__check_time() and self.__enable:         
         if self.__auto_mode:
            self.__error_update(input)
            self.__pterm = self.__kp * self.__error
            self.__iterm += self.__error*self.__dt

            if self.__iterm < -20:
               self.__iterm = -20
            if self.__iterm > 20:
               self.__iterm = 20

            self.__dterm = self.__delta_error / self.__dt
            self.__output = self.__pterm + (self.__ki * self.__iterm)+ (self.__kd * self.__dterm)

            self.__output = max(self.__min_output, self.__output)
            self.__output = min(self.__max_output, self.__output)

            self.__last_input = input
         return self.__output
      return 0.0


   def set_setpoint(self, setpoint):
      """set_setpoint Setter for the setpoint

      :param setpoint: Setpoint value
      :type setpoint: float
      """      
      self.__setpoint = setpoint

   def set_sampletime(self, sampletime):
      """set_sampletime Setter for the Sample Time

      :param sampletime: Time in milliseconds that the PID output should be updated
      :type sampletime: float
      """      
      if sampletime > 0:
         self.__sample_time = sampletime

   def set_auto(self):
      """set_auto Setter for the auto mode
      """      
      self.__auto_mode = True
   
   def set_manual(self):
      """set_manual Setter for the manual mode
      """      
      self.__auto_mode = False

   def set_kp(self, kp):
      """set_kp Setter for the proportional gain

      :param kp: Proportional Gain
      :type kp: float
      """      
      self.__kp = kp
   
   def set_ki(self, ki):
      """set_ki Setter for the integral gain

      :param ki: Integral Gain
      :type ki: float
      """      
      self.__ki = ki

   def set_kd(self, kd):
      """set_kd Setter for the derivative gain

      :param kd: Derivative Gain
      :type kd: float
      """            
      self.__kd = kd

   def set_output(self, output):
      """set_output Setter for the output if in manual mode

      :param output: 
      :type output: _type_
      """      
      if not self.__auto_mode:
         self.__output = output

   def get_output(self):
      """get_output Returns the value of the output

      :return: Value of the output being commanded from the PID
      :rtype: float
      """      
      return self.__output


