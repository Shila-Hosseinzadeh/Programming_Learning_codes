
# in sets members don't change (not immutable) only  can add and remove items in sets not in order

# Add Set Items with add()

myset = {"a", "b", "c", "d","e","f" }
print (f"myset :{myset}")
myset.add(1)
print (f"myset.added (1) :{myset}")

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
myset = {"a", "b", "c", "d","e","f" }
print (f"myset :{myset}")
myset.add("e")
print (f"myset.added (e) :{myset}")

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
myset = {"a", "b", "c", "d","e","f" }
print (f"myset :{myset}")
myset.add(2)
print (f"myset.added (2) :{myset}")

myset.add(5)
print (f"myset.added (2,5) :{myset}")

# add set to set with update() :not in order and has unique members not repeated members

myset = set(("a", "b", "c", "d","e","f",True , False ,1 ,0 ))
myset1 = {"a", "b", "c", "d","e","f" }
print (f"myset1 :{myset1}")
print (f"myset :{myset}")
myset.update(myset1)
print (f"myset + myset1 : updated myset = {myset}")
print("******************************************____________________________________")
"""
add any iterable to set with update() 
"""
#  add any iterable to set with update() :not in order and has unique members not repeated members

myset = {"a", "b", "c", "d","e","f" }
print (f"myset :{myset}")

mylist = [1,3,4,5,6,2,3,0,1]
myset1 = (11,1,2,"ab","ac","ad",True ,False ,00,91)
print (f"mylist :{mylist}")
print (f"myset1 :{myset1}")

myset.update(mylist ,myset1 )
print (f"myset +  mylist + myset1  :updated myset = {myset}")

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

myset = {"a", "b", "c", "d","e","f" }
print (f"myset :{myset}")

mylist = [1,3,4,5,6,2,3,0,1]
myset1 = (11,1,2,"ab","ac","ad",True ,False ,00,91)
print (f"mylist :{mylist}")
print (f"myset1 :{myset1}")

myset.update(myset1 , mylist )
print (f"myset + myset1  + mylist : updated myset = {myset}")

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
myset = {"a", "b", "c", "d","e","f" }
print (f"myset :{myset}")

mylist = [1,3,4,5,6,2,3,0,1,True,False]
myset1 = (11,1,2,"ab","ac","ad",True ,False ,00,91)
mylist2 = ["q"]
mydict ={"aaaaaaaaaaa":5666}
print (f"mylist :{mylist}")
print (f"myset1 :{myset1}")
print (f"mylist2 :{mylist2}")
print(f"mydict:{mydict}") # in dictionary updete() only adds keys

"""
in dictionary only adds keys
"""
myset.update(mylist ,myset1  , mylist2 ,mydict)
print (f"myset +  mylist + myset1 + mylist2 + mydict : updated myset = {myset}")
