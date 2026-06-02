print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# join lists
# list1 + list2
list1 = [ 1,2,3,4,5]
list2 = [11,12,13,14,15]

print(f"list1 : {list1}")
print(f"list2 : {list2}")

print(f"list1 + list2 : {list1 + list2}")
print(f"list2 + list1 : {list2 + list1}")
print(f"result :\n (list2 + list1 : {list2 + list1} ) != (list1 + list2 : {list1 + list2})")

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


#join lists with append
list1 = [ 1,2,3,4,5]
list2 = [11,12,13,14,15]

print(f"list1 : {list1}")
print(f"list2 : {list2}")

for i in list1:
    list2.append(i)
print(list2)

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


#join lists with extend
list1 = [ 1,2,3,4,5]
list2 = [11,12,13,14,15]
print(f"list1 : {list1}")
print(f"list2 : {list2}")

list1.extend(list2)
print(f"list1.extend(list2) : {list1}")

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

#join with *

list1 = [ 1,2,3,4,5]
list2 = [11,12,13,14,15]
print(f"list1 : {list1}")
print(f"list2 : {list2}")


print([x for x in [*list1 , *list2]]) #print(f"list2 +list2 : {[*list1 , *list2]}")

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
