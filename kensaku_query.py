import pandas as pd
import re
import csv

df = pd.read_csv('受注new.csv', encoding = 'CP932', header = 0)

kensaku_key = 'セット'

cyusyutu = df.query(f'商品名.str.contains("{kensaku_key}")', engine='python')
# cyusyutu = df.query('商品名.str.contains("' + kensaku_key + '")', engine='python')
# cyusyutu = marged.query('商品名.str.contains("セット")', engine='python')
cyusyutu.to_csv('受注抽出.csv', index = False, quoting = csv.QUOTE_ALL, encoding = 'cp932')