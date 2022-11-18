"""
x = int(input("Введите целое положительное число: "))
digs = []
while x:
    digs.append(x%10)   #берем последнюю цифру числа
    x = x//10           #отбрасываем последнюю цифру числа
   
print(digs)

#
# сортировка методом выбора
A = [2, 2, -1, -5, 55, 34, 0, 10]
N = len(A)
for i in range(N-1):
    for j in range(i+1, N):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]
print(A)

### не рабочие ###

# СОРТИРОВКА ХОАРА
import random

def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
   l_nums = [n for n in nums if n < q]
 
   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return quicksort(l_nums) + e_nums + quicksort(b_nums)



#Bubble Sort Algorithm
def bubbleSort(data):        lenght = len(data)
for iIndex in range(lenght):            swapped = False
for jIndex in range(0, lenght - iIndex - 1):
    if data[jIndex] > data[jIndex + 1]:
        data[jIndex], data[jIndex + 1] = data[jIndex + 1], data[jIndex]
        swapped = True
if swapped == False: break
    
#print(quicksort([4,6,5,3,5,9]) )
"""

# сортировка вставками
def insertion(list_nums):  
    for i in range(1, len(list_nums)):
        item = list_nums[i]
        i2 = i - 1
        while i2 >= 0 and list_nums[i2] > item:
            list_nums[i2 + 1] = list_nums[i2]
            i2 -= 1
        list_nums[i2 + 1] = item
nums = [54, 43, 3, 11, 0]  
insertion(nums) 
print(nums) # Выведет [0, 3, 11, 43, 54]
# сортировка выборкой

def selection(sort_nums):  
    for i in range(len(sort_nums)):
        index = i
        for j in range(i + 1, len(sort_nums)):
            if sort_nums[j] < sort_nums[index]:
                index = j
        sort_nums[i], sort_nums[index] = sort_nums[index], sort_nums[i]
nums = [54, 43, 3, 11, 0]  
selection(nums)
print(nums) # Выведет [0, 3, 11, 43, 54]

#сортировка слиянием
def mergeSort(sort_nums):
    if len(sort_nums)>1:
        mid = len(sort_nums)//2
        lefthalf = sort_nums[:mid]
        righthalf = sort_nums[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                sort_nums[k]=lefthalf[i]
                i=i+1
            else:
                sort_nums[k]=righthalf[j]
                j=j+1
            k=k+1
        while i<len(lefthalf):
            sort_nums[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j<len(righthalf):
            sort_nums[k]=righthalf[j]
            j=j+1
            k=k+1
nums = [54, 43, 3, 11, 0] 
mergeSort(nums)
print(nums) # Выведет [0, 3, 11, 43, 54]

# быстрая сортировка
def partition(sort_nums, begin, end):
    part = begin
    for i in range(begin+1, end+1):
        if sort_nums[i] <= sort_nums[begin]:
            part += 1
            sort_nums[i], sort_nums[part] = sort_nums[part], sort_nums[i]
    sort_nums[part], sort_nums[begin] = sort_nums[begin], sort_nums[part]
    return part
def quick_sort(sort_nums, begin=0, end=None):
    if end is None:
        end = len(sort_nums) - 1
    def quick(sort_nums, begin, end):
        if begin >= end:
            return
        part = partition(sort_nums, begin, end)
        quick(sort_nums, begin, part-1)
        quick(sort_nums, part+1, end)
    return quick(sort_nums, begin, end)
nums = [54, 43, 3, 11, 0] 
quick_sort(nums)
print(nums) # Выведет [0, 3, 11, 43, 54]

# пузырьковая сортировка
def bubble(list_nums):  
    swap_bool = True
    while swap_bool:
        swap_bool = False
        for i in range(len(list_nums) - 1):
            if list_nums[i] > list_nums[i + 1]:
                list_nums[i], list_nums[i + 1] = list_nums[i + 1], list_nums[i]
                swap_bool = True
nums = [54, 43, 3, 11, 0]   
bubble(nums)
print(nums) # Выведет [0, 3, 11, 43, 54]

#сортировка Хоара
def partition(nums, low, high):  
    # В качестве опорного выбирается средний элемент 
    # В качестве опорного возможен выбор первого, последнего
    # либо произвольного элемента 
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Когда элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), мы меняем элементы местами
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):  
    # Создаём вспомогательную функцию, вызываемую рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

# Проверка, что всё работает
random_list_of_nums = [22, 5, 1, 18, 99]  
quick_sort(random_list_of_nums)  
print(random_list_of_nums)

# Хоар 2

from random import choice
def hoar_sort(A):
    if len(A) <= 1:
        return A
    barier = choice(A)
    left = [x for x in A if  x < barier]
    middle = [x for x in A if x == barier]
    right = [x for x in A if x > barier]
    left = hoar_sort(left)
    right = hoar_sort(right)
    return left + middle + right
A=[2,4,3,6,4,7,5,1,2,4,3]
x=hoar_sort(A)
print(x)

# EVKLIDE ALGORITHM
a = int(input("Введите 1-е натуральное число: "))
b = int(input("Введите 2-е натуральное число: "))
sa = a; sb = b
b = min(sa, sb)
a = max(sa, sb)
while b:
    a,b = b, a%b
 
print("НОД(%d, %d) = %d"%(sa,sb,a))
