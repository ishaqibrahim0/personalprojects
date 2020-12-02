import requests
import re
import gmaps

# acquired api key from google maps api
api_key = 'AIzaSyAMs5Ir8dS4-e7LkpByMR-c7M95RnwnU4g'
start = input("Enter Start: ")
destination = input("Enter Destination: ")
mode = input('Enter mode of transport: ')
# Extracting api info to maps.google api's to get the data
result = requests.get(
    "https://maps.googleapis.com/maps/api/directions/json?origin=" + start + "&destination=" + destination + "&mode=" + mode + "&key=" + api_key)
# https://maps.googleapis.com/maps/api/directions/json?origin=Boston+MA&destination=Santa+Clara+CA&mode=driving&key=AIzaSyAMs5Ir8dS4-e7LkpByMR-c7M95RnwnU4g
# return result in json format
routedata = result.json()

# extracting json data
print("Total Distance time: " + routedata["routes"][0]["legs"][0]["duration"]["text"])
count = 1

# Print each steps
for step in routedata["routes"][0]["legs"][0]["steps"]:
    print("Step " + str(count) + ":")
    initial_steps = "In " + step["distance"]["text"] + ", " + step["html_instructions"] + ". This will take you " + \
                    step["duration"]["text"]
    # notes which tags to remove from string
    clean = re.compile('<.*?>')
    # applies tag removal to initial text
    directions = re.sub(clean, "", initial_steps)
    print(directions)
    # makes sure step is in increasing sequential order
    count = count + 1
gmaps.configure(api_key='api_key')
fig = gmaps.figure()
city_1 = (37.2753, -107.880067)
city_2 = (37.7749, -122.419416)
layer = gmaps.directions.Directions(city_1, city_2, mode='car')
fig.add_layer(layer)
print(fig)
