import pandas as pd
import time
import csv

now_s = time.ctime()
start = time.strptime(now_s)
print('開始時間：', time.strftime("%Y/%m/%d %H:%M:%S", start))

# ファイル読込み
s = time.time()
path = r'C:\Superbox\work\data\horiuchi'
df1 = pd.read_csv(path + r'\都道府県.csv', encoding = 'cp932', header = 0)
e = time.time()
syori = e - s
print('　ファイル読込み：', syori)

now_e = time.ctime()
end = time.strptime(now_e)
print('終了時間：', time.strftime("%Y/%m/%d %H:%M:%S", end))

# syori_t = now_e - now_s
# syori_total = time.strptime(syori_t)
# print('処理時間：', time.strftime("%H:%M:%S", syori_total))