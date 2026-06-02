# Tuple Methods
# tuples are immutable .doesn't change. have 2 methods: index() , count()

#index()

mytuple=("a","b","c","d","f",",f","a","b" ,"c","c","d")
x = input(" please inter x : ")
if x in mytuple:
    print(f" {x} exists in  first position of  {mytuple.index(x)}.")
    
else:
    print(f" {x}  doesn't exist in this tuple.")


#count() & Index()
# count ()

i = 0
while i < 10:

    x = input(" please inter x : ")
    if x in mytuple:
        if mytuple.count(x) > 0:
        print (f"{x} exists  {mytuple.count(x)} times in first position of {mytuple.index(x)}. ")
        break
    else :
        print(f" chance {i+1} : {x}  doesn't exist in this tuple.")
        if i+1 < 10:
           print(f" you have { 9 - i} chance inter another word :")
        else :
            print (f" { i+1 } !!!! Time is Over !!! ")
    i+=1
