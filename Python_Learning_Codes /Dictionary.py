#set of keys and values {key:value} , is ordered , doesn't have duplicate member

dic1 ={"a":1,"b":2 ,"c":3}
print(dic1[a]) #prints values of keys
print(type(dic1))
print(len(dic1))
# dic() method make dictionary
# access items
print(dic1["a"]) # if there isn't the key we have error
# get() if there is not key we don't have error, we have None
print(dic1.get("c"))
#keys() method is refference type
print(dic1.keys())
dic1["a"]=5
print(dic1.keys())
# values() method , is refference type
print9dic1.values())
# if we add one item to dic1 dictionary it is refference type
#items() method 
print(dic1.items()) # is refference type
# in 
if "a" in dic1:
  print(dic1["a"]) # print("a" in dic1)


# change dic1 items 
#[]
dic1["b"] = 5
print(dic1)
#update() for multy changes
dic1.update({"g":9,"f":0,"l":3,"r":12})


