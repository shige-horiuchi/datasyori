import pandas as pd

df = pd.read_csv(r'C:\SuperBOX\work\data\horiuchi\受注（過去）.csv', encoding = 'CP932', header = 0)
# df = pd.read_csv('受注old.csv', encoding = 'CP932', header = 0)
count = 0
zyucyuu = 0

for meisai in df.values:
    match = meisai[9].find("大隅うなぎ")
    if match != -1:
        count += 1
        zyucyuu += meisai[14]

count_c = '{:,}'.format(count)
zyucyuu_c = '{:,}'.format(zyucyuu)

print('該当件数：', count_c, '受注金額：', zyucyuu_c)