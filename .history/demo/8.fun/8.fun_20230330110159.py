# def say_hello(name):
#     print("Hello,"+name+"!")

# say_hello('sun')

# # 关键字实参
# def describe_pet(animal_type, pet_name):
#     print("I have a "+animal_type+".")
#     print("My "+animal_type+"'s name is "+pet_name.title()+".")

# describe_pet(pet_name='harry', animal_type='hamster')

# # 禁止函数修改列表
# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print("Printing model: "+current_design)
#         completed_models.append(current_design)
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs[:], completed_models)

# print(unprinted_designs)

# # 传递任意数量的实参
# def make_pizza(*toppings):
#     for topping in toppings:
#         print("- "+topping)
# make_pizza('pepperoni','mushrooms','green peppers')

# 传递任意数量的关键字实参
# def build_profile(first, last, **user_info):
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
# user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
# print(user_profile)

# # 导入整个模块
# import pizza as p
# p.make_pizza(16, 'pepperoni')

# # 导入特定的函数
# from pizza import make_pizza as mp
# mp(16, 'pepperoni')

# 导入特定的函数
from pizza import *
mp(16, 'pepperoni')
