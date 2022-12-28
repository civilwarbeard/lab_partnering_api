#requirements
import requests
import json
from csv import DictWriter
import time

#This file will take the UUIDs and fetch the individual technologies and then convert into CSV
#variables api key & url for individual Tech
url = "https://labpartnering.org/api/v2/technology-summaries/"
api_key = "RCDQEfBKGukPbjI1o1TCaRxODatVTH47rTaXrVqM" 
query_params = {"api_key": api_key}


#Loop through uiud_list and grab individual technologies

with open('nrel.csv', 'w', newline='') as file:
    fieldnames = ["id","title", "image", "tiny_url", "public_links", "attachments",
                 "videos", "patents", "expert", "summary", "description", 
                 "applications_and_industries", "benefits", "development_stage",
                 "internal_number", "tags", "labs"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    
    for uuid in uuid_list: 
    	#pace out requests to Nrel api
    	time.sleep(2)

        new_url = url + uuid

        api_response = requests.get(new_url, params=query_params, allow_redirects=True)
    
        technology = api_response.json()
        print("Looks good")

        writer.writerow(technology)
