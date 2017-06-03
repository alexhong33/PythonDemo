'''
Created on 2017年6月3日

@author: Alex

Q：为什么我在类里创建__init__或其他函数的时候需要使用self?

如果你不实用self，像这种代码cheese = 'Frank'就是不明确的. 
代码并不清楚你指的是实例的cheese属性，还是一个叫做cheesed的全局变量。
如果你使用self.cheese='Frank'代码就会十分清楚你指的就是实例中的属性self.cheese.
'''

class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
            

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around that family",
                        "With pockets full of shells"])


happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
