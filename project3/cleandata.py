#grabs and cleans data. Also adds it together
import pickle

def clean(filename):
	#Import the file 
	input_file = open(filename,'r') 
	rawText = pickle.load(input_file)

	#Truncate the header and footer
	for i in range(0,len(rawText)):
		if rawText[i:i+6]=="ACT I.":
			start=i+6
			break
	reverseText=rawText[::-1]
	for i in range(0,len(reverseText)):
		# print reverseText[i:i+8]
		if reverseText[i:i+7]=="DNE EHT":
			end=i+7
			break
	truncText=rawText[start:-end-1]

	#Wipe text of newline and return indicators, parse into individual words, and then delete all extra spaces
	cleanerText=truncText.replace("\r","")
	cleanText=cleanerText.replace("\n","")
	wordList=cleanText.split(" ")
	while '' in wordList:
		wordList.remove('')
	return wordList