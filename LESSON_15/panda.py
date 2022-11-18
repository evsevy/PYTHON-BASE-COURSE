import pandas as pd
import numpy as np

df = pd.DataFrame({'DATE': [1, 2, 3, 4, 5],
                   'VOLUME': [100, 200, 300,400,500],
                   'PRICE': [214, 234, 253,272,291]})
"""
df['LAST_3_DAYS_AVE_PRICE'] = (df['PRICE'].shift(1,fill_value=0) + 
                               df['PRICE'].shift(2,fill_value=0) + 
                               df['PRICE'].shift(3,fill_value=0))/3
"""



print(df)
 #Поиск среднего 
a = pd.Index([3,3,4,2,1,3, 1, 2, 3, 4, np.nan,4,6,7])
print(a.value_counts())

# Поиск наибольшего значения.
import pandas as pd
import numpy as np
df = pd.DataFrame({'HEIGHT': [170,78,99,160,160,130,155,70,70,20],
                   'WEIGHT': [50,60,70,80,90,90,90,50,60,70]},
                   index=['A','B','C','D','E','F','G','H','I','J'])
print(df)



dfl = df.nlargest(3,'HEIGHT')
print(dfl)
# Наименьшего
dfs = df.nsmallest(3,'WEIGHT')
print(dfs)

