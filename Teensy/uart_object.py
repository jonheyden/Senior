

class uart_container:
   def __init__(self, uart_) -> None:
      
      self.uartob = uart_
      self.pidarr = [
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0]          
      ]
      self.inputarr = [
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0], 
         [0,0,0,0,0],
         [0,0,0,0,0]
      ]
      self.outputarr = [
         [0],
         [0],
         [0],
         [0],
         [0],
         [0], 
         [0],
         [0]
      ]
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
      self.ltcarr = [
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]
      ]
      self.__mode = 0

   def check_buffer(self):
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
         elif x == ['ltc']:
            self.uartob.write(b'recieved')
            for i in range(4):
               y = self.get_decode()
               self.ltcarr[i] = list(map(int,y))
               self.uartob.write(b'recieved')

   
   def get_decode(self):
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