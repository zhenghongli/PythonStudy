
#這是副程式
def product(a,b,c):
    return a*b*c


L=[2,3,5]
try:
    print(product(*L))
except TypeError:
    print("型態錯誤 太長或太短了了")
    

print(L.pop())          #取出
print(L)                #列出
L.insert(1,4)           #插入(位置,值)
print(L)
L.sort()                #排序   
print(L)                
L.remove(2)             #刪除2這個值
print(L)
L.append(3)             #最後面插入3
print(L)
C=[1,2,8]
L.extend(C)             #List合併
print(L)
L.reverse()             #反轉List
print(L)        
print(L.count(3) )      #顯示3出現的次數
print(len(L))           #秀出陣列長度
del L[1:3]              #刪除1~3區間
print(L)
print(L[::2])
print(L[1::2])          #切片格式[開始：結束：隔幾片]
"""
for i in range(len(L)):
    print(L[i])
"""
L[1::2]=[0]*len(L[1::2])
print(L)
try:
    print(L.index(5))
except ValueError:
    print("找不到")
"""    
View=[x for x in range(1900,1940) if x%4==0]
print(View)
"""
"""
View2=[x*y for x in range(1,9) for y in range(1,9) ]
print(View2)
"""