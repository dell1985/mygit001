# _*_coding:utf-8 _*_
import json
import requests
import time
import csv
import pandas as pd
from pandas.io.json import json_normalize

# 取当前日期
data0 = time.strftime('%Y-%m-%d')
# 取当日排名数据（全部）-》URL1，取当日交易快讯——》URL2
url1 = ("http://www.shfe.com.cn/data/dailydata/kx/pm20190404.dat")
url2 = ("http://www.shfe.com.cn/data/dailydata/kx/kx20190404.dat")
# 反爬虫
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}
# r1 = requests.get(url1, headers=headers).text  # 取回数据转成结果是字符串类型
# r2 = requests.get(url2, headers=headers).text
# ret3 = requests.get(url1).text  # 如果没有服务器没有反爬虫的措施，可以这样简写
ret3 = requests.get(url1)
print(ret3)

r1 = json.loads(requests.get(url1, headers=headers).text)
r2 = json.loads(requests.get(url2, headers=headers).text)
print(r1)
print(r2)

temp1 = r1['o_cursor']
temp2 = r2['o_curinstrument']
print(temp1)
print(temp2)

jsonbj1 = json.loads(requests.get(url1, headers=headers).text)
jsonbj2 = json.loads(requests.get(url2, headers=headers).text)

print(jsonbj1)
print(jsonbj2)

for i1 in jsonbj1['o_cursor']:

    '''
    content = {}
    content['INSTRUMENTID'] = i1['INSTRUMENTID']
    content['RANK'] = i1['RANK']
    content['PARTICIPANTABBR1'] = i1['PARTICIPANTABBR1']
    content['CJ1'] = i1['CJ1']
    content['CJ1_CHG'] = i1['CJ1_CHG']
    content['PRODUCTNAME'] = i1['PRODUCTNAME']
    '''
    f=(data0, i1['PRODUCTNAME'], i1['INSTRUMENTID'], i1['PARTICIPANTABBR1'], i1['CJ1'], i1['CJ1_CHG'], i1['RANK'])
    print(f)


for i2 in jsonbj1['o_cursor']:

    content = {}
    content['INSTRUMENTID'] = i2['INSTRUMENTID']
    content['RANK'] = i2['RANK']
    content['PARTICIPANTABBR2'] = i2['PARTICIPANTABBR2']
    content['CJ2'] = i2['CJ2']
    content['CJ2_CHG'] = i2['CJ2_CHG']
    content['PRODUCTNAME'] = i1['PRODUCTNAME']
    print(data0, i2['PRODUCTNAME'], i2['INSTRUMENTID'], i2['RANK'], i2['PARTICIPANTABBR2'], i2['CJ2'], i2['CJ2_CHG'])

for i3 in jsonbj1['o_cursor']:
    content = {}
    content['INSTRUMENTID'] = i3['INSTRUMENTID']
    content['RANK'] = i3['RANK']
    content['PARTICIPANTABBR3'] = i3['PARTICIPANTABBR3']
    content['CJ3'] = i3['CJ3']
    content['CJ3_CHG'] = i3['CJ3_CHG']
    content['PRODUCTNAME'] = i3['PRODUCTNAME']
    print(data0, i3['PRODUCTNAME'], i3['INSTRUMENTID'], i3['RANK'], i3['PARTICIPANTABBR3'], i3['CJ3'], i3['CJ3_CHG'])

for i4 in jsonbj2['o_curinstrument']:
#    print('i4=', i4)
    '''
    content = {}
    content['PRODUCTID'] = i4['PRODUCTID']
    content['PRODUCTSORTNO'] = i4['PRODUCTSORTNO']
    content['PRODUCTNAME'] = i4['PRODUCTNAME']
    content['DELIVERYMONTH'] = i4['DELIVERYMONTH']

    content['PRESETTLEMENTPRICE'] = i4['PRESETTLEMENTPRICE']
    content['OPENPRICE'] = i4['OPENPRICE']
    content['HIGHESTPRICE'] = i4['HIGHESTPRICE']
    content['LOWESTPRICE'] = i4['LOWESTPRICE']

    content['CLOSEPRICE'] = i4['CLOSEPRICE']
    content['SETTLEMENTPRICE'] = i4['SETTLEMENTPRICE']
    content['ZD1_CHG'] = i4['ZD1_CHG']
    content['ZD2_CHG'] = i4['ZD2_CHG']

    content['VOLUME'] = i4['VOLUME']
    content['OPENINTEREST'] = i4['OPENINTEREST']
    content['OPENINTERESTCHG'] = i4['OPENINTERESTCHG']
    content['ORDERNO'] = i4['ORDERNO']
    content['ORDERNO2'] = i4['ORDERNO2']
    '''
    print(data0, i4['PRODUCTID'], i4['PRODUCTSORTNO'], i4['PRODUCTNAME'], i4['DELIVERYMONTH'], i4['PRESETTLEMENTPRICE'],
          i4['OPENPRICE'], i4['HIGHESTPRICE'], i4['LOWESTPRICE'], i4['CLOSEPRICE'], i4['SETTLEMENTPRICE'],
          i4['ZD1_CHG'], i4['ZD2_CHG'], i4['VOLUME'], i4['OPENINTEREST'], i4['OPENINTERESTCHG'], i4['ORDERNO'],
          i4['ORDERNO2'])



