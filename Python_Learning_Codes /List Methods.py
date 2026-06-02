
# list comprehension
num_list=[x for x in range(51)]
even_num =[x for x in range(51) if x % 2 == 0]
squared_num = [x**2 for x in range(51)]
print(f"num_list of 0 <= num <= 50 : {num_list} ")
print(f"even_num of 0 <= num <= 50 : {even_num} ")
print(f"squared_num of 0 <= num <= 50 : {squared_num} ")

# sort lists
my_list1 = ["a", "b", "c", "d", "e", "A", "B"]
my_list2 = [1, 2, 45, 78, 345, 678, 90]
my_list1.sort()
my_list2.sort()

my_list3 = ["s", "m", "cV", "r", "e", "A", "B"]
my_list4 = [178, 25, 405, 784, 345, 6, 90]
my_list3.sort(reverse=True)
my_list4.sort(reverse=True)

def my_func(x):
    return abs(x - 10)

my_list5 = [abs(x - 10) for x in my_list2]
my_list4.sort(key=my_func)

print(f' my_list1: ["a", "b", "c", "d", "e", "A", "B"]')
print(f" my_list1.sort(): {my_list1}")

print(f" my_list2: [1, 2, 45, 78, 345, 678, 90]")
print(f" my_list2.sort(): {my_list2}")

print(f' my_list3: ["s", "m", "cV", "r", "e", "A", "B"]')
print(f" my_list3.sort(): {my_list3}")

print(f' my_list4: [178, 25, 405, 784, 345, 6, 90]')
print(f" my_list4.sort(): {my_list4}")

print(f' my_list5: {my_list5}')
print(f" my_list4.sort(key=my_func) {my_list4}")

# Reference Lists

my_list6 = ["a", "b", "c", "d", "e", "A", "B", "R", "h"]
my_list7 = ["a", "b", "c", "d", "e", "A", "B"]

print(f" my_list6: {my_list6}")
print(f" my_list7: {my_list7}")

my_list7 = my_list6

print( f" if my_list7 = my_list6: my_list6 = {my_list6})")
print( f" if my_list7 = my_list6: my_list7 = {my_list7})")

my_list6.append("abcdef")

print(f" if my_list6.append(\" abcdef \"): my_list6 = {my_list6}")
print(f" if my_list6.append(\"abcdef\"): my_list7 = {my_list7})")
print("\"abcdef\" is added to my_list6 & my_list7")
print("result : my_list6 & my_list7 are in the same reference")

print("---------------------------------------------------------------------------------")

# copy lists
my_list6 = ["a", "b", "c", "d", "e", "A", "B", "R", "h"]
my_list7 = ["a", "b", "c", "d", "e", "A", "B"]
print(f" my_list6: {my_list6}")
print(f" my_list7: {my_list7}")

my_list7 = my_list6.copy()  # or : my_list7 =list (my_list6)

print("for copy list6 : \n copy() : my_list7 = my_list6.copy() \n list() : my_list7 = list (my_list6)\n slice[]: mylist7 = mylist6[:]")

print(f" if my_list7 = my_list6.copy(): my_list6={my_list6})")
print(f" if my_list7 = my_list6.copy(): my_list7= {my_list7})")
my_list6.append("abcdef")
print(f" if my_list6.append(\"abcdef\"): mylist6 = {my_list6}")
print(f" if my_list6.append(\"abcdef\"): my_list7 = {my_list7})")
print("\"abcdef\" is added to my_list6 not my_list7")
print("result : my_list6 & my_list7 are not in the same reference")
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

print(f"list2 +list2 : {[*list1 , *list2]}")
print(f"[x for x in [*list1 , *list2]]: {[x for x in [*list1 , *list2]]} ")

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# append()

list1 = [ 1,2,3,4,5]
list2 = [11,12,13,14,15]
print(f"list1 : {list1}")
print(f"list2 : {list2}")

list1.append(25)
print(f"list1.append(25) : {list1}")

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# clear

list1 = [ 1,2,3,4,5]
list2 = [11,12,13,14,15]
print(f"list1 : {list1}")
print(f"list2 : {list2}")
list1.clear()
print(f"list1.clear() : {list1}")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# copy

list1 = [ 1,2,3,4,5]
list2 = [11,12,13,14,15]
print(f"list1 : {list1}")
print(f"list2 : {list2}")
list1.copy()
print(f"list1.copy() : {list1}")

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# count()

list1 = [ 1,2,3,4,5]
list2 = [11,12,13,14,15]
print(f"list1 : {list1}")
print(f"list2 : {list2}")

print(f"list1.count(11) : {list1.count(11)}")
print(f"list2.count(11) : {list2.count(11)}")

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# index()

list1 = [ 1,2,3,4,5]
list2 = [11,12,13,14,15]
print(f"list1 : {list1}")
print(f"list2 : {list2}")

print(f"list1.index(1) : {list1.index(1)}")
print(f"list2.index(13) : {list2.index(13)}")

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# insert()

list1 = [ 1,2,3,4,5]
list2 = [11,12,13,14,15]
print(f"list1 : {list1}")
print(f"list2 : {list2}")
list1.insert(11,3)
list2.insert(3,1)
print(f"list1.insert(11 ,3): {list1}")
print(f"list2.insert(3 ,1): {list2}")

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# pop()

list1 = [ 1,2,3,4,5]
list2 = [11,12,13,14,15]
print(f"list1 : {list1}")
print(f"list2 : {list2}")


print(f"list1.pop(3): {list1.pop(3)}")
print(f"list2.pop(0): {list2.pop(0)}")
print(f"list1 : {list1}")
print(f"list2 : {list2}")

print(f"list1.pop(): {list1.pop()}")
print(f"list2.pop(): {list2.pop()}")
print(f"list1 : {list1}")
print(f"list2 : {list2}")

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# reverse()

list1 = [ 1,2,3,4,5]
list2 = [11,12,13,14,15]
print(f"list1 : {list1}")
print(f"list2 : {list2}")
list1.reverse()
list2.reverse()
print(f"list1.reverse(): {list1}")
print(f"list2.reverse(): {list2}")

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# remove()

list1 = [ 1,2,3,4,5]
list2 = [11,12,13,14,15]
print(f"list1 : {list1}")
print(f"list2 : {list2}")

list1.remove(2)
list2.remove(14)
print(f"list1.remove(2): {list1}")
print(f"list2.remove(14): {list2}")

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# sort()

list1 = [ 234,1,4,5,6,0,45,6,78]
list2 = [1,5,23,0,9,123]
print(f"list1 : {list1}")
print(f"list2 : {list2}")

list1.sort()
list2.sort()
print(f"list1.sort(): {list1}")
print(f"list2.sort(): {list2}")

list1.sort(reverse=True)
list2.sort(reverse =True)
print(f"list1.sort(reverse=True): {list1}")
print(f"list2.sort(reverse=True): {list2}")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# extend()

list1 = [ 1,2,3,4,5]
list2 = [11,12,13,14,15]
print(f"list1 : {list1}")
print(f"list2 : {list2}")
list1.extend([110,150])
list2.extend ([1,4])
print(f"list1.extend([110,150]): {list1}")
print(f"list2.extend ([1,4]) : {list2}")
