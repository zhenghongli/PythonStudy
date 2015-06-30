while True:
    inputtxt=raw_input("input")
    fin =open("read.txt",'r')
    temp=fin.read()
    
    fin =open("read.txt",'w')
    writetxt=temp+inputtxt
     
    fin.write(writetxt)
    fin =open("read.txt",'r')
    print(fin.read())


#input函數輸入的是一個純值