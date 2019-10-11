import pandas as pd
import csv

path = r'C:\Users\s.horiuchi\Documents\Python\auto'
df1 = pd.read_csv(path + r'\顧客.csv', encoding = 'CP932', header = 0)
df2 = pd.read_csv(path + r'\受注.csv', encoding = 'CP932', header = 0)

marged = pd.merge(df1, df2, on = '顧客番号')
marged.to_csv('顧客受注.csv', index = False, quoting = csv.QUOTE_ALL, encoding = 'cp932')