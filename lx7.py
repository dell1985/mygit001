a = "111.11111"
b = 2
c = 3
d = 4
url1 = ("http://www.shfe.com.cn/data/dailydata/kx/pm20190327.dat")
url2 = ("http://www.shfe.com.cn/data/dailydata/kx/kx20190327.dat")
data0 = url1[43:51]
with open('lx.txt', 'a') as f:
    f.write(data0 + ',' + a + ',' + b + '\n')
