import pandas as pd
import time
import datetime
import csv
from openpyxl import Workbook

now_s = datetime.datetime.now()
print('開始時間：', now_s)

# ファイル読込み
s = time.time()
path = r'C:\Superbox\work\data\horiuchi'
df1 = pd.read_csv(path + r'\顧客.csv', encoding = 'cp932', header = 0, dtype = {'電話番号': str, '郵便番号': str})
df2 = pd.read_csv(path + r'\受注（最新）.csv', encoding = 'cp932', header = 0)
df3 = pd.read_csv(path + r'\受注（過去）.csv', encoding = 'cp932', header = 0)
e = time.time()
syori = e - s
print('　ファイル読込み：', syori)

# 受注　結合
s = time.time()
zyucyu = pd.concat([df2, df3])
e = time.time()
syori = e - s
print('　結合：', syori)

# 顧客＋受注　マッチング
s = time.time()
marged = pd.merge(df1, zyucyu, on = '顧客番号')
e = time.time()
syori = e - s
print('　マッチング：', syori)

# 商品名　検索
s = time.time()
kensaku_key = '大隅うなぎ'
cyusyutu = marged.query(f'商品名.str.contains("{kensaku_key}")', engine='python')
# cyusyutu = marged.query('商品名.str.contains("' + kensaku_key + '")', engine='python')
# cyusyutu = marged.query('商品名.str.contains("大隅うなぎ")', engine='python')
e = time.time()
syori = e - s
print('　検索：', syori)

# 集計　姓＋名＋電話番号＋郵便番号＋住所
s = time.time()
syukei = cyusyutu.groupby(['姓', '名', '電話番号', '郵便番号_x', '住所'], as_index = False).agg({'受注日': 'max', '受注番号': 'size', '受注金額': 'sum'}) # size 要素数
e = time.time()
syori = e - s
print('　集計：', syori)

# csv出力
# syukei.to_csv('集計.csv', index = False, quoting = csv.QUOTE_ALL, encoding = 'cp932')

# Excel出力
s = time.time()
wb = Workbook()
ws = wb.active

path = r'C:\Users\s.horiuchi\Documents\Python\datasyori'
# df = pd.read_csv(path + r'\集計.csv', encoding = 'cp932', header = 0, dtype = {'電話番号': str, '郵便番号_x': str})
ws.append(syukei.columns.tolist())
for row in syukei.values:
    ws.append(list(row))

ws.title = kensaku_key # Excel sheet名
# ws.title = '大隅うなぎ' # Excel sheet名
wb.save('処理結果.xlsx')
e = time.time()
syori = e - s
print('　出力：', syori)

now_e = datetime.datetime.now()
print('終了時間：', now_e)

syori_t = now_e - now_s
print('処理時間：', syori_t)