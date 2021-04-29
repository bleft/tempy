import Adafruit_DHT
import time
import pymongo

cl = pymongo.MongoClient()
coll = cl["climate"]["sensor"]

if __name__ == '__main__':
    try:
        humidity, temp_c = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
        t = time.time()
        entry = {
            "time": t,
            "humidity": humidity,
            "temperature": temp_c,
            "location": "office"
        }
        coll.insert_one(entry)
    except Exception as e:
        print(e)

def printValues():
    humidity, temp_c = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
    return "Temp: {} \n Himidity {}".format(temp_c, humidity)
