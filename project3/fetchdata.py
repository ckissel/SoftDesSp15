import pickle
from pattern.web import * #Psst, careful importing all of a library like this. 
# It may overwrite functions you already have in other parts of your code, and could lead to a mess. 
# You could instead do something like:

# import pattern.web as p, and now you can more easily call it's funcitons with little typing such as
# p.function()

#Super clean code. Nice use of libraries

macbeth_full_text = URL('https://www.gutenberg.org/cache/epub/1129/pg1129.txt').download()
midsummer_full_text = URL('https://www.gutenberg.org/cache/epub/1778/pg1778.txt').download()

f = open('macbeth_full_text','w') #Pssst, maybe don't call these f and g, but other than that, super intuitive
pickle.dump(macbeth_full_text,f)
f.close()

g = open('midsummer_full_text','w')
pickle.dump(midsummer_full_text,g)
g.close()