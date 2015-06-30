x=10
print(bin(x))           #轉二進制
print(oct(x))           #轉八進制
print(int('20'))        #字串轉十進制
print(hex(x))           #轉十六進制
print(int('30',16))     #將字串轉成指定進制


try:
    print(int('30',2))     #將字串轉成指定進制
except ValueError:
    print('數值錯誤')