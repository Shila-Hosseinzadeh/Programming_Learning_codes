
# access tuples
mytuple = ( "a", "b", "c", "d")
print (mytuple[0])
print(mytuple[-1])
print(mytuple[-2])

# slice range
print(mytuple[1:4])
print(mytuple[:])
print(mytuple[:-1])
print(mytuple[-4:-1])
print(mytuple[0:])

# in
print("v" in mytuple)
print("a" in mytuple)
print("4" in mytuple)

# Update Tuples
## tuple to list
mylist = list(mytuple)
print(mylist)
mylist.append("BBB")
print(mylist)
mynewtuple = tuple (mylist)
print(mynewtuple)
print(mytuple)

## tuple + tuple
print(mytuple + mynewtuple)
y=("333", )
mytuple += y
print(mytuple)

## remove()
mytuple = ( "a", "b", "c", "d")
mylist = list(mytuple)

mylist.remove("a")
print(mylist)
mynewtuple = tuple (mylist)
print(mynewtuple)


## delet tuple
mynewtuple =('a', 'b', 'c', 'd', '333')
print(f" mynewtuple before delet : {mynewtuple}")

del mynewtuple
print(f" mynewtuple after delet : \n name 'mynewtuple' is not defined.")
print(mynewtuple)


# unpack tuples
mytuple =('a', 'b', 'c', 'd', "e", "f")
print(mytuple)
(q, w, z,r,m,n) = mytuple
print(q)
print(n)

# unpack tuples *
mytuple =('a', 'b', 'c', 'd', "e", "f")
print(mytuple)
(q, *w,n) = mytuple
print(q)
print(w)
print(n)
print(type(w))
print(type(n))



