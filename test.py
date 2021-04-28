import Adafruit_DHT
import time

SENSOR_LOCATION_NAME = "Office"

while True:
    humidity, temp_c = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)

    print("{} Temperature(C) {}  Humidity: {}".format(SENSOR_LOCATION_NAME, temp_c,  humidity))
    time.sleep(10)
