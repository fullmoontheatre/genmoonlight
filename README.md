# genmoonlight
A python script to generate a Radiance file description of the moon at a specific location, date and time.

"" Installation of dependencies

`python3 -m pip install -r requirements.txt`

"" Options

```
#                                                _ _       _     _
#    __ _  ___ _ __  _ __ ___   ___   ___  _ __ | (_) __ _| |__ | |_
#   / _` |/ _ \ '_ \| '_ ` _ \ / _ \ / _ \| '_ \| | |/ _` | '_ \| __|
#  | (_| |  __/ | | | | | | | | (_) | (_) | | | | | | (_| | | | | |_
#   \__, |\___|_| |_|_| |_| |_|\___/ \___/|_| |_|_|_|\__, |_| |_|\__|
#   |___/                                            |___/

usage: genmoonlight.py [-h] [-a LATITUDE] [-o LONGITUDE] [-m MERIDIAN]
                       [-d DATE] [-t TIME]

optional arguments:
  -h, --help            show this help message and exit
  -a LATITUDE, --latitude LATITUDE
                        latitude
  -o LONGITUDE, --longitude LONGITUDE
                        longitude
  -m MERIDIAN, --meridian MERIDIAN
                        meridian
  -d DATE, --date DATE  date - format: YYYY-MM-DD
  -t TIME, --time TIME  time - format: HH:MM
```

## Usage example

`$ ./genmoonlight.py -a 50.790707850000004 -o -2.6816552948061627 -m 0 -d 2023-10-28 -t 23:00`

```
#                                                _ _       _     _
#    __ _  ___ _ __  _ __ ___   ___   ___  _ __ | (_) __ _| |__ | |_
#   / _` |/ _ \ '_ \| '_ ` _ \ / _ \ / _ \| '_ \| | |/ _` | '_ \| __|
#  | (_| |  __/ | | | | | | | | (_) | (_) | | | | | | (_| | | | | |_
#   \__, |\___|_| |_|_| |_| |_|\___/ \___/|_| |_|_|_|\__, |_| |_|\__|
#   |___/                                            |___/

# Moon data for 2023-10-28 23:00
# Location - latitude: 50.790707850000004 | longitude: -2.6816552948061627
# Target Moon's azimuth: 156.55337260727157
# Target Moon's altitude: 51.48679241644569
# Target Moon's angular size: 0.5461606174045139
# Target Moon's age (days): 14.211730042770796
# Target Moon's fractional phase: 0.9997474211255863
# Target Moon's phase name: WANING_GIBBOUS
# Distance of target Moon's from Earth: 365075.8837129292 km

# Lunar altitude  51.48679241644569 deg, azimuth 156.55337260727157 deg
# lunar age 14.211730042770796 days, disc illum fraction 0.9997474211255863, angular disc size 0.5461606174045139 deg

void light lunar
0
0
3 16.371726561054125 15.592120534337262 13.253302454186672

lunar source moon
0
0
4 0.2477670055152368 -0.571279794378561 0.7824646365892849 0.5461606174045139
```


