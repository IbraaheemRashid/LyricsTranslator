# Ian Annase
# 1/24/18

import requests
import json
from lyrics_api import *

# example call: base_url + lyrics_matcher + format_url + artist_search_parameter + artist_variable + track_search_parameter + track_variable + api_key
# example json print: print(json.dumps(api_call, sort_keys=True, indent=2))


# musixmatch api base url
base_url = "https://api.musixmatch.com/ws/1.1/"

# your api key
api_key = "&apikey=723bd4d1788a264ac6b28c02b8dd7f23"
deepl_endpoint = 'https://api-free.deepl.com/v2/translate'
deepl_auth_key = '5709494d-d0a5-2422-0803-2ce4534fbb30:fx' 

while True:
    print()
    print("Welcome to the Musixmatch API explorer!")
    print()
    print("MENU OPTIONS")
    print("1 - Search for the lyrics of a song")
    print("0 - Exit")
    print()
    choice = input("> ")
    print()

    if choice == "0":
        break

    # example
    if choice == "1":
        print("Whats's the name of the artist?")
        artist_name = input("> ")
        print("What's the name of the track?")
        track_name = input("> ")
        print()
        api_call = base_url + lyrics_matcher + format_url + artist_search_parameter + artist_name + track_search_parameter + track_name + api_key
        request = requests.get(api_call)
        data = request.json()
        data = data['message']['body']
        print("API Call: " + api_call)
        print()
        print(data['lyrics']['lyrics_body'])
        # after printing the lyrics
        lyrics = data['lyrics']['lyrics_body']

        print("Would you like to translate these lyrics? (y/n)")
        choice2 = input("> ")
        
        if choice2 == "y":
            print("Choose a target language (Es, Fr etc.): ")
            choice3 = input("> ")
            
            # make a DeepL API call to translate the lyrics
            params = {
                'auth_key': deepl_auth_key,
                'text': lyrics,
                'source_lang': 'EN', # replace with the source language code if it's not English
                'target_lang': choice3 # replace with the target language code
            }
            response = requests.post(deepl_endpoint, data=params)
            response.raise_for_status()
            translation = response.json()['translations'][0]['text']

            # print the translated lyrics
            print()
            print("Translated lyrics:")
            print(translation)
            
        elif choice2 == "n":
            print("Goodbye")
            input()
            break