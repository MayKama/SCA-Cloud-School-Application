num1 = float(input("enter first number, any number: "))

op = input("enter opertor: ")
num2 = float(input("enter second number, any number: "))

if op == "+" :
    print(num1 + num2)
    
elif op == "-":
    print(num1 - num2)
elif op == "*" :
    print (num1* num2)    

elif op == "/":
    print(num1/ num2)
    
else:
    print()
    print("INAVLID OPERATOR: PLEASE ENTER A VALID OPERATOR")       
    
