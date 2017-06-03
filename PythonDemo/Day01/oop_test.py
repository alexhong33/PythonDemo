'''
运行
$ python oop_test.py english


Q: 这句代码result = sentence[:]实现了什么

这是python中用来复制列表的一种方式。你使用了列表的分割切片语法[:]，得到列表从第一个到最后一个元素的切片。


class(类)：告诉python去创建一个新类型。object(对象)：有两种意思，事物的基本类型，或者事物的实例化。
instance(实例)：你通过python创建一个类所获得的。def：用来在类中定义一个函数。self：在一个类包含的函数中，
self是一个用来访问实例或对象的变量。inheritance：概念，表示一个类可以继承另一个类的特征,
就像你和你的父母。composition：概念，表示一个类可以包含其他类,就像汽车轮子。 
attribute：类所拥有的特性，通常是变量。is-a：惯用语，表示一个东西继承自另一个东西(a),
像在“鲑鱼”是“鱼”。 has-a：惯用语，表示由其他事情或有一个特征(a),如“鲑鱼有嘴。”



'''


import random
from urllib import request
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in request.urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(str(random.sample(WORDS, param_count))))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", str(word), 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", str(word), 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, str(phrase))
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print ("ANSWER:  %s\n\n" % answer)
except EOFError:
    print ("\nBye")