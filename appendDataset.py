from os import replace
import numpy as np
import pandas as pd
import string 
import random

def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele  
    return str1 

def id_generator(size=5, chars=string.ascii_uppercase):
    chars = chars.upper()
    chars = chars.translate({ord(c): None for c in string.whitespace})
    chars = random.sample(chars,5)
    return listToString(chars)


file = 'Cust/Customers northwind ('

for count in range (6):
    if (count == 0):
        df = pd.read_csv('Cust/Customers northwind.csv')
    else:
        loc = file + str(count) + ').csv'
        print(loc)
        df = pd.read_csv('Cust/Customers northwind.csv')
    for index, row in df.iterrows():
        df.at[index,'customer_id']=id_generator(5,row['name'])
    if (count == 0):
        targetDF = df.copy()
    else:
        frames = [targetDF,df]
        targetDF = pd.concat(frames)
cols = targetDF.columns.tolist()
cols = cols[-1:] + cols[:-1]
targetDF = targetDF[cols]
# print(targetDF.head())
print(targetDF.tail())
print(targetDF.shape)
targetDF.drop_duplicates(subset=['customer_id'])
targetDF.to_csv('appended.csv',index=False)