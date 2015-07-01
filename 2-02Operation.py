x=5
y=3
w=4
z=-4
#字串

print('%d+%d=%d')%(x,y,x+y)
print('%d-%d=%d')%(x,y,x-y)
print('%d*%d=%d')%(x,y,x*y)
print('%d/%d=%d')%(x,y,x/y)
print('%d//%d=%d(四捨五入捨去後的整數)')%(x,y,x//y)
print('%d%%%d=%d(取餘數)')%(x,y,x%y)
print('%d**%d=%d(平方)')%(x,y,x**y)
print('%d**%d=%d(平方)')%(x,y,pow(x,y))
print('%d**%d=%d(平方後取餘數)')%(x,y,pow(x,y,w))
print('%d')%(-x)
print('%d')%(+x)
print('%d(絕對值)')%(abs(z))
print('商%d餘%d')%(divmod(x,y))
print('四捨五入第一位%f'%round(1.6666,1))

