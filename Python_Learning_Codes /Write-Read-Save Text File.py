# read text file in one position (same address)

text_file = open("text.txt", mode = "r") # read
mytext = text_file.read()
print(mytext)


# close text file

text_file.close()
mytext = text_file.read()
print(mytext)


# close simply automaticly
with open("text.txt" , mode="r") as text_file:
    text=text_file.read()
print(text)




# read text file in other project (another address)

text_file = open("E:/programming/python/projects/1/mytext.txt", mode = "r") # read
mytext = text_file.read()
print(mytext)



# write text file in one position (same address)

with open("textw.txt" , mode="w") as text_file:
    text=text_file.write("this is a new line in my text file\n")
    text=text_file.write("this is second line in my text file\n")
    text=text_file.write("this  is third line in my text file \n")


# write  previous text file (append)
with open("textw.txt" , mode="a") as text_file:
    text=text_file.write("this is append line in my text file\n")

with open("text.txt" , mode="a") as text_file:
    text=text_file.write("this is append line in my text file\n")


# readline
text_file = open("text.txt", mode = "r") # read
mytext = text_file.readline()
mytext = text_file.readline()

print(mytext)


# readlines

text_file = open("text.txt", mode = "r") # read
mytext = text_file.readlines()
print(mytext)

