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
        coll.insert(entry)
    except Exception as e:
        print(e)


def printValues():
    result = list(coll.find())
    return result


def currentValues():
    try:
        humidity, temp_c = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
        t = time.time()
        entry = {
            "time": t,
            "humidity": humidity,
            "temperature": temp_c,
            "location": "office"
        }
        return entry
    except Exception as e:
        return str(e)
