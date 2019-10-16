import pandas as pd
import csv

path = r'C:\Users\s.horiuchi\Documents\Python\datasyori'
df = pd.read_csv(path + r'\受注抽出.csv', encoding = 'CP932', header = 0, dtype = {'電話番号': str})

syukei = df.groupby(['姓','名','電話番号'], as_index = False).agg({'受注日': 'max', '受注番号': 'size', '受注金額': 'sum'}) # size 要素数
# syukei = df.groupby(['姓','名','電話番号'], as_index = False).agg({'受注日': 'max', '受注番号': 'count', '受注金額': 'sum'}) # count 要素の個数
syukei.to_csv('集計.csv', index = False, quoting = csv.QUOTE_ALL, encoding = 'cp932')