

# Remove Set Items
# remove() if value doesn't exist in set we have error.
myset = {"a", "b", "c", "d","e","f" }
print (f"myset :{myset}")


myset.remove("a")
print (f"myset :{myset}")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


# discard() if value doesn't exist in set we don't have error.
myset = {"a", "b", "c", "d","e","f" }
print (f"myset :{myset}")


myset.discard("a")
print (f"myset :{myset}")

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# pop() deletes random a value
myset = {"a", "b", "c", "d","e","f" }
print (f"myset :{myset}")


myset.pop()
print(f'poped item :{myset.pop()}')
print (f"myset :{myset}")

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


# clear() clears set and delets all items
myset = {"a", "b", "c", "d","e","f" }
print (f"myset :{myset}")


myset.clear()

print (f"myset :{myset}")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


# del  :deletes set
myset = {"a", "b", "c", "d","e","f" }
print (f"myset :{myset}")

del myset
#print (f"myset :{myset}") # have error after del :NameError: name 'myset' is not defined

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


