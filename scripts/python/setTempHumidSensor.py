#!/usr/bin/python

import sys
import getopt
import homeassistant.remote as remote
import Adafruit_DHT


def main(argv):
    sensor_name_temperature = "sensor.office_temperature"
    sensor_name_humidity = "sensor.office_humidity"

    apiurl = ""
    password = ""
    pinid = ""

    try:
        opts, args = getopt.getopt(
            argv, "hu:p:i:s:", ["apiurl=", "password=", "pinid="])
    except getopt.GetoptError:
        print("test.py -u <api url> -p <password> -i <pin id>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print("test.py -u <api url> -p <password> -i <pin id>")
            sys.exit()
        elif opt in ("-u", "--apiurl"):
            apiurl = arg
        elif opt in ("-p", "--password"):
            password = arg
        elif opt in ("-i", "--pinid"):
            pinid = arg

    humidity, temperature = getSensorData(pinid)

    setSensorState(apiurl, password, sensor_name_temperature, temperature)
    setSensorState(apiurl, password, sensor_name_humidity, humidity)


def getSensorData(pinid):
    sensor = Adafruit_DHT.DHT22
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pinid)

    return humidity, temperature


def setSensorState(apiurl, password, sensorname, state):
    api = remote.API(apiurl, password)
    remote.set_state(api, sensorname, new_state=state)


if __name__ == "__main__":
    main(sys.argv[1:])
