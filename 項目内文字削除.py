import pandas as pd
import csv

df = pd.read_csv('ad_in.csv', encoding = 'UTF-8', header=None, skiprows=1)
df.columns = ['レベル','日付と時刻','ソース','イベント ID','タスクのカテゴリ','メッセージ']

rep = df.replace({'\r\n': '', '\t': ''}, regex=True)
rep.to_csv('ad_out.csv', index = False, quoting = csv.QUOTE_ALL,encoding = 'UTF-8')