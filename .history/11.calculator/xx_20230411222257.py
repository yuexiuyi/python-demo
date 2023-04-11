# 使用异常避免崩溃
print("Give me two numbers, and I'll divide them")
print("Enter 'q' to quit")

while True:
      first_number = input("\nFirst number:")
      if(first_number == 'q'):
        break
      second_number = input ("Second number:")
      if(first_number == 'q'):
        break
      try:
        answer = int(first_number) /int(second_number)
      except ZeroDivisionError:
        print ("you can not divide by zero!")
      else:
        print(answer)
