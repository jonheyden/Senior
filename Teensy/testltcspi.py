import config
import spi_device
import time

chan20 = (0x1c << 27) | (0x1 << 26) | (0x1 << 25) | (0x0 << 24) | (0x1 << 22) | (0x100c49 << 0)
st_add = (0x0200) + 4 * (20-1)

st_addh = (st_add >> 8) & 0xff
st_addl = st_add & 0xff

d1 = (chan20 >> 24) & 0xff
d2 = (chan20 >> 16) & 0xff
d3 = (chan20 >> 8) & 0xff
d4 = (chan20 >> 0) & 0xff


transdata = [d4,d3,d2,d1,st_addl,st_addh,2]
transdata = bytearray(transdata)

conv_controlbyte = 0x80
lbit = conv_controlbyte & 20

convdata = [lbit,0,0,2]
convdata = bytearray(convdata)

ramad1 = 0x05C 

ramh = (ramad1 >> 8) & 0xff
raml = ramad1 & 0xff

readdata = [0,0,0,0,raml,ramh,3]
rdata = bytearray(7)
rdata[0] = 3
rdata[1] = ramh
rdata[2] = 92
rdata[3] = 0
rdata[4] = 0
rdata[5] = 0
rdata[6] = 0

read_data = bytearray(readdata)

device = spi_device.SPIDevice(config.ltcspi, config.ltc_cs)

return_data = bytearray(7)

with device as bus_device:
   bus_device.write(transdata)

time.sleep(1)

with device as bus_device:
   bus_device.write(convdata)

time.sleep(1)

while (1):
   with device as bus_device:
      bus_device.write(convdata)
   time.sleep(1)
   if (config.ltc_interrupt.value == True):
      with device as bus_device:
         bus_device.write_readinto(read_data, return_data)
         print(return_data.decode())
   time.sleep(1)


