#!/usr/bin/python

import sys
import getopt
import homeassistant.remote as remote
import WazeRouteCalculator


def main(argv):
    sensor_name_route_time = "sensor.commute_time_her"
    sensor_name_route_distance = "commute_distance_her"

    from_address = '86899 Landsberg am Lech, Deutschland'
    to_address = '82205 Gilching, Deutschland'
    region = 'EU'

    apiurl = ""
    password = ""

    try:
        opts, args = getopt.getopt(
            argv, "hu:p:i:s:", ["apiurl=", "password="])
    except getopt.GetoptError:
        print("test.py -u <api url> -p <password>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print("test.py -u <api url> -p <password>")
            sys.exit()
        elif opt in ("-u", "--apiurl"):
            apiurl = arg
        elif opt in ("-p", "--password"):
            password = arg

    route_time, route_distance = getRouteData(from_address, to_address, region)

    setSensorState(apiurl, password, sensor_name_route_time, route_time)
    setSensorState(apiurl, password, sensor_name_route_distance, route_distance)


def getRouteData(from_address, to_address, region):
    route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, region)
    route_time, route_distance = route.calc_route_info()

    return route_time, route_distance


def setSensorState(apiurl, password, sensorname, state):
    api = remote.API(apiurl, password)
    remote.set_state(api, sensorname, new_state=state)


if __name__ == "__main__":
    main(sys.argv[1:])
