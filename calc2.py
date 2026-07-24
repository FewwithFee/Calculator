
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operator = input("Enter an operator (+, -, *, /): ")
if operator == "+":
    answer = first_number + second_number
    print("The answer is", round(answer, 2))

elif operator == "-":
    answer = first_number - second_number
    print("The answer is", round(answer,2))

elif operator == "*":
    answer = first_number * second_number
    print("The answer is", round(answer,2))

elif operator == "/":
    answer = first_number / second_number
    print("The answer is", round(answer,2))

else :
    print(f"{operator} is not a valid operator")


