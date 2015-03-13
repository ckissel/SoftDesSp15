#Caleb Kissel
#Pig Latin Converter

def piglatin(word):
	if ((word[0] not in ['a','e','i','o','u']) and (word[1] not in ['a','e','i','o','u'])) or ((word[0] in ['a','e','i','o','u']) and (word[0] not in ['a','e','i','o','u'])):
		x=2
	else:
		x=1
	print x
	L=[word[x:],word[:x],'ay']
	return ''.join(L)


if __name__=="__main__":
	print piglatin('steph')
	print piglatin('circuits')
	print piglatin('antidisestablishmentariansim')
	print piglatin('dickbutt')