def calculator(num1, num2):
    if user_input == "+":
        result = num1 + num2
    if user_input == "-":
       result = num1 - num2    
    if user_input == "*":
        result = num1 * num2
    if user_input == "/":
        result = num1 / num2
    return result


while True:
    try:
        num1 = int(input("num1 = "))  
        num2 = int(input("num2 = "))  
        while True:
            user_input = input("Choose operator `(+,-,*,/): ")
            if user_input == "+" or user_input == "-" or user_input == "*" or user_input == "/":
                break
            else:
                print("you can only import` (+,-,*,/): ")
        print(calculator(num1,num2))
    except( ZeroDivisionError,ValueError,TypeError) as e:
        print(e)
    finally:
        answer = input("do you want to continue? yes/no : ")
        if answer == "no":
            break