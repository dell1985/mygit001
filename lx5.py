# _*_coding:utf-8 _*_
import json
import requests
import time
import pandas as pd
from pandas.io.json import json_normalize

# 取当前日期
data0 = time.strftime('%Y-%m-%d')
# 取当日排名数据（全部）-》URL1，取当日交易快讯——》URL2
url1 = ("http://www.shfe.com.cn/data/dailydata/kx/pm20190327.dat")
url2 = ("http://www.shfe.com.cn/data/dailydata/kx/kx20190327.dat")
# 反爬虫
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}
# r1 = requests.get(url1, headers=headers).text  # 取回数据转成结果是字符串类型
# r2 = requests.get(url2, headers=headers).text
# ret3 = requests.get(url1).text  # 如果没有服务器没有反爬虫的措施，可以这样简写
ret3 = requests.get(url1)
print(type(ret3))
print(type(ret3.text))
r1 = json.loads(requests.get(url1, headers=headers).text)
r2 = json.loads(requests.get(url2, headers=headers).text)
print(r1)
print(r2)
print(type(r1))

temp1 = r1['o_cursor']
temp2 = r2['o_curinstrument']
print(temp1)
print(temp2)
print(type(temp1))

