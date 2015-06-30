text="Hello People"
try:
    print(text[-12])
    print(text[0])
    print(text[0:2])
    print(text[::2])       #每兩個字元提取一次　
    print(text[13])
    print(text[11])
except IndexError:
    print "溢位了"