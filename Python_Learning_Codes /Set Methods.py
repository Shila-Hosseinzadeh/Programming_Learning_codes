# add() , clear() , copy
s1 = {"a","b" ,"c"}
s2 = s1.copy()
s2.add("d")
print(s1)
print (s2)
# sets are not in order and members are unique

# difference() difference_update() , - , =-

a={1,2,3,4,5}
b={1,2,4,5,6,7}
only_a = a.difference(b)
print(only_a)
a.difference_update(b)
print(a)

# remove() with error ,without error discard()

# intersection() , intersection_update() , & , =&
# issubset() ,issuperset() , isdisjoint()
# pop() delet member random from sets ,remove() delets decided member from sets
# symmetric_difference() ,symmetric_difference_update() ,^ ,=^
# update() ,union() , | , =|
