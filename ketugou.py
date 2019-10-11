import pandas as pd
import glob
import csv

path = r'C:\Users\s.horiuchi\Documents\Python\auto'
allfiles = glob.glob(path + r'\受注*.csv')

list = []
for file in allfiles:
    list.append(pd.read_csv(file, encoding = 'cp932', header = 0))

df = pd.concat(list)
# df.to_csv('受注.csv', index = False, quoting = csv.QUOTE_NONNUMERIC, encoding = 'cp932')
df.to_csv('受注.csv', index = False, quoting = csv.QUOTE_ALL, encoding = 'cp932')