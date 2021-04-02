import json
import difflib
from difflib import get_close_matches as matcher

data = json.load(open("data.json"))

def return_word(key):
    if key in data:
        definition = data.get(key)
    else:
        option = "".join(matcher(key,data.keys(),1,0.8))
        if option == '':
            definition = ['Not found']
        else :
            choice = input(f'Do you mean {option} ? (Y/N)').lower()
            if choice == 'y':
                definition = data.get(option)    
            else : 
                definition = ['Not found']
    return definition

key = input("Enter word: ").lower()
answer = return_word(key)
print("\n".join(answer))

