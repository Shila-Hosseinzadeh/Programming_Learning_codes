# single
## super class

class Father():
    # attributes
    def __init__(self):
        self.family = "pedrami"
        self.hair_color = "black"

    # methods
    def behave(self):
        print("He works hard.")
        print("He is so nice.")


## sub class
class Doghter(Father):
    # if we write def for Doghter : this code does'nt work :
    # def __init__(self):
    # self.name ="shila"
    # doghter = Doghter()
    # print (f" Doghter's Family is {doghter.family},and her haircolor is {doghter.haircolor}")
    # doghter.behave()
    def __init__(self):
        super().__init__()
        self.name = "shila"
        self.hair_color = "red"

    def behave2(self):
        print("doghter's behavior")
        super().behave()


doghter = Doghter()
print(f" Doghter's Family is {doghter.family}\
, and her haircolor is {doghter.hair_color} ,doghter's name ie {doghter.name}")
doghter.behave()
doghter.behave2()

print("________________________________________________________________")


# multiple


class Father:
    # attributes
    def __init__(self):
        self.family = "pedrami"
        self.hair_color = "black"

    # methods
    def behave(self):
        print("He works hard.")
        print("He is so nice.")


class Mother:

    # attributes

    def __init__(self):
        self.family = "Medrami"
        self.hair_color = "brown"

    # methods
    def behave2(self):
        print("Mother listens to music.")
        print("Mother exercises")


class Doghter( Mother, Father):
    def __init__(self):
        super().__init__()
        self.family = "her family"
        self.name = "Shiva"

    def behave2(self):
        super().__init__()
        print("only her behave3")


doghter = Doghter()
print(f"Doghter's Family is {doghter.family}, and her haircolor is {doghter.hair_color} \
,doghter's name is {doghter.name}")

doghter.behave2()


print("_____________________________________________________________________________")


# multilevel

class GrandFather():
    # attributes
    def __init__(self):
        self.family = "Gedrami"
        self.hair_color = "white"

    # methods
    def behave(self):
        print("He listens radio.")
        print("He reads book.")

class Father (GrandFather):
    # attributes

    def __init__(self):
        super().__init__()
        self.family = "Pedrami"
        self.hair_color = "black"

    # methods

    def behave2(self):
        print("He works hard.")
        print("He is so nice.")



class Doghter(Father):
    def __init__(self):
        self.family = "Dedrami"
        self.name = "Shina"
        self.hair_color ="blue"


#object

doghter = Doghter()
print(f"Doghter's Family is {doghter.family}, and her haircolor is {doghter.hair_color} \
,doghter's name is {doghter.name}")

doghter.behave()
doghter.behave2()
