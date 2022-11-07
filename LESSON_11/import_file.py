
import file_1
#from pprint import pprint
#import sys

print(file_1.a)
print(file_1.func())
print(file_1.pi)

#print(sys.path)
print(file_1.A.x)

# Если в другой папке импортируемый файл, 
# сперва название папки-точка-имя файла     

if __name__ == '__main__':
    print(file_1.hello('EVGENY'))
