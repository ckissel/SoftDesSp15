import pickle
from pattern.web import *

macbeth_full_text = URL('https://www.gutenberg.org/cache/epub/1129/pg1129.txt').download()
midsummer_full_text = URL('https://www.gutenberg.org/cache/epub/1778/pg1778.txt').download()

f = open('macbeth_full_text','w')
pickle.dump(macbeth_full_text,f)
f.close()

g = open('midsummer_full_text','w')
pickle.dump(midsummer_full_text,g)
g.close()