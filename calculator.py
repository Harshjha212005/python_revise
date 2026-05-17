num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

operator = input("enter operator(+, -, *, /, **): ")
ans = 0
if operator == '+':
    ans = num1 + num2 
    print(ans)
elif operator == '-':
    ans = num1 - num2 
    print(ans)
elif operator == '*':
    ans = num1 * num2 
    print(ans)
elif operator == '/':
    ans = num1 / num2 
    print(ans)
elif operator == '**':
    ans = num1 ** num2 
    print(ans)
else:
    print("Enter valid opetator") 