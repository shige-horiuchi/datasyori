import pandas as pd
import csv
import time
import datetime

now_s = datetime.datetime.now()
print('開始時間：', now_s)
# print('開始時間：', now_s.strftime('%Y/%m/%d %H:%M:%S'))

s = time.time()
list = []
with open('ad_in.csv', "r",  encoding = 'UTF-8') as file:
    reader = csv.reader(file)
    # header = next(reader) ヘッダーを読み飛ばす場合
    for row in reader:
        for i, v in enumerate(row):
            row[i] = v.replace('\n', ' ').replace('\t', '') 
        list.append(row)

df_out = pd.DataFrame(list)
df_out.to_csv('ad_out.csv', header=False, index = False, quoting = csv.QUOTE_ALL, encoding = 'UTF-8')

e = time.time()
syori = e - s
print('　for：', syori)

s = time.time()

df = pd.read_csv('ad_in.csv', encoding = 'UTF-8', header = 0)
rep = df.replace({'(.*)\n(.*)': ' ', '(.*)\t(.*)': ''}, regex=True)
rep.to_csv('ad_out1.csv', index = False, quoting = csv.QUOTE_ALL, encoding = 'UTF-8')

e = time.time()
syori = e - s
print('　pands：', syori)

now_e = datetime.datetime.now()
print('終了時間：', now_e)
# print('開始時間：', now_e.strftime('%Y/%m/%d %H:%M:%S'))

syori_t = now_e - now_s
print('処理時間：', syori_t)