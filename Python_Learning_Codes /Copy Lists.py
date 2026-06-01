
# Reference Lists

my_list6 = ["a", "b", "c", "d", "e", "A", "B", "R", "h"]
my_list7 = ["a", "b", "c", "d", "e", "A", "B"]
print("\n")

print(f" my_list6: {my_list6}")
print(f" my_list7: {my_list7}")
print("\n")
my_list7 = my_list6
print("\n")
print( f" if my_list7 = my_list6: my_list6 = {my_list6})")
print( f" if my_list7 = my_list6: my_list7 = {my_list7})")

print("\n")
my_list6.append("abcdef")
print("\n")
print(f" if my_list6.append(\" abcdef \"): my_list6 = {my_list6}")
print(f" if my_list6.append(\"abcdef\"): my_list7 = {my_list7})")
print("\"abcdef\" is added to my_list6 & my_list7")
print("result : my_list6 & my_list7 are in the same reference")
print("\n")
print("---------------------------------------------------------------------------------")
print("\n")
# copy lists
my_list6 = ["a", "b", "c", "d", "e", "A", "B", "R", "h"]
my_list7 = ["a", "b", "c", "d", "e", "A", "B"]
print("\n")
print(f" my_list6: {my_list6}")
print(f" my_list7: {my_list7}")
print("\n")
my_list7 = my_list6.copy()  # or : my_list7 =list (my_list6)
print("\n")
print("for copy list6 : \n copy() : my_list7 = my_list6.copy() \n list() : my_list7 = list (my_list6)\n slice[]: mylist7 = mylist6[:]")
print("\n")
print(f" if my_list7 = my_list6.copy(): my_list6={my_list6})")
print(f" if my_list7 = my_list6.copy(): my_list7= {my_list7})")
print("\n")
my_list6.append("abcdef")
print("\n")
print(f" if my_list6.append(\"abcdef\"): mylist6 = {my_list6}")
print(f" if my_list6.append(\"abcdef\"): my_list7 = {my_list7})")
print("\"abcdef\" is added to my_list6 not my_list7")
print("result : my_list6 & my_list7 are not in the same reference")
