# sets doesn't have index and not in order
# make set with set() and set = {}
myset = set(("a", "b", "c", "d","e","f",True , False ,1 ,0 ))
myset1 = {"a", "b", "c", "d","e","f" }
print (f"myset1 :{myset1}")
print (f"myset :{myset}")


# delets repeated items
myset2 = {"a", "b", "c", "d","e","f","a", "b", "c", "d","e","f","a", "b", "c", "d","e","f","a", "b", "c", "d","e","f","a", "b", "c", "d","e","f" }
print(f"myset2 : {myset2}")

# True = 1 ,False = 0
myset3 = {"a", "b", "c", "d","e","f",True , False ,1 ,0 }
print (f"myset3 :{myset3}")

# sets shuffles the members in sets
myset5 = {"a", "b", "c", "d","e","f",True , False ,1 ,0 ,True ,1,0}
print (f'myset5 : {"a", "b", "c", "d","e","f",True , False ,1 ,0 ,True ,1,0}:{myset5}')


# len delets repeated members and then calculate the length :
myset7 = {"a", "b", "c", "d","e","f",True , False ,1 ,0 ,True ,1,0,1,0,2,3,0}

print (f'myset7 with  18  members : {"a", "b", "c", "d","e","f",True , False ,1 ,0 ,True ,1,0,1,0,2,3,0}  :\n afetr calculating length of set : has {len(myset7)} members')


# for deleting repeated members in list :
# transfer list to set and then to list


mylist1 = ["a", "b", "c", "d","e","f",True , False ,1 ,0 ,True ,1,0,1,0,2,3,0]
myset8 =set(mylist1)
print (f'transfered mylist1 =["a", "b", "c", "d","e","f",True , False ,1 ,0 ,True ,1,0,1,0,2,3,0] to myset8  :\n myset8 = {set(mylist1)} ')
print (f' transfered mylist1 =["a", "b", "c", "d","e","f",True , False ,1 ,0 ,True ,1,0,1,0,2,3,0] to mylist1 without repeated members  :\n mylist1 = {list(myset8)} ')

