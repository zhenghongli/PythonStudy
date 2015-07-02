
while True:
    

    try:
        a=input("Input Num:")
        str(a)
        print(a+1)
    except NameError:
        print("Error")
    
    else:
        print("OK")
    finally:
        print("finally")



#https://docs.python.org/2/library/exceptions.html