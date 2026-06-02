#sort method
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
