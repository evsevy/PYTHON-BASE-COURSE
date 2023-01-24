# LESSON_2
import cmath
import sys
a='诶'
b='西'
d=a.encode('utf-8')
f=b.encode('utf-8')
c=a==b
print(c,d,f)
#

l=sys.getsizeof(a)
print(l)
#
k=sys.getsizeof(b)
print(k)
#
a=(10.5).hex()

b=float.fromhex('0x1.5000000000000p+3')
print(a,b)

#COMPLEX NUMBERS
z = 3 + 4j
 
print(z.real, z.imag)
#
x=(-0.5)**0.5
print(x)
#
v=int((2 + 0j).real) #imag - float
print(v)
#
c = complex(); print(type(c)); print(c)
#
c = complex(1, 1); print(c); c = complex(1.5, -2.1); print(c); c = complex(0xF);print(c)
c = complex("1+2j"); print(c)
#
n = 255
print(n.to_bytes(length=2, byteorder="big"))
print(n)
print(int.from_bytes(b'\x06\xc1', byteorder="big"))
print(cmath.phase(1 - 2j))
print(cmath.exp(4))

"""Модуль cmath – предоставляет функции для работы с комплексными числами.

cmath.phase(x) - возвращает фазу комплексного числа (её ещё называют аргументом).
Эквивалентно math.atan2(x.imag, x.real). Результат лежит в промежутке [-π, π].

Получить модуль комплексного числа можно с помощью встроенной функции abs().

cmath.polar(x) - преобразование к полярным координатам. Возвращает пару (r, phi).

import cmath

#find the polar coordinates of complex number
print (cmath.polar(2 + 3j))
print (cmath.polar(1 + 5j))

cmath.rect(r, phi) - преобразование из полярных координат.

cmath.exp(x) - ex.

cmath.log(x[, base]) - логарифм x по основанию base. Если base не указан, возвращается натуральный логарифм.

cmath.log10(x) - десятичный логарифм.

cmath.sqrt(x) - квадратный корень из x.

cmath.acos(x) - арккосинус x.

cmath.asin(x) - арксинус x.

cmath.atan(x) - арктангенс x.

cmath.cos(x) - косинус x.

cmath.sin(x) - синус x.

cmath.tan(x) - тангенс x.

cmath.acosh(x) - гиперболический арккосинус x.

cmath.asinh(x) - гиперболический арксинус x.

cmath.atanh(x) - гиперболический арктангенс x.

cmath.cosh(x) - гиперболический косинус x.

cmath.sinh(x) - гиперболический синус x.

cmath.tanh(x) - гиперболический тангенс x.

cmath.isfinite(x) - True, если действительная и мнимая части конечны.

cmath.isinf(x) - True, если либо действительная, либо мнимая часть бесконечна.

cmath.isnan(x) - True, если либо действительная, либо мнимая часть NaN.

cmath.pi - π.

cmath.e - e. """
import cmath
x=1+2
s=(2+3j)*0.5
q=9
d=q**(1./3.)
print(d)
print(s)
print(abs(x))

def cuberoot(x):
    if x < 0:
        x = abs(x)
        cube_root = x**(1/3)*(-1)
    else:
        cube_root = x**(1/3)
    return cube_root


print(cuberoot(27))
print(round(cuberoot(-27)))

'''import numpy as np 

arr1 = [1, 8, 27, 64] 
arr2 = np.cbrt(arr1) 
print(arr2)
'''

# https://unicode-table.com

null_variable = None
not_null_variable = 'Hello There!'

# The is keyword
if null_variable is None:
    print('null_variable is None')
else:
    print('null_variable is not None')

if not_null_variable is None:
    print('not_null_variable is None')
else:
    print('not_null_variable is not None')























