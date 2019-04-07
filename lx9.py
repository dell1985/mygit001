# _*_coding:utf-8 _*_

import csv
#初始化交易日历库
with open('ymd1.csv', 'w',encoding='utf-8') as f:
    f.write(' \n')
r1000 = csv.reader(open("2019A.csv",encoding='utf-8'))
print(r1000)
list = []
for row in r1000:
    # 输出的每一行是一个list,list中的每一个元素转换成了string类型
    aaa = str(row[0:1])
    aaa=(aaa[2:10])
    aaaa=(len(aaa))
    bbbb=(aaa[0:3])
    print(bbbb)
    print(aaaa)
    print(aaa)
   # if aaaa == 8: and aaa[0:3]=="201":
    with open('ymd3.csv', 'a',encoding='utf-8') as f:
        f.write(aaa + ',' + '\n')
