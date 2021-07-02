from os import replace
import numpy as np
from numpy.core.fromnumeric import product
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

details = pd.read_csv('customers.csv')
duplicateRowsDF = details[details.duplicated(['1'])]
index = duplicateRowsDF.index;
print(index)
for idx in (index):
    details.at[idx,'1'] = id_generator(5,details.at[idx,'3'])

duplicateRowsDF = details[details.duplicated(['1'])]
print("Duplicate Rows based on a single column are:", duplicateRowsDF, sep='\n')
details.to_csv('customers.csv',index=False)