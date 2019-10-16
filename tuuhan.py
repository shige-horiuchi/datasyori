import pandas as pd
import time
import csv
from openpyxl import Workbook

now = time.ctime()
start = time.strptime(now)
print('開始時間：', time.strftime("%Y/%m/%d %H:%M", start))
s = time.time()

# ファイル読み込み
path = r'C:\Superbox\work\data\horiuchi'
df1 = pd.read_csv(path + r'\顧客.csv', encoding = 'cp932', header = 0, dtype = {'電話番号': str, '郵便番号': str})
df2 = pd.read_csv(path + r'\受注（最新）.csv', encoding = 'cp932', header = 0)
df3 = pd.read_csv(path + r'\受注（過去）.csv', encoding = 'cp932', header = 0)

# 受注　結合
zyucyu = pd.concat([df2, df3])

# 顧客＋受注　マッチング
marged = pd.merge(df1, zyucyu, on = '顧客番号')

# 商品名　検索
cyusyutu = marged.query('商品名.str.contains("大隅うなぎ")', engine='python')

# 集計　姓＋名＋電話番号＋郵便番号＋住所
syukei = cyusyutu.groupby(['姓', '名', '電話番号', '郵便番号_x', '住所'], as_index = False).agg({'受注日': 'max', '受注番号': 'size', '受注金額': 'sum'}) # size 要素数

# csv出力
# syukei.to_csv('集計.csv', index = False, quoting = csv.QUOTE_ALL, encoding = 'cp932')

# Excel出力
wb = Workbook()
ws = wb.active

path = r'C:\Users\s.horiuchi\Documents\Python\datasyori'
# df = pd.read_csv(path + r'\集計.csv', encoding = 'cp932', header = 0, dtype = {'電話番号': str, '郵便番号_x': str})
ws.append(syukei.columns.tolist())
for row in syukei.values:
    ws.append(list(row))

ws.title = '処理結果'
wb.save('結果.xlsx')

e = time.time()
now = time.ctime()
end = time.strptime(now)
print('開始時間：', time.strftime("%Y/%m/%d %H:%M", end))

syori = e - s
print('処理時間：', syori)