# import pandas as pd
import csv

list = []
with open('ad_in.csv', "r",  encoding = 'UTF-8') as file:
    reader = csv.reader(file)
    header = next(reader) # ヘッダーを読み飛ばす
    for row in reader:
        for i, v in enumerate(row):
            row[i] = v.replace('\n', ' ').replace('\t', '') 
        list.append(row)

header = ['レベル','日付と時刻','ソース','イベント ID','タスクのカテゴリ','メッセージ']
with open('ad_out.csv', 'w', encoding = 'UTF-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in list:
        writer.writerow(row)