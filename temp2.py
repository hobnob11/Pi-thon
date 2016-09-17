#!/usr/bin/python
#loading up modules
from w1thermsensor import W1ThermSensor
import os
import time
from influxdb import InfluxDBClient

while True:

        sensor1 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "041601403dff") #first temp sensor
        sensor1_val = sensor1.get_temperature()

        sensor2 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "0316054850ff") #second one
        sensor2_val = sensor2.get_temperature()

        print("posting data")


        sensor1_json_body =[
        {
		"sensor" : "temp_sensor_01",
		"points" : {
			"temp" : sensor1_val,
			"time" : time.time()
			}
        }]
        #sensor2_json_body =[
        #  {
        #    "name" : "sensor2_temp_c",
        #    "columns" : ["value", "sensor"],
        #    "points" : [
        #      [sensor2_val, "sensor02"]
        #    ]
        #  }
        #]

        client = InfluxDBClient('ts.willhobson.co.uk', 8086, 'pi', 'CakePass90', 'pi_temp')
        client.write_points(sensor1_json_body)
        #client.write_points(sensor2_json_body)
        print(sensor1_val)
        #print(sensor2_val)
        
	time.sleep(2)
