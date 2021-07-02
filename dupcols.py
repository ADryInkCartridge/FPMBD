from os import replace
import numpy as np
from numpy.core.fromnumeric import product
import pandas as pd
import string 
import random

details = pd.read_csv('order_details.csv')
prod = pd.read_csv('products.csv')
duplicateRowsDF = details[details.duplicated(['1','2'])]
index = duplicateRowsDF.index;
for idx in (index):
    pid = details.at[idx,'2']
    details.at[idx,'2'] = pid + 1
    details.at[idx,'3'] = prod.at[pid,'6']

duplicateRowsDF = details[details.duplicated(['1','2'])]
print("Duplicate Rows based on a single column are:", duplicateRowsDF, sep='\n')
details.to_csv('order_details.csv',index=False)