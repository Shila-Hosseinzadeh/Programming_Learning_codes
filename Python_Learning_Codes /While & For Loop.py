# print until banana

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple']
print(fruits.index("banana"))

# while_loop
i = 0
while i < fruits.index("banana"):
    print(fruits[i])
    i = i + 1
# for_loop
for i in range(fruits.index("banana")):
    print(fruits[i])
