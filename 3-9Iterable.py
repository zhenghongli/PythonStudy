x=[1,3,4]
y=[2,3,6,0]
print(x + y)
print(2 * y)
print(max(x))
print(min(y))
print(sum(x))
print(x in y)
print(any(x))
print(all(y))

print(all([any([1,2,3]),0,1,4]))

#打散 列舉
e = enumerate('abcdefgh')
a=list(e)
print (a)

#打包 合併
z=zip(x,y)
print(z)
w=zip(*z)
print(w)

name=["danny","Eric","Tina"]
idd=[1,3,6]
student=zip(idd,name)
print(student)

L1=[62,22,11,["A","B"]]
L2=L1[:]
print(L2)