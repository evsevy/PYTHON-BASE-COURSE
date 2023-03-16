import pandas as pd
import numpy as np

df = pd.DataFrame({'DATE': [1, 2, 3, 4, 5],
                   'VOLUME': [100, 200, 300,400,500],
                   'PRICE': [214, 234, 253,272,291]})

print(df)

"""
Допустим, ситуация требует сместить все строки в датафрейме или отобразить в
нем цену акций предыдущего дня. Перед нами может стоять задача вывести
среднюю температуру последних трех дней. Так вот shift()
идеально подходит для всех этих целей.
Данная функция в Pandas сдвигает индекс на желаемое число периодов.
Она принимает скалярный параметр под названием период, который представляет
число сдвигов по требуемой оси. shift() пригодится для работы с
данными временных рядов.
Можно воспользоваться fill_value для заполнения за пределами граничных значений.
"""
print(df.shift(1))
print(df.shift(1,fill_value=0))


#
"""
При необходимости вывести цену акций предыдущего дня
в новом столбце применяем shift(
) следующим образом:
Мы можем легко вычислить среднюю цену акций за три последних дня и создать новый столбец,
как показано ниже:
"""
df['LAST_3_DAYS_AVE_PRICE'] = (df['PRICE'].shift(1,fill_value=0) + 
                               df['PRICE'].shift(2,fill_value=0) + 
                               df['PRICE'].shift(3,fill_value=0))/3
print(df)

#Можно пойти дальше и получить значение из следующего временного интервала или ряда:
df['TOMORROW_PRICE'] = df['PRICE'].shift(-1,fill_value=0)
print(df)
# ДОБАВЛЕНИЕ СТОЛБЦЕВ В КОНЦЕ И МЕЖДУ:

#df['Population density'] = df['City Population']/df['City Area']
#df.insert(loc=3, column='Population density', value=(df['City Population']/df['City Area']))

a = pd.Index([3,3,4,2,1,3, 1, 2, 3, 4, np.nan,4,6,7])
a.value_counts()


b = pd.Series(['ab','bc','cd',1,'cd','cd','bc','ab','bc',1,2,3,2,3,np.nan,1,np.nan])
b.value_counts()

df = pd.DataFrame(np.arange(15).reshape(-1, 3), columns=['A', 'B','C'])
print(df)


#С помощью mask проверяем делится ли элемент на 2 без остатка. 
#При соотвествии условию меняем знак элемента

print(df.mask(df % 2 == 0,-df))

import pandas as pd
import numpy as np
df = pd.DataFrame({'HEIGHT': [170,78,99,160,160,130,155,70,70,20],
                   'WEIGHT': [50,60,70,80,90,90,90,50,60,70]},
                   index=['A','B','C','D','E','F','G','H','I','J'])
print(df)
#Поиск наибольших трех, для наименьших: nsmallest()
dfl = df.nlargest(3,'HEIGHT')
print(dfl)

#        АГРЕГАЦИИ
# pip install Scikit-learn

import numpy as np # линейная алгебра
import pandas as pd # обработка данных, CSV файл ввода-вывода (например, pd.read_csv)
from sklearn.datasets import load_boston

boston = load_boston()
df = pd.DataFrame(data=boston.data,columns=boston.feature_names)
df['price']=boston.target
print(df.head())

print(df.describe(),'\n')

a=df['RM_levels']=df['RM'].apply(lambda x: 'low' if x<5.8 else 'middle' if x<6.6 else 'high')
print(a)
b=df['price_levels']=df['price'].apply(lambda x: 'low' if x<
                                       17 else 'middle' if x<25 else 'high')
print(b)
c=df[['RM','RM_levels','price','price_levels']].head()
print(c,'\n,\n ')

##############################

df_price = df.groupby(by=['price_levels']).mean()
print(df_price)
print(df.info())

d=df['price_levels']=df['price_levels'].astype('category')
print(d)
e=df['price_levels'].cat.reorder_categories(['low','middle','high'], inplace=True)
print(e)
f=df['RM_levels']=df['RM_levels'].astype('category')
print(f)
h=df['RM_levels'].cat.reorder_categories(['low','middle','high'], inplace=True)
print(h,'\n,\n ' )
df_price = df.groupby(by=['price_levels'],as_index=False).mean()
print(df_price)

df_price = df.groupby(by=['price_levels'],as_index=False)[['price','RM']].mean().sort_values(by='price_levels', ascending=True)
print(df_price)

df_price = df.groupby(by=['price_levels'],as_index=False)[['CRIM','LSTAT']].apply(lambda v: v.max()-v.min())
print(df_price)
