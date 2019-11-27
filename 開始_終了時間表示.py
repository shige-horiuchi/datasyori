import pandas as pd
import time
import datetime
import csv

now_s = datetime.datetime.now()
print('開始時間：', now_s)

# ファイル読込み
s = time.time()
path = r'C:\Superbox\work\data\horiuchi'
df1 = pd.read_csv(path + r'\都道府県.csv', encoding = 'cp932', header = 0)
e = time.time()
syori = e - s
print('　ファイル読込み：', syori)

now_e = datetime.datetime.now()
print('終了時間：', now_e)

syori_t = now_e - now_s
print('処理時間：', syori_t)