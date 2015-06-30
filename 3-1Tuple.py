tuple1="I","like","Python",3,4
print(tuple1.count(3))          #該物件在tuple中出現的次數
print(tuple1.index(3))          #該物件由左開始出現的位置
print(tuple1[3])                #由左置右第3個位置（有含0）
print(tuple1[-3])               #由右置左第3個位置
tuple2="I","like","Python"
print(tuple2[:1],"very",tuple2[1:])

tuple3=(tuple1,tuple2)
print(tuple3[1][1:-1])

import math
Shape=((-3,4),(5,12),(28,-45))
for x,y in Shape:
    print(math.hypot(x,y))