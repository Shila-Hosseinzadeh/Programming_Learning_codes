#in 10 repeat guess the word in tuple:
i = 0
while i < 10:

    x = input(" please inter x : ")
    if x in mytuple:
        print (f"{x} exist in {mytuple}.in  {i+1} level you guessed the word!!! You Won!!!! . Game finished")
        break
    else :
        print(f"chance {i+1} : {x}  doesn't exist in this tuple.")
        if i+1 < 10:
           print(f" you have { 9 - i} chance inter another word :")
        else :
            print (f" { i+1 } !!!! Game is Over !!! ")
    i+=1
