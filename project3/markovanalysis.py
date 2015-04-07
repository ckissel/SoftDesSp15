"""
Overall, I think the scope of your project was not too hard or difficult, 
but I still think you implemented it really well. I like how you kept your code
as concise as possible, seperated it into seperate files, and made it really readable,
both with the comments, and the intuitive variables and process. Check fetchdata for some
more specific comments.

It's also a nice always a nice bonus when your code works and does something interesting.
I'm pretty entertained by the result.

I know you can do a lot more though, and I'm especially excited to see where you can take your
soft-des project. It sounds really cool with a blending of software and mech-e skills.

Grade:
+Functionality: 4/5 (-1 for difficulty, but good implementation)
+Documentation: 5/5 (Great file organization and commenting)
+Style: 5/5 (Great - readable, and good use of libraries)
+CheckIn: yes
+Total: 4.75/5
"""


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

