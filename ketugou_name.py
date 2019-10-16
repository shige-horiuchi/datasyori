import pandas as pd
import csv

path = r'C:\Users\s.horiuchi\Documents\Python\datasyori'
df1 = pd.read_csv(path + r'\受注new.csv', encoding = 'CP932', header = 0)
df2 = pd.read_csv(path + r'\受注old.csv', encoding = 'CP932', header = 0)

concat = pd.concat([df1, df2])
concat.to_csv('受注.csv', index = False, quoting = csv.QUOTE_ALL, encoding = 'cp932')