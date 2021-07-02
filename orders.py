import random
import time
import numpy as np
import pandas as pd
import string 
import datetime

def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y-%m-%d', prop)


cust = pd.read_csv('customers.csv')
# a = (random_date("2008-1-1", "2009-1-1", random.random()))
# date_1 = datetime.datetime.strptime(a, "%Y-%m-%d")
# end_date = date_1 + datetime.timedelta(days=10)
# print(date_1.date())
# print(end_date.date())

total = []
a = "1980-1-1"
date = datetime.datetime.strptime(a, "%Y-%m-%d")
order_date = date + datetime.timedelta(days=0)
for i in range (1,250000,1):
    if (i % 30 == 0):
        order_date = order_date + datetime.timedelta(days=random.randint(1,3))
    req_date = order_date + datetime.timedelta(days=random.randint(5,20))
    shipped_date = order_date + datetime.timedelta(days=random.randint(3,25))
    custidx = random.randint(1,6000)
    new_row = [i, cust.at[custidx-1,'1'] ,random.randint(1,9),order_date.date(),req_date.date(),shipped_date.date(),random.randint(1,6),random.randint(1,150),cust.at[custidx-1,'2'],cust.at[custidx-1,'5'],cust.at[custidx-1,'6'],cust.at[custidx-1,'7'],cust.at[custidx-1,'8'],cust.at[custidx-1,'9']]
    total.append(new_row)
df = pd.DataFrame(total)
df.to_csv('orders.csv',index=False)