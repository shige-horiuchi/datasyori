import pandas as pd
import time
import csv
from openpyxl import Workbook

path = r'C:\Superbox\work\data\horiuchi'
df = pd.read_csv(path + r'\受注（過去）.csv', encoding = 'cp932', header = 0)
kensaku_key = '大隅うなぎ'

# クエリー処理
s = time.time()

cyusyutu = df.query(f'商品名.str.contains("{kensaku_key}")', engine='python')
# cyusyutu.to_csv('抽出テスト１.csv', index = False, quoting = csv.QUOTE_ALL, encoding = 'cp932')

e = time.time()
syori = e - s
print('クエリー処理：', syori)

# for処理
s = time.time()
list = []
for meisai in df.values:
    # match = meisai[9].find("{kensaku_key}")
    match = meisai[9].find("大隅うなぎ")
    if match != -1:
        list.append(meisai) 
# df_out = pd.DataFrame(list)
# df_out.to_csv('抽出テスト２.csv', index = False, quoting = csv.QUOTE_ALL, encoding = 'cp932')
e = time.time()
syori = e - s
print('for処理：', syori)