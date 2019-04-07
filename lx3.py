# _*_coding:utf-8 _*_
import json
import requests
import time
import pandas as pd
import csv


# 取当前日期
data0 = time.strftime('%Y-%m-%d')
# 取当日排名数据（全部）-》URL1，取当日交易快讯——》URL2
url1 = ("http://www.shfe.com.cn/data/dailydata/kx/pm20190327.dat")
url2 = ("http://www.shfe.com.cn/data/dailydata/kx/kx20190327.dat")
# 反爬虫
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}
df = pd.read_json("http://www.shfe.com.cn/data/dailydata/kx/pm20190327.dat",orient='records')
print(type(df))

print(df[5:8])