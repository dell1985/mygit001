import pandas as pd



provice = {"省份":{"pro1":"上海","pro2":"浙江","pro3":"江苏"},
           "年份":{"pro1":"2001","pro2":"2009","pro3":"2009"},
           "人口":{"pro1":"99822123","pro2":"34434343","pro3":"9085556"},
          }
data = pd.DataFrame(provice)

print(data)