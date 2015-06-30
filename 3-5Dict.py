d1=dict({"id":1,"name":"danny"})
print(d1.keys())

print(d1.get("id"))
print(d1.get("ids","沒找到"))
print(d1.items())
print(d1)
d1.pop("id")
print(d1)
print(d1.pop("name","No"))
print(d1)


d1={}.fromkeys("ABCD",3)
print(d1)
d2={}.fromkeys("ABRT",3)
print(d2)
print(dict(d1,**d2))
