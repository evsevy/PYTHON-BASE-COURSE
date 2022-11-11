
# ВИДЫ ГЕНЕРАЦИИ СПИСКОВ

data = [i for i in range(0, 10)]
print(data)


data = [i for i in "python"]
print(data)

data = [i for i in range(0, 10) if i % 2 == 0]
print(data)


data = [i * j for i in range(0, 3) for j in range(0, 3)]
print(data)

data = [[i * j for i in range(0, 3)] for j in range(0, 3)]
print(data)


data = [(lambda i: i*i)(i) for i in range(0, 10)]
print(data)



import csv

