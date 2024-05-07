class Human:
    population = 0
    data =[]
    def __init__(self,name,age,alive=True):
        self.name = name
        self.age = age
        self.alive = alive
        Human.population += 1
        Human.data.append(self.name)   # only we are giving or appending name
    def greet(self):
        print(f"Hey my name is {self.name}, Good morning")
    # adding more method
    def dead(self):
        if self.alive:
            print(f"{self.name} is no more...")
            Human.population -= 1
            Human.data.remove(self.name)
            self.alive = False
        else:
            print(f"{self.name} is already dead")
    def childBirth(self,number):
        Human.population += number

rahul = Human("Rahul",26)
anand = Human("Anand",20)