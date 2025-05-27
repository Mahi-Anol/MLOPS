import pandas as pd
import os

data={'name':['Alice','bob','charlie'],
      'age':[25,30,35],
      'city':['New York','Los Angeles', 'chicago']
      }

df=pd.DataFrame(data)

df.to_csv(r'D:\MLOPS\Data Versioning\data.csv')