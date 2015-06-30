import collections
Aatest=collections.namedtuple("Aatest","aaaa bbbb cccc")
Seating=collections.namedtuple("Seating","dddd eeee")
aatest=Aatest("Abus","AAA",Seating(100,220))
print(aatest.cccc.eeee)
"""
print
sales=[]
sales.append(sale(99,22,"22"))
sales.append(sale(11,44,"21"))
print (sales[0][-1])
"""