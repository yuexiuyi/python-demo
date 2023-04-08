class Car():
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def drive(self):
        print("The {} car is driving".format(self.color))

    def stop(self):
        print("The {} car is stopped".format(self.color))