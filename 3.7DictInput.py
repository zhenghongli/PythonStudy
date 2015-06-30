def FileOW(num,txt):
    fin =open("dict.txt",'r')
    temp=fin.read()
    d1=dict({"id":num,"name":txt})
    fin =open("dict.txt",'w')
    writetxt=temp+str(d1)+'\n'
     
    fin.write(writetxt)
    fin =open("dict.txt",'r')    
    print(fin.read())


while True:
    try:    
        inputnum=raw_input("輸入學生學號：")
        inputtxt=raw_input("輸入學生姓名：")
        FileOW(inputnum,inputtxt)
    except ValueError:
        print("Error")