def say_hello(name):
    print("Hello,"+name+"!")

say_hello('sun')

# 关键字实参
def describe_pet(animal_type, pet_name):
    print("I have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")

describe_pet(pet_name='harry', animal_type='hamster')