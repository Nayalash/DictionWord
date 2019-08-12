# Diction Word
# Developed By Nayalash Mohammad
# fetch.py


import requests

word = "..."


def getData():
    try:
        url = f"""https://googledictionaryapi.eu-gb.mybluemix.net/?define={word}"""
        rawData = requests.get(url).json()
        data = rawData[0]['meaning']['noun'][0]['definition']
        return f"""The definition for that word is: {data}"""
    except:
        return "Invalid Input"

