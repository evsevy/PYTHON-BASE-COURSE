
#АРГУМЕНТ "KEY"
DOCS = (('a',4),('b',1),('c',9),('d',7))

s = sorted(DOCS, key = lambda x: x[-1])
print(s)
