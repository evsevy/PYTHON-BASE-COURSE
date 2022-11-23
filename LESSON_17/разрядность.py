n=int(input())
r=[]
while n>0:
    r.append(n%10)
    n=n//10
if len(r) != 5:
    print("Число не 5-разрядное")
else:
    for i,k in enumerate(r):
        print(i+1,"-й разряд =",k)




n = input('Введите пятиразрядное число >> ')
if n.isnumeric():
    if len(n) == 5:
        print(f'1-ый разряд - {n[-1]}')
        print(f'2-ой разряд - {n[-2]}')
        print(f'3-ий разряд - {n[-3]}')
        print(f'4-ый разряд - {n[-4]}')
        print(f'5-ый разряд - {n[-5]}')
    else:
        print(f'Число не пятиразрядное')
else:
    print(f'Это не число')
