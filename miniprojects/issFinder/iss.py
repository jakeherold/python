#!/bin/python3
# International Space Station Finder
# A mini-project for fun and no profit
# Created by Jake Herold
# If you're reading, utilizing, redistributing, or learning from this code you hearin agree to not judge my terrible code. 
#
# Version 0.0.1

# Modules

import urllib.request
import json

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print("The " + str(result['number']) + " astronauts presently in space are: ")
for i, item in enumerate(result['people']):
    print(item['name'])
print("There are currently " + str(result['number']) + " people in space")









