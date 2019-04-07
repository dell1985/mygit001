url1 = ("ahttp://www.shfe.com.cn/data/dailydat/kx/pm20190327.dat")
url2 = ("http://www.shfe.com.cn/data/dailydata/kx/kx20190327.dat")
ddd=url1[43:51]
print(ddd)
#浮点保留2位小数点
a=1.12345
print(type(a))
print(a)
print(float('%.2f' % a))
c=12345678944444445.123456677898
print(c)
print(type(c))
c=("{:.2f}".format(c))
print(c)
print(str(c))