# Join Sets
# union()
set1 = {1,2,3,4,5}
set2 = {"a","b","c",1,3}
set11 = {1,2,3,4,5,33,"G","d"}
set12 = {"a","b","c",1,3,"E",22,45}
set3 = set1.union(set2,set11,set12)
print(f"set1.union(set2,set11,set12,...) ---> set3 ={set3}")

# |
set4 = set1 | set1 |set11 |set12
print(f"set1 | set2 |se11 |set12 ---> set4 = {set4}")

# set.union(tuple) ---> set
list1 = ["a","s","r"]
set5=set1.union(list1)
set5 = set1.union(list1)

# | or is only for sets for join other  sets use union()
# update() adds set2 members th set1
set1 = {1,2,3,4,5}
set2 = {"a","b","c",1,3}
set1.update(set2)
print(set1)

# union() & update() removes repeated members.



# intersection() , set1 & set2 === shared members of set1 & set2
set1 = {1,2,3,4,5}
set2 = {"a","b","c",1,3}
set3=set1.intersection(set2) === set3 = set1 & set2 === se1.intersection_update(set2)
print(set3)


# difference() ,  set1 - set2 === non-shared members of set1
set1 = {1,2,3,4,5}
set2 = {"a","b","c",1,3}
set3=set1.difference(set2) == set3 = set1 - set2 === se1.difference_update(set2)
print(set3)

# symmetric_difference() ,  set1 ^ set2  === non-shared members of set1 & set2
set1 = {1,2,3,4,5}
set2 = {"a","b","c",1,3}
set3=set1.symmetric_difference(set2) === set3 = set1 ^ set2 
print(set3)
