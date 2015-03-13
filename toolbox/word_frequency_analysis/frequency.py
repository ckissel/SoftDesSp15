""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string
import re
import pickle

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	

	with open (file_name, "r") as myfile:
	    rawText=myfile.read().replace('\n', '')


	
	wordList = re.sub("[^\w]", " ",  str(rawText)).split()
	return wordList

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	wordCounts={}
	for word in word_list:
		if word not in wordCounts.keys():
			wordCounts[word]=word_list.count(word)
	largestwords=sorted(wordCounts, key=wordCounts.get, reverse=True)[:n]
	return largestwords


if __name__ == '__main__':
	print get_top_n_words(get_word_list('pg32325.txt'),10)
	# print get_word_list('pg32325.txt')
