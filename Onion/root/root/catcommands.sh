cat temp.txt | mosquitto_pub -t potentiometerPosition -l
#tail -f temp.txt | mosquitto_pub -t potentiometerPosition -l &
