# _*_coding:utf-8_*_
import csv
import json
import requests




ymd = csv.reader(open("add4.csv"))





for row in ymd:

    # 输出的每一行是一个list,list中的每一个元素转换成了string类型
    aaa = str(row[0:1])
#取日期部分
    aaa=aaa[2:10]
    url_a = "http://www.shfe.com.cn/data/dailydata/kx/pm"
    print(aaa)
    url1 = url_a + aaa + ".dat"
    print('url1=',url1)

    data00= aaa
    print(data00)
    #反爬虫
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
    }

    jsonbj1 = json.loads(requests.get(url1, headers=headers).text)

    for i1 in jsonbj1['o_cursor']:
        with open('pm1.csv', 'a') as f:
            f.write(data0 + ',' + str(i1['RANK']) + ',' + i1['PARTICIPANTABBR1'] + ',' + i1['PRODUCTNAME'] + ',' + i1[
                'INSTRUMENTID'] + ',' + str(i1['CJ1']) + ',' + str(i1['CJ1_CHG']) + '\n')

    # # 期货持多仓保存在pm22.csv
    for i2 in jsonbj1['o_cursor']:
        with open('pm2.csv', 'a') as f:
            f.write(data0 + ',' + str(i2['RANK']) + ',' + i2['PARTICIPANTABBR2'] + ',' + i2['PRODUCTNAME'] + ',' + i2[
                'INSTRUMENTID'] + ',' + str(i2['CJ2']) + ',' + str(i2['CJ2_CHG']) + '\n')

    # 期货持多仓量变化记录在 .csv
    for i3 in jsonbj1['o_cursor']:
        with open('pm3.csv', 'a') as f:
            f.write(data0 + ',' + str(i3['RANK']) + ',' + i3['PARTICIPANTABBR3'] + ',' + i3['PRODUCTNAME'] + ',' + i3[
                'INSTRUMENTID'] + ',' + str(i3['CJ3']) + ',' + str(i3['CJ3_CHG']) + '\n')

    # 期货持空仓量变化记录在 pm3csv
