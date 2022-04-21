class uart_container:
   def __init__(self, uart_) -> None:
      """__init__ Initializes the uart container

      :param uart_: Uart object
      :type uart_: busio.UART
      """      
      
      self.uartob = uart_
      #PID [kp, ki, kd, min_output, max_output, min_input, max_input, sample_time, setpoint, mode, enable]
      self.pidarr = [
         [0,0,0,0,0,0,0,0,0,0,0], 
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0]          
      ]
      #input [mode, eng high, eng low]
      self.inputarr = [
         [0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0], 
         [0,0,0],
         [0,0,0]
      ]
      #output [mode,output_value,enable]
      self.outputarr = [
         [0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0], 
         [0,0,0],
         [0,0,0]
      ]
      #Relay [on/off]
      self.relayarr = [
         [0],
         [0],
         [0],
         [0],
         [0],
         [0], 
         [0],
         [0]
      ]
      self.digitalarr = [
         [0],
         [0],
         [0],
         [0],
         [0],
         [0], 
         [0],
         [0]
      ]      
      #LTC [Sensor Type, Sensor Type, Sensor Type, Sensor Type]
      self.ltcarr = [
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]
      ]
      self.__mode = 0

   def check_buffer(self):
      """check_buffer Used to check the buffer for data and update accordingly.
      """      
      if self.uartob.in_waiting > 0:
         x = self.uartob.readline()
         x = x.decode('utf-8').strip().split(',')
         if x == ['input']:
            self.uartob.write(b'recieved')
            for i in range(8):
               y = self.get_decode()
               self.inputarr[i] = list(map(int,y))
               self.uartob.write(b'recieved')
         elif x == ['output']:
            self.uartob.write(b'recieved')
            for i in range(8):
               y = self.get_decode()
               self.outputarr[i] = list(map(int,y))
               self.uartob.write(b'recieved')
         elif x == ['pid']:
            self.uartob.write(b'recieved')
            for i in range(8):
               y = self.get_decode()
               self.pidarr[i] = list(map(int,y))
               self.uartob.write(b'recieved')
         elif x == ['relay']:
            self.uartob.write(b'recieved')
            for i in range(8):
               y = self.get_decode()
               self.relayarr[i] = list(map(int,y))
               self.uartob.write(b'recieved')
         elif x == ['digital']:
            self.uartob.write(b'recieved')
            for i in range(8):
               y = self.get_decode()
               self.digitalarr[i] = list(map(int,y))
               self.uartob.write(b'recieved')         
         elif x == ['ltc']:
            self.uartob.write(b'recieved')
            for i in range(4):
               y = self.get_decode()
               self.ltcarr[i] = list(map(int,y))
               self.uartob.write(b'recieved')

   
   def get_decode(self):
      """get_decode Helper function to decode the data from the buffer.

      :return: Decoded data
      :rtype: str
      """      
      data = self.uartob.readline()
      data = data.decode('utf-8').strip()
      data = data.split(',')
      return data


'''
   def recieve_data(self):
      count = 0
      if self.__mode == 0:
         while(count < 9):
         self.__mode = 1
      elif self.__mode == 1:
         self.__mode = 2
      elif self.__mode == 2:
         self.__mode = 3
      elif self.__mode == 3:
         self.__mode = 4
      elif self.__mode == 4:
         self.__mode = 0

'''