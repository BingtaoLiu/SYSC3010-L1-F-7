from sense_hat import SenseHat  
import time  
import sys  
 
  
# --------- User Settings ---------
BUCKET_NAME = "Fridge weather"
BUCKET_KEY = "sensehat"
SENSOR_LOCATION_NAME = "Fridge"
MINUTES_BETWEEN_SENSEHAT_READS = 0.1
USER_ID = "3"
SENSOR_ID = "4"
# ---------------------------------

  
sense = SenseHat()  
  
while True:
  # Read the sensors
  temp_c = sense.get_temperature()
  humidity = sense.get_humidity() 
  pressure_mb = sense.get_pressure() 

  # Format the data
  temp_f = temp_c * 9.0 / 5.0 + 32.0
  temp_f = float("{0:.2f}".format(temp_f))
  humidity = float("{0:.2f}".format(humidity))
  pressure_in = 0.03937008*(pressure_mb)
  pressure_in = float("{0:.2f}".format(pressure_in))

  # Print and stream 
  print USER_ID
  print SENSOR_ID
  print SENSOR_LOCATION_NAME + " Temperature(F): " + str(temp_f)
  print SENSOR_LOCATION_NAME + " Humidity(%): " + str(humidity)
  


  time.sleep(60*MINUTES_BETWEEN_SENSEHAT_READS)