
#Str.join();
Arytxt=["apple","banana","papaya"]
print("-".join(Arytxt))             #字串合併
s="ABCDEFGHGFE"
print("".join(reversed(s)))         #倒序




#index引數（str,start,end）
#print(s.index('L'))                #查找不到會觸發ValueError
try:
   print(s.index('B'))
   print(s.index('L'))              #如果無查找到則會觸發ValueError
except ValueError:
   print("找不到")

#count,find,rfind,
print('Search B',s.find('B'))       #從左邊開始查找Ｂ的出現位置
print('Search L',s.find('L'))       #從左邊開始查找Ｌ的出現位置　沒查找到則回傳-１
print('Search B',s.rfind('B'))      #從右邊開始查找Ｂ的出現位置
print('Search P',s.rfind('P'))      #從右邊開始查找Ｐ的出現位置　沒查找到則回傳-１
print('Search G',s.count('G'))      #回傳Ｇ在字串裡出現的次數


#endswith,startswith
str1='Stay hungry. Stay foolish.'   
print(str1.endswith('.'))           #該字串最後一個字是否為．
print(str1.endswith('foolish'))     #該字串最後一個字是否為foolish
print(str1.startswith('S'))         #該字串第一個字是否為S
print(str1.startswith('s'))         #該字串第一個字是否為s
      


#capitalize,title,lower
str='adMiNIstRator'
print(str.capitalize())             #轉Title
print(str.title())                  #轉Title
print(str.lower())                  #字串轉小寫                    
print(str.swapcase())               #大寫轉小寫　小寫轉大寫


#split,rsplit,partition,rpartition
Str2='Never, never, never, never give up.'
print(Str2.split(' '))               #分割字串
print(Str2.rsplit('er'))              #由右分割字串
print(Str2.partition('er'))           #找尋到指定的字串後以他為基準將字串打散成三部份
print(Str2.rpartition('er'))          #由右找尋到指定的字串後以他為基準將字串打散成三部份


#replace(str,onstr,count)
Str3='You’ve got to find what you love,'
print(Str3.replace('o','u',3))


