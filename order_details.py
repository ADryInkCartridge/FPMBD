from os import replace
import numpy as np
import pandas as pd
import string 
import random

from pandas.core.base import NoNewAttributesMixin
prod = pd.read_csv('products.csv')
print(prod.head())

total = []

for i in range (1,250000,1):
    for j in range (random.randint(1,20)):
        # row['order_id'] = i
        # row['product_id'] = random.randint(1,2000)
        # row['quantity'] = random.randint(1,200)

        dis = random.randint(1,1000)
        if (dis > 800):
            # row['discount'] = 0.05
            discount = 0.05
        elif (dis > 850):
            # row['discount'] = 0.10
            discount = 0.10
        elif (dis > 950):
            # row['discount'] = 0.15
            discount = 0.15
        elif (dis > 995):
            # row['discount'] = 0.20
            discount = 0.20
        else:
            # row['discount'] = 0
            discount = 0
        idx = random.randint(1,2000)
        new_row = [i, idx ,prod.at[idx-1,'6'],random.randint(1,200),discount]
        total.append(new_row)
# print(total)
df = pd.DataFrame(total,columns=['order_id','product_id','unit_price','quantity','discount'])
df.to_csv('order_details.csv',index=False)