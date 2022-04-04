
class setting_container:
   def __init__(self, i_container, o_container, i_shiftreg, o_shiftreg, r_shiftreg, d_shiftreg, p_container, ltcob) -> None:
      """__init__ Initializes the setting_container object.

      :param i_container: Input container array
      :type i_container: list
      :param o_container: Output container array
      :type o_container: list
      :param i_shiftreg: input Shiftregister Object
      :type i_shiftreg: shift_object.shiftregister
      :param o_shiftreg: Output Shift Register Object
      :type o_shiftreg: shift_object.shiftregister
      :param r_shiftreg: Relay Shift Register Object
      :type r_shiftreg: shift_object.shiftregister
      :param d_shiftreg: Digital Shift Register Object
      :type d_shiftreg: shift_object.shiftregister
      :param p_container: PID Container array
      :type p_container: list
      :param ltcob: LTC2984 Object
      :type ltcob: ltc2984.ltc2984
      """      
      
      self.__input_array = i_container
      self.__output_array = o_container
      self.__input_shiftreg = i_shiftreg
      self.__output_shiftreg = o_shiftreg
      self.__relay_shiftreg = r_shiftreg
      self.__digital_shiftreg = d_shiftreg
      self.__pid_array = p_container

      self.__relayValue = 0b00000000
      self.__digitalValue = 0b00000000
      self.__inputValue = 0b00000000
      self.__outputValue = 0x0000
      self.__ltcob = ltcob

      #PID [kp, ki, kd, min_output, max_output, min_input, max_input, sample_time, setpoint, mode, enable]
      self.__pidarr = [
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
      self.__inputarr = [
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
      self.__outputarr = [
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
      self.__relayarr = [
         [0],
         [0],
         [0],
         [0],
         [0],
         [0], 
         [0],
         [0]
      ]
      self.__digitalarr = [
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
      self.__ltcarr = [
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]
      ]

   def check_update(self, uartob):
      """check_update Checks the uart object for new data and updates the settings container accordingly

      :param uartob: Uart Container Object
      :type uartob: uart_object.uart_container
      """      
      if self.__pidarr != uartob.pidarr:
         for i in range(len(self.__pidarr)):
            self.__pidarr[i] = uartob.pidarr[i]

         for i in range(len(self.__pidarr)):
            for j in range(len(self.__pidarr[i])):
               if j == 0:
                  self.__pid_array[i].set_kp(self.__pidarr[i][j])
               if j == 1:
                  self.__pid_array[i].set_ki(self.__pidarr[i][j])
               if j == 2:
                  self.__pid_array[i].set_kd(self.__pidarr[i][j])
               if j == 3:
                  self.__pid_array[i].set_min_output(self.__pidarr[i][j])
               if j == 4:
                  self.__pid_array[i].set_max_output(self.__pidarr[i][j])
               if j == 5:
                  self.__pid_array[i].set_min_input(self.__pidarr[i][j])
               if j == 6:
                  self.__pid_array[i].set_max_input(self.__pidarr[i][j])
               if j == 7:
                  self.__pid_array[i].set_sampletime(self.__pidarr[i][j])
               if j == 8:
                  self.__pid_array[i].set_setpoint(self.__pidarr[i][j])
               if j == 9:
                  if self.__pidarr[i][j] == 0:
                     self.__pid_array[i].set_manual()
                  else:
                     self.__pid_array[i].set_auto()
               if j == 10:
                  if self.__pidarr[i][j] == 0:
                     self.__pid_array[i].disable()
                  else:
                     self.__pid_array[i].enable()

      if self.__inputarr != uartob.inputarr:
         for i in range(len(self.__inputarr)):
            self.__inputarr[i] = uartob.inputarr[i]

         for i in range(len(self.__inputarr)):
            self.__input_array[i].update(self.__inputarr[i][0], self.__inputarr[i][1], self.__inputarr[i][2])
            if self.__input_array[i].get_mode() == 0:
               self.__inputValue = self.__inputValue | (1 << i)
            else:
               self.__inputValue = self.__inputValue & (0xFF & (0 << i))

         self.__input_shiftreg.update(self.__inputValue)

      if self.__outputarr != uartob.outputarr:
         for i in range(len(self.__outputarr)):
            self.__outputarr[i] = uartob.outputarr[i]
            self.__outputValue = 0x0000
         for i in range(len(self.__outputarr)):
            for j in range(len(self.__outputarr[i])):
               if j == 0:
                  self.__output_array[i].update_mode(self.__outputarr[i][j])
                  if self.__outputarr[i][j] == 0:
                     self.__outputValue = self.__outputValue | (1 << (i*2))
                  else:
                     self.__outputValue = self.__outputValue | (3 << (i*2)) 
               if j == 1:
                  self.__output_array[i].value(self.__outputarr[i][j])
               if j == 2:
                     if self.__outputarr[i][j] == 0:
                        self.__output_array[i].disable()
                     else:
                        self.__output_array[i].enable()
         
         self.__output_shiftreg.update(self.__outputValue)
         


      if self.__relayarr != uartob.relayarr:
         for i in range(len(self.__relayarr)):
            self.__relayarr[i] = uartob.relayarr[i]
         for i in range(len(self.__relayarr)):
            self.__relayValue = self.__relayValue | (self.__relayarr[i][0] << i)
            
         self.__relay_shiftreg.update(self.__relayValue)
            
      if self.__digitalarr != uartob.digitalarr:
         for i in range(len(self.__digitalarr)):
            self.__digitalarr[i] = uartob.digitalarr[i]
         for i in range(len(self.__digitalarr)):
            self.__digitalValue = self.__digitalValue | (self.__digitalarr[i][0] << i)
            
         self.__digital_shiftreg.update(self.__digitalValue)

      if self.__ltcarr != uartob.ltcarr:
         for i in range(len(self.__ltcarr)):
            self.__ltcarr[i] = uartob.ltcarr[i]

         for i in range(len(self.__ltcarr)):
            for j in range(len(self.__ltcarr[i])):
               if j == 0:
                  if self.__ltcarr[i][0] <= 8 and self.__ltcarr[i][0] >= 1:
                     data = self.__ltcob.generate_thermocouple_assignment(self.__ltcarr[i][j])
                     channel = (i*4) + (j + 3)
                     self.__ltcob.chan_assignment(channel, data)
               if j == 1:
                  if self.__ltcarr[i][0] <= 8 and self.__ltcarr[i][0] >= 1:
                     data = self.__ltcob.generate_thermocouple_assignment(self.__ltcarr[i][j])
                     channel = (i*4) + (j + 3)
                     self.__ltcob.chan_assignment(channel, data)                     
               if j == 2:
                  if self.__ltcarr[i][0] <= 8 and self.__ltcarr[i][0] >= 1:
                     data = self.__ltcob.generate_thermocouple_assignment(self.__ltcarr[i][j])
                     channel = (i*4) + (j + 3)
                     self.__ltcob.chan_assignment(channel, data)                     
               if j == 3:
                  if self.__ltcarr[i][0] <= 8 and self.__ltcarr[i][0] >= 1:
                     data = self.__ltcob.generate_thermocouple_assignment(self.__ltcarr[i][j])
                     channel = (i*4) + (j + 3)
                     self.__ltcob.chan_assignment(channel, data)
                  
                  if self.__ltcarr[i][0] > 8:
                     data = self.__ltcob.generate_RTD_assignment(self.__ltcarr[i][0], self.__ltcarr[i][1])
                     if i == 0:
                        self.__ltcob.chan_assignment(4, data)
                     if i == 1:
                        self.__ltcob.chan_assignment(8, data)
                     if i == 2:
                        self.__ltcob.chan_assignment(12, data)
                     if i == 3:
                        self.__ltcob.chan_assignment(16, data)