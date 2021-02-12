#Trello export from the json so that we don't have to upgrade to the business Trello - can just run this script (token and key taken out for privacy and get an out put of the data from trello cards tracking recruitment contacts)


import requests
import json 
import csv
import sys
import re

url = "https://api.trello.com/1/boards/PUfTUopS/cards"

query = {
   'key': "" # add key,
   'token': "" #add token
}

trello_board_response = requests.request(
   "GET",
   url,
   params=query
)

trello_cards = trello_board_response.json()
#build a row
#def buildRowArray(name,branch,status,description)

def getCardName(obj):
    return obj["name"]
def getCardBranch(obj):
    branches = ["South","North Tuesday", "North Wednesday", "Beacon Hill", "Central District", "Capitol Hill"]
    labels = obj["labels"]
    branch_label=[element for element in labels if element["name"] in branches]
    if branch_label != []:
        return branch_label[0]["name"]

def getCardContact(obj,type):
    description_text = str(obj["desc"])
    if str(type) == "email":
        email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', description_text)
        if email_match is not None:
            return email_match.group()
        else:
            return "none"
    elif type == "phone":
        phone_match = re.search(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', description_text)
        if phone_match is not None:
            return phone_match.group()
        else: 
            return "none"

def getCardStatus(obj):
    #grab listid
    status = obj["idList"]
    #get request with the listid -> convert to json
    url_list = "https://api.trello.com/1/lists/" + str(status)
    status_response = requests.request(
        "GET",
        url_list,
        params=query
    )
    #in the json object, grab list name, return
    return status_response.json()["name"]

#for ever card in the json object, pull the data and get the fields
with open('active_contact.txt',mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for card in trello_cards:
        name = getCardName(card)
        branch = getCardBranch(card)
        status = getCardStatus(card)
        email = getCardContact(card,"email")
        phone = getCardContact(card,"phone")
        row = [name,branch,status,email]
        csv_writer.writerow(row)
        print(name)
        print(branch)
        print(status)
        print(email)
        print(phone)
        



