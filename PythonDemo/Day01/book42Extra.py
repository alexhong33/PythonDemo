'''
Created on 2017年6月3日

@author: Alex
'''

class Student(object):
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def print_score(self):
        print('%s: %s' % (self.name, self.score))
        

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
print(bart)
print(Student)