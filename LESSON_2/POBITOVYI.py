
#ПОБИТОВЫЕ ОПЕРАТОРЫ
#x << y - побитовый сдвиг влево
#x >> y - побитовый сдвиг вправо
#x & y - побитовое И
#x ^ y - побитовое исключающее ИЛИ
#x | y - побитовое ИЛИ
#~x - побитовое НЕ
'''
a=50
b=bin(a)
print(b)
0b110010
>>> b<<1

>>> a<<1
100
>>> bin(100)
'0b1100100'
>>> '''
#&
a=40
b=15
c=a&b
print(bin(a))
print(bin(b))
print(bin(c))
#|
a=40
b=15
c=a | b
print(bin(a))
print(bin(b))
print(bin(c))
#^
a=40
b=15
c=a ^ b
print(bin(a))
print(bin(b))
print(bin(c))
#~
a=40
b=15
c=~a
d=~b
print(bin(a))
print(bin(b))
print(bin(c))
print(bin(d))
#<< >>
a=40
b=a<<1
c=a>>1
print(bin(a))
print(bin(b)) # 40*2**1
print(bin(c)) # 40/2**1

# ЕЛЕНИЕ ПО МОДУЛЮ
a=1/3
b=1%3
print(a,b)
#
num = 11

if (num % 2) == 0:
   print(num, "is even")
else:
   print(num, "is odd")
#
def isPrimeNumber(num):
  if num < 1:
    return False
  for i in range(2, num):
    if (num % i) == 0:
      return False
  else:
    return True
print(isPrimeNumber(num))
#
def secondsToMinutes(sec):
  seconds = sec // 60
  minutes = sec % 60
  return "%d minutes and %d seconds" % (minutes, seconds)

print(secondsToMinutes(657))

