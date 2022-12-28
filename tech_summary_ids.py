#requirements
import requests
import json
import time


#Get all of the individual UUIDs for the technologies. The summary pages
#doesn't have the full info so we have to get the list of UUIDs and then 
#loop through those

#setup API route/keys
base_url = "http://labpartnering.org/api/v2/technology-summaries?page="
api_key = <key_goes_here> 
query_params = {"api_key": api_key}

#set initial variables and things we need from returned json
next_page_url = ""
last_page = 184
current_page = 1
uuid_values_list = []
uuid_list = []

url = base_url + str(current_page)

#This delay in the loop is annoying but necessary b/c after 60 requests it sends empty responses
while current_page < last_page: 
    time.sleep(3)
    #request to Nrel api
    api_response = requests.get(url, params=query_params, allow_redirects=True)

    #make sure we can store responses at JSON and move on
    try:
        nrel_data = api_response.json()
        
    except:
        print("This URL cannot form proper json: " + url)
        new_page = current_page + 2
        url = base_url + str(new_page)
        continue

    #can uncomment print if things don't seem to be working
    #print("Success on page: " + url)

    #reset variables for loop
    current_page = nrel_data.get('current_page')
    next_page_url = nrel_data.get('next_page_url')
    last_page = nrel_data.get('last_page')
    url = next_page_url

    #throw out the metadata and dict>list
    raw_data_lines = nrel_data["data"]

    #store just the UUIDs from Technologies Summary
    uuid_values_list.append([ dict['uuid'] for dict in raw_data_lines ])
    
#Finally change List of lists into flat list
#Iterate through the outer list
for element in uuid_values_list:
    if type(element) is list:
        # If the element is of type list, iterate through the sublist
        for item in element:
            uuid_list.append(item)
    else:
        uuid_list.append(element)
