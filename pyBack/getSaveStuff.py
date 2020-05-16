""" File: getSaveStuff.py mocking a JSON response and saving it to someJSON.txt"""


import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

def saveJSON():
    with open('pyBack/data/someJSON.txt', 'w+') as outfile:
        json.dump(data, outfile)
