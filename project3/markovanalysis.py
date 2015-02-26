#overscript

from cleandata import clean
from analyzer import markovanalyzer
from createtext import generator


#execfile(fetchdata) # UN-COMMENT ME TO FETCH DATA FROM PROJECT GUTENBERG

fulltext=clean('macbeth_full_text')+clean('midsummer_full_text')

markovdict=markovanalyzer(fulltext)

result=generator(1000, markovdict)
newText=" ".join(result)

print len(result)
print newText

