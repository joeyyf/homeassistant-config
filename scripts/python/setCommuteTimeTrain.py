#!/usr/bin/python

import sys
import getopt
import homeassistant.remote as remote
import schiene


def main(argv):
    sensor_name_route_time = ""
    sensor_name_route_delay = ""
    from_station = ""
    to_station = ""
    region = ""
    apiurl = ""
    password = ""

    try:
        opts, args = getopt.getopt(
            argv, "hu:p:f:t:s:d:", ["apiurl=", "password="])
    except getopt.GetoptError:
        print("test.py -u <api url> -p <password> -f <from_station> -t <to_station> -s <sensor_name_time> -d <sensor_name_delay>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print("test.py -u <api url> -p <password> -f <from_station> -t <to_station> -s <sensor_name_time> -d <sensor_name_delay>")
            sys.exit()
        elif opt in ("-u", "--apiurl"):
            apiurl = arg
        elif opt in ("-p", "--password"):
            password = arg
        elif opt in ("-f"):
            from_station = arg
        elif opt in ("-t"):
            to_station = arg
        elif opt in ("-s"):
            sensor_name_route_time = "sensor.{0}".format(arg)
        elif opt in ("-d"):
            sensor_name_route_delay = "sensor.{0}".format(arg)

    routeData = getRouteData(from_station, to_station)
    nextRoute = routeData[0]

    if 'details' in nextRoute:
        nextRoute.pop('details')

        delay = nextRoute.get('delay', {'delay_departure': 0, 'delay_arrival': 0})
        delay_arrival = delay['delay_arrival']
        delay_departure = delay['delay_departure']
        departure = nextRoute.get('departure')

        setSensorState(apiurl, password, sensor_name_route_time, str(departure))
        #setSensorState(apiurl, password, sensor_name_route_distance, str(route_distance))


def getRouteData(from_station, to_station):
    s = schiene.Schiene()
    route = s.connections(from_station, to_station)

    return route


def setSensorState(apiurl, password, sensorname, state):
    api = remote.API(apiurl, password)
    print("setting {0} to {1}".format(sensorname, state))
    remote.set_state(api, sensorname, new_state=state)


if __name__ == "__main__":
    main(sys.argv[1:])
