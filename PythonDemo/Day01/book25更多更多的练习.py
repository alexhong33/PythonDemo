'''
Created on 2017年6月2日

@author: Alex

总结
学习了使用
stuff.split(' ')
sorted(words)
'''
from Day01 import book25_ex25


sentence = "All good things come to those who wait."
words = book25_ex25.break_words(sentence)
print("--------------")
# stuff.split(' ')
print(words)
print("--------------")
words


sorted_words = book25_ex25.sort_words(words)
print("--------------")
# sorted(words)
print(sorted_words)
print("--------------")
sorted_words



book25_ex25.print_first_word(words)
print(words)
book25_ex25.print_last_word(words)
print(words)
words

print("--------------")
print(sorted_words)
book25_ex25.print_first_word(sorted_words)
print(sorted_words)
book25_ex25.print_last_word(sorted_words)
print(sorted_words)
sorted_words
print("--------------")
print("--------------")
sorted_words = book25_ex25.sort_sentence(sentence)
print(sorted_words)
sorted_words
book25_ex25.print_first_and_last(sentence)
print(sorted_words)
book25_ex25.print_first_and_last_sorted(sentence)
print(sorted_words)
print("--------------")
print("--------------")