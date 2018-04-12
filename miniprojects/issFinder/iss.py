#!/bin/python3
# International Space Station Finder
# A mini-project for fun and no profit
# Created by Jake Herold
# If you're reading, utilizing, redistributing, or learning from this code you hearin agree to not judge my terrible code. 
#
# Version 0.1.2

# Modules
import urllib.request
import json
import time

# Get basic Astronaut API data and assign to a variable to manipulate within the script. 
astroUrl = 'http://api.open-notify.org/astros.json'
astroResponse = urllib.request.urlopen(astroUrl)
astroResult = json.loads(astroResponse.read())

# Get basic ISS Location data and assign each component to a variable
stationUrl = 'http://api.open-notify.org/iss-now.json'
stationResponse = urllib.request.urlopen(stationUrl)
stationResult = json.loads(stationResponse.read())
location = stationResult['iss_position']
lat = stationResult['iss_position']['latitude']
lon = stationResult['iss_position']['longitude']
timey = stationResult['timestamp']

# Get basic info about when the ISS will pass over a specific place and time in the future
passUrl = 'http://api.open-notify.org/iss-pass.json'
passUrlWithCoords = passUrl + '?lat=' + str(lat) + '&lon=' + str(lon)
passResponse = urllib.request.urlopen(passUrlWithCoords)
passResult = json.loads(passResponse.read())
passOverTime = passResult['response'][1]['risetime']

print("The " + str(astroResult['number']) + " astronauts presently in space are: ")
for i, item in enumerate(astroResult['people']):
    print("\t" + item['name'] + "is currently on the " + item['craft'])

print("lat is: " + lat)
print("lon is: " + lon)
print("time is: " + str(timey))

print(time.ctime(passOverTime))





