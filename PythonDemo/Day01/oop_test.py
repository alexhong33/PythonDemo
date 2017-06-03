'''
Created on 2017年6月3日

@author: Alex
'''

import random
import sys
from urllib import request

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
 
    "class %%%(%%%):" : "Make a class name %%% that is-a %%%.",
    "class %%%(object):\n\tdef _init_(self, ***)" :
        "class %%% has-a _init_ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)" : 
        "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()" : 
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."

}


# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASES_FIRST = True
else:
    PHRASES_FIRST = False
    
#load up the words from the website
for word in request.urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())
    
    
def convert(snippet, phrase):
    class_names = [w.capitalize() for w in 
                   random.sample(WORDS, snippet.count())]
    
    























