import pandas as pd
import time
import csv
from openpyxl import Workbook

now = time.ctime()
start = time.strptime(now)
print('開始時間：', time.strftime("%Y/%m/%d %H:%M", start))

# ファイル読込み
s = time.time()
path = r'C:\Superbox\work\data\horiuchi'
df1 = pd.read_csv(path + r'\パーツ.csv', encoding = 'cp932', header = 0)
df2 = pd.read_csv(path + r'\車.csv', encoding = 'cp932', header = 0)
df3 = pd.read_csv(path + r'\販売計画_東日本.csv', encoding = 'cp932', header = 0)
df4 = pd.read_csv(path + r'\販売計画_西日本1.csv', encoding = 'cp932', header = 0)
e = time.time()
syori = e - s
print('　ファイル読込み：', syori)

# 販売計画　結合
s = time.time()
keikaku = pd.concat([df3, df4])
e = time.time()
syori = e - s
print('　結合：', syori)

# 販売計画＋車　マッチング
s = time.time()
marged1 = pd.merge(keikaku, df2, on = '商品ID')
e = time.time()
syori = e - s
print('　マッチング1：', syori)

# 販売計画＋車+パーツ　マッチング
s = time.time()
marged2 = pd.merge(marged1, df1, on = '商品ID')
e = time.time()
syori = e - s
print('　マッチング2：', syori)

# 商品名　検索
s = time.time()
cyusyutu = marged2.query('パーツ区分.str.contains("エンジン")', engine='python')
e = time.time()
syori = e - s
print('　検索：', syori)

# 集計　生産工場＋販売予定年月＋仕入先＋パーツ名
s = time.time()
syukei = cyusyutu.groupby(['生産工場', '販売予定年月', '仕入先', 'パーツ名'], as_index = False).agg({'パーツコード': 'size', '仕入価格': 'sum'}) # size 要素数
e = time.time()
syori = e - s
print('　集計：', syori)

# Excel出力
s = time.time()
wb = Workbook()
ws = wb.active

path = r'C:\Users\s.horiuchi\Documents\Python\datasyori'
ws.append(syukei.columns.tolist())
for row in syukei.values:
    ws.append(list(row))

ws.title = '結果'
wb.save('処理結果.xlsx')
e = time.time()
syori = e - s
print('　出力：', syori)

now = time.ctime()
end = time.strptime(now)
print('終了時間：', time.strftime("%Y/%m/%d %H:%M", end))