class METHOD():
    
     x = 10
     y = 20
     
     @classmethod
     def _m(cls, g):
         return METHOD.x + g + METHOD.y

     def __init__(self, a, b):
         self.a = a
         self.b = b
# МЕТОД ЭКЗЕМПЛЯРА:
     def _q(self):
         return self.a + self.b

     @staticmethod
     def _b(x, y):
         return x + y
        
     

obj_q = METHOD(3, 4)
result = obj_q._q()  # METHOD._q(obj_q)
print(result)
print(METHOD._m(10)
print(METHOD._b(30,50))
#print(self._b(self.x, self.y))
















    
    










