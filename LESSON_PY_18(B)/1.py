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
