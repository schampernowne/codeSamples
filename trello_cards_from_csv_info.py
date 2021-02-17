
import requests
import sys
import csv
import pandas
import numpy

file = sys.argv[1]

print(file)

def createCard(name, email, phone, notes):

    url = "https://api.trello.com/1/cards"

    query = {
        'key': {{get trello API key for your account}},
        'token': {{get trello API token for your account}},
        'idList': {{id of column}}',
        'name' : name,
        'desc' : str(email) + str(" " + phone) + str(" " + notes),
        'idCardSource': '60233b027593af49194267c0', #or another ID of a template card you want to use
        'keepFromSource': 'all'
    }

    trello_board_response = requests.request(
        'POST',
        url,
        params=query
    )


    #read a row -> get name, email, phone, notes (should be based on order)
data = pandas.read_csv(file, header='infer', na_filter=False)
print(data)

for row in data.iterrows():
    name = str(row[1]["name"])
    phone = str(row[1]["phone"])
    email = str(row[1]["email"])
    notes = str(row[1]["notes"])
    createCard(name, email, phone, notes)
    print(name + "," + phone + "," + email)
    


