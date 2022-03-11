

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

