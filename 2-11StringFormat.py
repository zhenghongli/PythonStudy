#Stringformet
print("{0}{1}".format('test',1))
print("{age}{name}".format(age=20,name="Danny"))

list1=["a","b","c","d"]
print("{0[1]},{0[2]}".format(list1))


print("{}{}{}".format("Python","aaa","bbb"))


"""
list2={{"id": 3, "name": "john"}, {"id": 2, "name": "brandon"}}
print(list2)
print("{0[id]}{{0[name]}".format(**list2))
"""
#利用locals()撈取當前有效範圍中的變數
def aa():
    a=2
    b="aa"
    print("{a}{b}".format(**locals()))  
aa()

str1="Never, never, never, never give up."
print("{0:-^60}".format(str1))
num1=12345678987654321
print("{0:*>20}".format(num1,10))



#正負號控制
print("[{0: }][{1: }]".format(12345,-45678))
print("[{0:+}][{1:+}]".format(12345,-45678))
print("[{0:-}][{1:-}]".format(12345,-45678))