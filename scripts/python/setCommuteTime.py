#!/usr/bin/python

import sys
import getopt
import homeassistant.remote as remote
import WazeRouteCalculator


def main(argv):
    sensor_name_route_time = ""
    sensor_name_route_distance = ""
    from_address = ""
    to_address = ""
    region = ""
    apiurl = ""
    password = ""

    try:
        opts, args = getopt.getopt(
            argv, "hu:p:f:t:s:d:r:", ["apiurl=", "password="])
    except getopt.GetoptError:
        print("test.py -u <api url> -p <password> -f <from_address> -t <to_address> -s <sensor_name_time> -d <sensor_name_distance> -r <region>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print("test.py -u <api url> -p <password> -f <from_address> -t <to_address> -s <sensor_name_time> -d <sensor_name_distance> -r <region>")
            sys.exit()
        elif opt in ("-u", "--apiurl"):
            apiurl = arg
        elif opt in ("-p", "--password"):
            password = arg
        elif opt in ("-f"):
            from_address = arg
        elif opt in ("-t"):
            to_address = arg
        elif opt in ("-s"):
            sensor_name_route_time = "sensor.{0}".format(arg)
        elif opt in ("-d"):
            sensor_name_route_distance = "sensor.{0}".format(arg)
        elif opt in ("-r"):
            region = arg

    route_time, route_distance = getRouteData(from_address, to_address, region)

    setSensorState(apiurl, password, sensor_name_route_time, str(route_time))
    setSensorState(apiurl, password, sensor_name_route_distance, str(route_distance))


def getRouteData(from_address, to_address, region):
    route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, region)
    route_time, route_distance = route.calc_route_info()

    return route_time, route_distance


def setSensorState(apiurl, password, sensorname, state):
    api = remote.API(apiurl, password)
    print("setting {0} to {1}".format(sensorname, state))
    remote.set_state(api, sensorname, new_state=state)


if __name__ == "__main__":
    main(sys.argv[1:])
