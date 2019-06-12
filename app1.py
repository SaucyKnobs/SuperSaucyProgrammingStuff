import json
import difflib
from difflib import get_close_matches #Imports a 3d party object that will return a list of the best/ 'good enough' mathces.
data = json.load(open("data.json")) #data file of a dictonary 

def translate(w): #Function
	w = w.lower() #checks dictionary for lowercase word
	if w in data:
		return data[w]
	elif w.title() in data: #Checks the dictionary for a title/noun
		return data[w.title()]
	elif w.upper() in data: #Checks the dictionary for an all uppercase word (USA, NATO, etc.)
		return data[w.upper()]
	elif len(get_close_matches(w, data.keys())) > 0: #Checks to see if there is anything resembling the word input.
		yn = input('Did you mean %s instead? Enter Y if yes, or N if no. ' % get_close_matches(w, data.keys())[0])
		if yn == "Y" or 'y' or '':
			return data[get_close_matches(w, data.keys())[0]] #If yes, returns the word that most resembles your word
		else:
			return 'Please check your spelling! '

	else:
		return 'The word doesnt exist. Please double check. '

word = input('Enter Word: ') #Asks user for a word

output = translate(word) #Plugs input into function defined above

if type(output) == list: #without this the output would have each letter in a defferent row making the string extremely long
	for item in output:
		print(item)
else:
	print()
