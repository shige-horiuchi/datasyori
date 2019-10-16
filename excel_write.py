import pandas as pd
import csv
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

path = r'C:\Users\s.horiuchi\Documents\Python\datasyori'
df = pd.read_csv(path + r'\集計.csv', encoding = 'cp932', header = 0, dtype = {'電話番号': str, '郵便番号_x': str})
ws.append(df.columns.tolist())
for row in df.values:
    ws.append(list(row))

ws.title = '処理結果'
wb.save('結果.xlsx')