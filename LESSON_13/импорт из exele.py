"""
import xlwings as xw

import pandas as pd

 

wb = xw.Book('ваш файл.xlsx')

data_excel = wb.sheets['Имя листа с данными']

data_pd = data_excel.range('A1:C4').options(pd.DataFrame, header = 1, index = False).value # Создаем DataFrame

print(data_pd)
"""
