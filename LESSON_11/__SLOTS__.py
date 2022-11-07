
# РАБОТА С ПАМЯТЬЮ '__SLOTS__'

"""
class NO_SLOTS():
    def __init__(self, a, b):
        self.a = a
        self.b = b

s = NO_SLOTS(10, 20)
#print(s.__dict__)
#print(s.__dir__)
#print(s.__class__)
#s.a = 100
#print(s.a)
#s.j = 100
#print(s.__dict__)
#print(s.__sizeof__() + s.__dict__.__sizeof__())

"""

class WITH_SLOTS():

#    CLASS_ATR = '@'
    
    __slots__ = ('a','b')
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

s = WITH_SLOTS(10,20)
#print(s.__dict__)
#del s.a
#s.a = 100
#print(s.CLASS_ATR)
#print(s.__sizeof__())

