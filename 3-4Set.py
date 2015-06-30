a={'a','b','c'}
b={'d','b','c'}
print(a&b)       #聯集  
print(a|b)       #交集  
print(a-b)       #差集  
print(a^b)       #對稱集
a.add('d')
print(a)
a.discard('a')
#a.remove('a')    #會觸發KeyError
print(a)
a.pop()
print(a)
c=frozenset({'d','e','f'})
print(c)
#print(c.pop())