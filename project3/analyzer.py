#function to create the markov dictionary for text
def markovanalyzer(text):


	markov={}
	
	#Perform Analysis
	for i in range(0,(len(text)-2)):
		trewple=(text[i],text[i+1]) #This is my dictionary key
		nextWord=(text[i+2])
		if trewple not in markov: #If this is a new trewple
			markov[trewple]={nextWord:1} #add it to the dictionary, and add an entry of 1 frequency
		else: #seen it before
			innerDict=markov[trewple]
			if nextWord in innerDict: # if we've also seen the next word
				innerDict[nextWord]+=1
				markov[trewple]=innerDict #increment the counter by 1
			else: #new nextword
				innerDict[nextWord]=1
				markov[trewple]=innerDict #add it
	return markov