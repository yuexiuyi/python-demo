# 使用异常避免崩溃
print("Give me equation, I'll calculate them")
print("Enter 'q' to quit")

while True:
      equation = input("\nGive me equation:")
      if(equation == 'q'):
        break


      if(operate == '/'):
        try:
          answer = int(first_number) /int(second_number)
        except ZeroDivisionError:
          print ("you can not divide by zero!")
      else:
        print(answer)
