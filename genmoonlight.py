#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""genmoonlight.py
"""

__author__ = "Francesco Anselmo"
__copyright__ = "Copyright 2023, Francesco Anselmo"
__credits__ = ["Francesco Anselmo"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Francesco Anselmo"
__email__ = "francesco.anselmo@gmail.com"
__status__ = "Dev"

import argparse
from datetime import datetime
from math import sin, cos, pi
import pylunar

radiance_moon_template = """
# Lunar altitude  {altitude} deg, azimuth {azimuth} deg
# lunar age {age} days, disc illum fraction {fraction}, angular disc size {size} deg\n
void light lunar
0
0
3 {radR} {radG} {radB}\n
lunar source moon
0
0
4 {vx} {vy} {vz} {size}\n
"""

def spherical2cartesian(rthetaphi):
    """ Convert spherical coordinates to cartesian coordinates
    """
    r       = rthetaphi[0]
    theta   = rthetaphi[1]* pi/180 # to radian
    phi     = rthetaphi[2]* pi/180
    x = r * sin( theta ) * cos( phi )
    y = r * sin( theta ) * sin( phi )
    z = r * cos( theta )
    return [x,y,z]

def deg_to_dms(deg):
    """ Convert decimal degrees to degrees, minutes, seconds
    """
    m, s = divmod(abs(deg)*3600, 60)
    d, m = divmod(m, 60)
    if deg < 0:
        d = -d
    d, m = int(d), int(m)
    return d, m, s

def show_title():
    """Show the program title
    """

    title = """
#                                                _ _       _     _
#    __ _  ___ _ __  _ __ ___   ___   ___  _ __ | (_) __ _| |__ | |_
#   / _` |/ _ \ '_ \| '_ ` _ \ / _ \ / _ \| '_ \| | |/ _` | '_ \| __|
#  | (_| |  __/ | | | | | | | | (_) | (_) | | | | | | (_| | | | | |_
#   \__, |\___|_| |_|_| |_| |_|\___/ \___/|_| |_|_|_|\__, |_| |_|\__|
#   |___/                                            |___/
"""
    print(title)

def main():
    """Main function
    """

    show_title()

    parser = argparse.ArgumentParser()
    # parser.add_argument("-v", "--verbose", action="store_true",
    #                     default=False, help="increase the verbosity level")
    parser.add_argument("-a", "--latitude", default="50.790707850000004", help="latitude")
    parser.add_argument("-o", "--longitude", default="-2.6816552948061627", help="longitude")
    parser.add_argument("-m", "--meridian", default="0", help="meridian")
    parser.add_argument("-d", "--date", default="2023-10-28", help="date - format: YYYY-MM-DD")
    parser.add_argument("-t", "--time", default="23:00", help="time - format: HH:MM")

    args = parser.parse_args()

    # if args.verbose:
    #     print("program arguments:")
    #     print(args)
    #     print()

    if args.latitude!="" and args.longitude!="" and args.meridian!="" and \
        args.date!="" and args.time!="":

        latitude_dms = deg_to_dms(float(args.latitude))
        longitude_dms = deg_to_dms(float(args.longitude))

        moon_info = pylunar.MoonInfo(latitude_dms, longitude_dms)

        datetime_str = '%s %s' % (args.date, args.time)
        print("# Moon data for %s" % datetime_str)

        datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')

        year = int(datetime.strftime(datetime_object,'%Y'))
        month = int(datetime.strftime(datetime_object,'%m'))
        day = int(datetime.strftime(datetime_object,'%d'))
        hour = int(datetime.strftime(datetime_object,'%H'))
        minute = int(datetime.strftime(datetime_object,'%M'))

        TARGET_MOMENT = (year, month, day, hour, minute, 0)

        moon_info.update(TARGET_MOMENT)
        print("# Location - latitude: %s | longitude: %s" % (args.latitude, args.longitude))
        print("# Target Moon's azimuth:", moon_info.azimuth())
        print("# Target Moon's altitude:", moon_info.altitude())
        print("# Target Moon's angular size:", moon_info.angular_size() )
        # print("# Target Moon's radius:", moon_info.moon.radius )
        print("# Target Moon's age (days):", moon_info.age())
        print("# Target Moon's fractional phase:", moon_info.fractional_phase())
        print("# Target Moon's phase name:", moon_info.phase_name())
        # print("# Target Moon's magnitude (measure of the brightness of a celestial object):",
        #       moon_info.magnitude())
        print("# Distance of target Moon's from Earth:", moon_info.earth_distance(), "km")
        # print("# Next four Moon phases:", moon_info.next_four_phases())

        moon_azimuth  = moon_info.azimuth()
        moon_altitude = moon_info.altitude()

        v = spherical2cartesian([1,90.0-moon_altitude,90.0-moon_azimuth])

        # the lunar colour is slightly brownish (https://habr.com/en/articles/479264/)
        lunar_colour = (1.05, 1.0, 0.85)

        # the lunar luminance is 1/449000 of full bright sun and scaled by the visible fraction
        lunar_luminance = 15.6 * pow(moon_info.fractional_phase(),2)

        print(radiance_moon_template.format(azimuth = moon_azimuth, 
                                        altitude = moon_altitude,
                                        age = moon_info.age(),
                                        fraction = moon_info.fractional_phase(),
                                        size = moon_info.angular_size(),
                                        radR = lunar_luminance * lunar_colour[0],
                                        radG = lunar_luminance * lunar_colour[1],
                                        radB = lunar_luminance * lunar_colour[2],
                                        vx = v[0],
                                        vy = v[1],
                                        vz = v[2]) )


if __name__ == "__main__":
    main()


"""
 
 
 // luminance is 1/449000 of full bright sun
  // and scaled by fraction visible
  lum = 15.6 * pow(discFrac,2);

  // moon is a source, like the sun
  fprintf(stdout,"void light lunar\n");
  fprintf(stdout,"0\n0\n3 %g %g %g\n",lum*lunC[0],lum*lunC[1],lum*lunC[2]);

  // complete the moon
  fprintf(stdout,"lunar source moon\n");
  fprintf(stdout,"0\n0\n4 %g %g %g %.3f\n",lunPos[0],lunPos[1],lunPos[2],discSize);"""

"""
# Lunar altitude  45.736 deg, azimuth 340.189 deg
# lunar phase  12.545, disc illum fraction   0.988, disc size   0.54 deg
void light lunar
0
0
3 15.9912 15.2298 12.9453
lunar source moon
0
0
4 0.236549 -0.656654 0.716136 0.543
"""
