





#Address
command_status_reg = 0x000
temp_results_reg = 0x010
channel_assignment_data = 0x200

read_command = 0x3
write_command = 0x2

#channels
ch1 = 0x200
ch2 = 0x204
ch3 = 0x208
ch4 = 0x20c
ch5 = 0x210
ch6 = 0x214
ch7 = 0x218
ch8 = 0x21c
ch9 = 0x220
ch10 = 0x224
ch11 = 0x228
ch12 = 0x22c
ch13 = 0x230
ch14 = 0x234
ch15 = 0x238
ch16 = 0x23c
ch17 = 0x240
ch18 = 0x244
ch19 = 0x248
ch20 = 0x24c

sensorlsb = 27
rtd_pt10 = 0xa << sensorlsb
rtd_pt50 = 0xb << sensorlsb
rtd_pt100 = 0xc << sensorlsb
rtd_pt200 = 0xd << sensorlsb
rtd_pt500 = 0xe << sensorlsb
rtd_pt1000 = 0xf << sensorlsb
#sense resistor
sense_resistor = 0x1d << sensorlsb
sense_type_none = 0x0 << sensorlsb

type_j = 0x1 << sensorlsb
type_k = 0x2 << sensorlsb
type_e = 0x3 << sensorlsb
type_n = 0x4 << sensorlsb
type_r = 0x5 << sensorlsb
type_s = 0x6 << sensorlsb
type_t = 0x7 << sensorlsb
type_b = 0x8 << sensorlsb

type_off_chip_diode = 0x1c << sensorlsb

rtd_sense_channel_lsb = 22
rsense_channel_none = 0x0 << rtd_sense_channel_lsb
rsense_channel_1 = 0x1 << rtd_sense_channel_lsb
rsense_channel_2 = 0x2 << rtd_sense_channel_lsb
rsense_channel_3 = 0x3 << rtd_sense_channel_lsb
rsense_channel_4 = 0x4 << rtd_sense_channel_lsb
rsense_channel_5 = 0x5 << rtd_sense_channel_lsb
rsense_channel_6 = 0x6 << rtd_sense_channel_lsb
rsense_channel_7 = 0x7 << rtd_sense_channel_lsb
rsense_channel_8 = 0x8 << rtd_sense_channel_lsb
rsense_channel_9 = 0x9 << rtd_sense_channel_lsb
rsense_channel_10 = 0xa << rtd_sense_channel_lsb
rsense_channel_11 = 0xb << rtd_sense_channel_lsb
rsense_channel_12 = 0xc << rtd_sense_channel_lsb
rsense_channel_13 = 0xd << rtd_sense_channel_lsb
rsense_channel_14 = 0xe << rtd_sense_channel_lsb
rsense_channel_15 = 0xf << rtd_sense_channel_lsb
rsense_channel_16 = 0x10 << rtd_sense_channel_lsb
rsense_channel_17 = 0x11 << rtd_sense_channel_lsb
rsense_channel_18 = 0x12 << rtd_sense_channel_lsb
rsense_channel_19 = 0x13 << rtd_sense_channel_lsb
rsense_channel_20 = 0x14 << rtd_sense_channel_lsb

rtd_num_wires_lsb = 20
rtd_num_wires_2 = 0x0 << rtd_num_wires_lsb
rtd_num_wires_3 = 0x1 << rtd_num_wires_lsb
rtd_num_wires_4 = 0x2 << rtd_num_wires_lsb

rtd_excitation_lsb = 18
rtd_excitation_off = 0x0 << rtd_excitation_lsb
rtd_excitation_sharing = 0x1 << rtd_excitation_lsb
rtd_excitation_sharing_rotation = 0x2 << rtd_excitation_lsb

sense_resistor_value_lsb = 0

thermocouple_cold_junction_lsb = 22
tc_cold_junc_ch_none = 0x0 << thermocouple_cold_junction_lsb
tc_cold_junc_ch_1 = 0x1 << thermocouple_cold_junction_lsb
tc_cold_junc_ch_2 = 0x2 << thermocouple_cold_junction_lsb
tc_cold_junc_ch_3 = 0x3 << thermocouple_cold_junction_lsb
tc_cold_junc_ch_4 = 0x4 << thermocouple_cold_junction_lsb
tc_cold_junc_ch_5 = 0x5 << thermocouple_cold_junction_lsb
tc_cold_junc_ch_6 = 0x6 << thermocouple_cold_junction_lsb
tc_cold_junc_ch_7 = 0x7 << thermocouple_cold_junction_lsb
tc_cold_junc_ch_8 = 0x8 << thermocouple_cold_junction_lsb
tc_cold_junc_ch_9 = 0x9 << thermocouple_cold_junction_lsb
tc_cold_junc_ch_10 = 0xa << thermocouple_cold_junction_lsb
tc_cold_junc_ch_11 = 0xb << thermocouple_cold_junction_lsb
tc_cold_junc_ch_12 = 0xc << thermocouple_cold_junction_lsb
tc_cold_junc_ch_13 = 0xd << thermocouple_cold_junction_lsb
tc_cold_junc_ch_14 = 0xe << thermocouple_cold_junction_lsb
tc_cold_junc_ch_15 = 0xf << thermocouple_cold_junction_lsb
tc_cold_junc_ch_16 = 0x10 << thermocouple_cold_junction_lsb
tc_cold_junc_ch_17 = 0x11 << thermocouple_cold_junction_lsb
tc_cold_junc_ch_18 = 0x12 << thermocouple_cold_junction_lsb
tc_cold_junc_ch_19 = 0x13 << thermocouple_cold_junction_lsb
tc_cold_junc_ch_20 = 0x14 << thermocouple_cold_junction_lsb

diode_differential_lsb = 26
diode_differential = 0x0 << diode_differential_lsb
diode_single_ended = 0x1 << diode_differential_lsb

diode_num_reading_lsb = 25
diode_num_reading_2 = 0x0 << diode_num_reading_lsb
diode_num_reading_3 = 0x1 << diode_num_reading_lsb

diode_averaging_lsb = 24
diode_averaging_off = 0x0 << diode_averaging_lsb
diode_averaging_on = 0x1 << diode_averaging_lsb

diode_current_lsb = 22
diode_current_10ua_40ua_80ua = 0x0 << diode_current_lsb
diode_current_20ua_80ua_160ua = 0x1 << diode_current_lsb
diode_current_40ua_160ua_320ua = 0x2 << diode_current_lsb
diode_current_80ua_320ua_640ua = 0x3 << diode_current_lsb

ideality_factor_lsb = 0

#Global Configuration Constants
rejection_50_60hz = 0x0
rejection_60hz = 0x1
rejection_50hz = 0x2
temp_unit_celsius = 0x0
temp_unit_fahrenheit = 0x4

#status byte constants
sensor_hard_failure = 0x80
adc_hard_failure = 0x40
cj_hard_failure = 0x20
cj_soft_failure = 0x10
sensor_above = 0x8
sensor_below = 0x4
adc_range_error = 0x2
valid_con = 0x1

#Addresses
command_status_register = 0x0000
ch_address_base = 0x0200
vout_ch_base = 0x0060
read_ch_base = 0x0010
conversion_result_memory_base = 0x0010
