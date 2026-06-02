#frozensets

# not editable, can't add or remove member ,unique , not in order ,immutable
# is suitable for keys of dictionary
s1 = frozenset {1,2,3,4}
print(s1)

# copy()  of frozensets : if delet s1 , s2 has not been removed
s2 = s1.copy()
print(s2)

# union() of frozensets === | or : operator 
s1 = frozenset {1,2,3,4}
s2 =frozenset{1,2,3,5,7,8}
s3 = s1 .union(s2)
print(s3)

# intersection() of frozensets === & : and operator 
s1 = frozenset {1,2,3,4}
s2 =frozenset{1,2,3,5,7,8}
s3 = s1 .intersection(s2)
print(s3)

# difference() of frozensets === s1 - s2 === members of only s1
s1 = frozenset {1,2,3,4}
s2 =frozenset{1,2,3,5,7,8}
s3 = s1 .difference(s2)
print(s3)

# symmetric_difference() of frozensets === s1 ^ s2 === non-shared members of all sets
s1 = frozenset {1,2,3,4}
s2 =frozenset{1,2,3,5,7,8}
s3 = s1 .symmetric_difference(s2)
print(s3)

# issubset() , issuperset()  === all of s2 members is in s1: s1 is superst , s2 is subset
s1 =frozenset{1,2,3,4,5,6}
s2 =frozenset {2,3,5}
print(s1.issuperset(s2))
print(s2.issubset(s1))

# isdisjoint() === s1 and s2 doesn't have any shared member
s1 =frozenset{1,4,6,7,8,9,0}
s2 =frozenset {2,3,5}
print(s1.isdisjoint(s2))
print(s2.isdisjoint(s1))

