#creates text
import random
def generator(n, markov): # generates text n words long

	first=random.choice(markov.keys())

	finalText=list(first)

	while len(finalText)< n: #while we are not n long yet
		key=(finalText[-2],finalText[-1])
		if key not in markov.keys():
			return finalText
		else:		
			finalText.append(random.choice(markov[key].keys()))
	return finalText