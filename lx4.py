# _*_coding:utf-8 _*_
import json
import requests
import time
import pandas as pd
from pandas.io.json import json_normalize
import string

# 取当前日期

# 取当日排名数据（全部）-》URL1，取当日交易快讯——》URL2
url1 = ("http://www.shfe.com.cn/data/dailydata/kx/pm20190403.dat")
url2 = ("http://www.shfe.com.cn/data/dailydata/kx/kx20190403.dat")
data0 = url1[43:51]
# 反爬虫
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}
# r1 = requests.get(url1, headers=headers).text  # 取回数据转成结果是字符串类型
# r2 = requests.get(url2, headers=headers).text
# ret3 = requests.get(url1).text  # 如果没有服务器没有反爬虫的措施，可以这样简写
ret3 = requests.get(url1)
print(type(ret3))

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
with open('qh1.csv', 'w') as f:
    f.write('日期,名次,期货公司名称,期货名称,合约代码,成交量,增减量' + '\n')

with open('qh2.csv', 'w') as f:
    f.write('日期,名次,期货公司名称,期货名称,合约代码,持买单,增减量' + '\n')

with open('qh3.csv', 'w') as f:
    f.write('日期,名次,期货公司名称,期货名称,合约代码,持卖单,增减量' + '\n')

with open('qh4.csv', 'w') as f:
    f.write('日期,期货名称,交割月份,前结算,今开盘,最高价,最低价,收盘价,结算参考价,涨跌1,涨跌2,成交手,持仓手数,增减量' + '\n')

with open('qh5.csv', 'w') as f:
    f.write('日期,期货名称,最高价,最低价,加权平均价,成交手,成交金额,年成交万手,年成交亿元' + '\n')

print('report_date')
for i1 in jsonbj1['o_cursor']:
    content = {}
    content['日期'] = data0
    content['合约代码'] = i1['INSTRUMENTID']
    content['名次'] = str(i1['RANK'])
    content['期货公司名称'] = i1['PARTICIPANTABBR1']
    content['成交量'] = str(i1['CJ1'])
    content['增减量'] = str(i1['CJ1_CHG'])
    content['期货名称'] = i1['PRODUCTNAME']
    print(data0, i1['PRODUCTNAME'], i1['INSTRUMENTID'], i1['PARTICIPANTABBR1'], i1['CJ1'], i1['CJ1_CHG'], i1['RANK'])
    with open('qh1.csv', 'a') as f:
        f.write(content['日期'] + ',' + content['名次'] + ',' + content['期货公司名称'] + ',' + content['期货名称'] + ',' + content[
            '合约代码'] + ',' + content['成交量'] + ',' + content['增减量'] + '\n')
# 期货成交量变化记录在 qh1.csv
for i2 in jsonbj1['o_cursor']:
    content = {}
    content['日期'] = data0
    content['合约代码'] = i2['INSTRUMENTID']
    content['名次'] = str(i2['RANK'])
    content['期货公司名称'] = i2['PARTICIPANTABBR2']
    content['持买单'] = str(i2['CJ2'])
    content['增减量'] = str(i2['CJ2_CHG'])
    content['期货名称'] = i2['PRODUCTNAME']
    print(data0, i2['PRODUCTNAME'], i2['INSTRUMENTID'], i2['RANK'], i2['PARTICIPANTABBR2'], i2['CJ2'], i2['CJ2_CHG'])
    with open('qh2.csv', 'a') as f:
        f.write(content['日期'] + ',' + content['名次'] + ',' + content['期货公司名称'] + ',' + content['期货名称'] + ',' + content[
            '合约代码'] + ',' + content['持买单'] + ',' + content['增减量'] + '\n')
# 期货持多仓量变化记录在 qh2.csv
for i3 in jsonbj1['o_cursor']:
    content = {}
    content['日期'] = data0
    content['合约代码'] = i3['INSTRUMENTID']
    content['名次'] = str(i3['RANK'])
    content['期货公司名称'] = i3['PARTICIPANTABBR3']
    content['持卖单'] = str(i3['CJ3'])
    content['增减量'] = str(i3['CJ3_CHG'])
    content['期货名称'] = i3['PRODUCTNAME']
    print(data0, i3['PRODUCTNAME'], i3['INSTRUMENTID'], i3['RANK'], i3['PARTICIPANTABBR3'], i3['CJ3'], i3['CJ3_CHG'])
    with open('qh3.csv', 'a') as f:
        f.write(content['日期'] + ',' + content['名次'] + ',' + content['期货公司名称'] + ',' + content['期货名称'] + ',' + content[
            '合约代码'] + ',' + content['持卖单'] + ',' + content['增减量'] + '\n')
# 期货持空仓量变化记录在 qh3.csv
for i4 in jsonbj2['o_curinstrument']:
    print('i4=', i4)

    content = {}
    content['日期'] = data0
    content['期货名称'] = i4['PRODUCTID']
    content['PRODUCTSORTNO'] = i4['PRODUCTSORTNO']
    content['期货名称'] = i4['PRODUCTNAME']
    content['交割月份'] = i4['DELIVERYMONTH']

    content['前结算'] = str(i4['PRESETTLEMENTPRICE'])
    content['今开盘'] = str(i4['OPENPRICE'])
    content['最高价'] = str(i4['HIGHESTPRICE'])
    content['最低价'] = str(i4['LOWESTPRICE'])

    content['收盘价'] = str(i4['CLOSEPRICE'])
    content['结算参考价'] = str(i4['SETTLEMENTPRICE'])
    content['涨跌1'] = str(i4['ZD1_CHG'])
    content['涨跌2'] = str(i4['ZD2_CHG'])

    content['成交手'] = str(i4['VOLUME'])
    content['持仓手数'] = str(i4['OPENINTEREST'])
    content['增减量'] = str(i4['OPENINTERESTCHG'])
    content['持仓手数1'] = str(i4['ORDERNO'])
    content['增减量1'] = str(i4['ORDERNO2'])

    print(data0, i4['PRODUCTID'], i4['PRODUCTSORTNO'], i4['PRODUCTNAME'], i4['DELIVERYMONTH'], i4['PRESETTLEMENTPRICE'],
          i4['OPENPRICE'], i4['HIGHESTPRICE'], i4['LOWESTPRICE'], i4['CLOSEPRICE'], i4['SETTLEMENTPRICE'],
          i4['ZD1_CHG'], i4['ZD2_CHG'], i4['VOLUME'], i4['OPENINTEREST'], i4['OPENINTERESTCHG'], i4['ORDERNO'],
          i4['ORDERNO2'])

    with open('qh4.csv', 'a') as f:
        f.write(content['日期'] + ',' + content['期货名称'] + ',' + content['交割月份'] + ',' + content['前结算'] + ',' + content[
            '今开盘'] + ',' + content[
                    '最高价'] + ',' + content['最低价'] + ',' + content['收盘价'] + ',' + content['结算参考价'] + ',' + content[
                    '涨跌1'] + ',' +
                content['涨跌2'] + ',' + content['成交手'] + ',' + content['持仓手数'] + ',' + content['增减量'] + '\n')

for i5 in jsonbj2['o_curproduct']:
    content = {}
    content['日期'] = data0

    content['期货名称'] = i5['PRODUCTNAME']

    content['最高价'] = str(i5['HIGHESTPRICE'])
    content['最低价'] = str(i5['LOWESTPRICE'])



    content['加权平均价'] = i5['AVGPRICE']


    content['成交手'] = str(i5['VOLUME'])
    content['成交金额'] = str(round(i5['TURNOVER']))
    content['年成交万手'] = str(int(i5['YEARVOLUME']))
    content['年成交亿元'] = str(int(i5['YEARTURNOVER']))
    with open('qh5.csv', 'a') as f:
        f.write(content['日期'] + ',' + content['期货名称'] + ',' + content['最高价'] + ',' + content['最低价'] + ',' + str(content[
            '加权平均价']) + ',' + content['成交手'] + ',' + content['成交金额'] + ',' + content['年成交万手'] + ',' + content[
                    '年成交亿元'] + '\n')
    with open('qh6.csv', 'a') as f:
        f.write(data0 + ',' +  i5['PRODUCTNAME'] + ',' + str(i5['HIGHESTPRICE']) + ',' + content['最低价'] + ',' + str(i5['AVGPRICE']) + ',' +
                content['成交手'] + ',' + content['成交金额'] + ',' + content['年成交万手'] + ',' + content[
                    '年成交亿元'] + '\n')