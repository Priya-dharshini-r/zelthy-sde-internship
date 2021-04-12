import requests


word = input("Word?")

# Getting request from the dictionary api
response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en_US/"+word)
result = response.json()

# Accessing elements from the json file
a = result[0]
b = a['meanings']
c = b[0]
d = c['partOfSpeech']
e = c['definitions']
f = e[0]
g = f['definition']

print(word+".", d+".", g)


