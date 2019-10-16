import pandas as pd
import csv

df = pd.read_csv('顧客受注.csv', encoding = 'CP932', header = 0)

cyusyutu = df.query('商品名.str.contains("セット")', engine='python')
cyusyutu.to_csv('受注抽出.csv', index = False, quoting = csv.QUOTE_ALL, encoding = 'cp932')