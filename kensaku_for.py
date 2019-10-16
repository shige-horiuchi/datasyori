import pandas as pd
import csv

df = pd.read_csv('受注old.csv', encoding = 'CP932', header = 0)
count = 0
zyucyuu = 0
list = []

for meisai in df.values:
    match = meisai[9].find("セット")
    if match != -1:
        count += 1
        zyucyuu += meisai[14]
        list.append(meisai) 
df_out = pd.DataFrame(list)
df_out.to_csv('抽出.csv', index = False, quoting = csv.QUOTE_ALL, encoding = 'cp932')

count_c = '{:,}'.format(count)
zyucyuu_c = '{:,}'.format(zyucyuu)

print('該当件数：', count_c, '受注金額：', zyucyuu_c)