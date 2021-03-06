#!/bin/python3
# International Space Station Finder
# A mini-project for fun and no profit
# Created by Jake Herold
# If you're reading, utilizing, redistributing, or learning from this code you hearin agree to not judge my terrible code. 
#
# Version 0.1.3

# Modules
import requests
import json
import time

# Get basic Astronaut API data and assign to a variable to manipulate within the script. 
astroUrl = 'http://api.open-notify.org/astros.json'
astroResponse = requests.get(astroUrl)
astroResult = astroResponse.json()

# Get basic ISS Location data and assign each component to a variable
stationUrl = 'http://api.open-notify.org/iss-now.json'
stationResponse = requests.get(stationUrl)
stationResult = stationResponse.json()
location = stationResult['iss_position']
lat = stationResult['iss_position']['latitude']
lon = stationResult['iss_position']['longitude']
timey = stationResult['timestamp']

# Get basic info about when the ISS will pass over a specific place and time in the future
passUrl = 'http://api.open-notify.org/iss-pass.json'
jakeLat = 45.4824777
jakeLon = -122.7356999
passUrlWithCoords = passUrl + '?lat=' + str(jakeLat) + '&lon=' + str(jakeLon)
passResponse = requests.get(passUrlWithCoords)
passResult = passResponse.json()
passOverTime = passResult['response'][1]['risetime']


# Outputs
print("The " + str(astroResult['number']) + " astronauts presently in space are: ")
for i, item in enumerate(astroResult['people']):
    print("\t" + item['name'] + " (" + item['craft'] + ")")
print("The ISS's latitude is currently: " + lat)
print("The ISS's longitude is currently: " + lon)
print("ISS passes Portland, OR at: " + time.ctime(passOverTime))