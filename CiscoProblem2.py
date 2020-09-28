import requests
import re

# aquired api key from google maps api
api_key ='AIzaSyCbKwLmOB20qF230N6rWSDaQw_XnMYyjUI'
start = input("Enter Start: ")
destination = input("Enter Destination: ")
mode = input('Enter mode of transport: ')
# Extracting api info to maps.googleapis to get the data
result = requests.get("https://maps.googleapis.com/maps/api/directions/json?origin="+start+"&destination="+destination+"&mode="+mode+"&key="+api_key)
# https://maps.googleapis.com/maps/api/directions/json?origin=Boston+MA&destination=Santa+Clara+CA&mode=driving&key=AIzaSyCbKwLmOB20qF230N6rWSDaQw_XnMYyjUI
# return result in json format
routedata = result.json()

#extracting json data
print("Total Distance time: "+routedata["routes"][0]["legs"][0]["duration"]["text"])
count = 1;

#Print each steps
for step in routedata["routes"][0]["legs"][0]["steps"]:
    print("Step "+str(count)+":")
    initial_steps = "In "+step["distance"]["text"]+", "+step["html_instructions"]+". This will take you "+step["duration"]["text"]
    #notes which tags to remove from string
    clean = re.compile('<.*?>')
    #applies tag removal to intial text
    directions = re.sub(clean, "", initial_steps)
    print(directions)
    #makes sure step is in increasing sequential order
    count = count + 1