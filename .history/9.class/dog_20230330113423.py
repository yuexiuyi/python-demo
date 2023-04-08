class Dog():
    def __init__(self, name, age):
        self.name = name.title()
        self.age = age
    
    def sit(self):
        print(self.name + " is sitting.")

    def roll_over(self):
        print(self.name + " rolled over!")

my_dog = Dog('sun', 6)