# 文字コード変換

import pandas as pd
import csv

path = r'C:\Superbox\work\data\horiuchi'
df = pd.read_csv(path + r'\都道府県.csv', encoding = 'CP932', header = 0)

df.to_csv(path + r'\都道府県_utf8.csv', index = False, quoting = csv.QUOTE_ALL, encoding = 'utf-8')