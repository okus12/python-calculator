print(""" Welcome To Calculator!
      [1] addition
      [2] subtraction
      [3] multiplication
      [4] division
      [5] exponentiantion
      [Q] Exit """)

choice=input("Enter your choice: ")
if choice=="1":
    num1=float(input("Enter your first number: "))
    num2=float(input("Enter your second number: "))
    print("The result is:",format(num1+num2))
elif choice=="2":
    num1=float(input("Enter your first number: "))
    num2=float(input("Enter your second number: "))
    print("The result is:",format(num1-num2))
elif choice=="3":
    num1=float(input("Enter your first number: "))
    num2=float(input("Enter your second number: "))
    print("The result is:",format(num1*num2))
elif choice=="4":
    num1=float(input("Enter your first number: "))
    num2=float(input("Enter your second number: "))
    print("The result is:",format(num1/num2))
elif choice=="5":
    num1=float(input("Enter your first number: "))
    num2=float(input("Enter your second number: "))
    print("The result is:",format(num1**num2))
elif choice=="Q" or choice=="q":
    print("Exiting The Calculator. Godbye!")
else:
    print("invalid choice,please try again.")
