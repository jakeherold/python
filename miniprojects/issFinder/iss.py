#!/bin/python3
# International Space Station Finder
# A mini-project for fun and no profit
# Created by Jake Herold
# If you're reading, utilizing, redistributing, or learning from this code you hearin agree to not judge my terrible code. 
#
# Version 0.1.0

# Modules
import urllib.request
import json

# Get basic API data and assign to a variable to manipulate within the script. 
astroUrl = 'http://api.open-notify.org/astros.json'
astroResponse = urllib.request.urlopen(astroUrl)
astroResult = json.loads(astroResponse.read())

stationUrl = 'http://api.open-notify.org/iss-now.json'
stationResponse = urllib.request.urlopen(stationUrl)
stationResult = json.loads(stationResponse.read())

print("The " + str(astroResult['number']) + " astronauts presently in space are: ")
for i, item in enumerate(astroResult['people']):
    print("\t" + item['name'] + "is currently on the " + item['craft'])

print("\n" + str(stationResult))










