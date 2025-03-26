'''Design a simple calculator which has the following functionality:
   add, sub, mul, div, mod, sqrt, log'''
import math

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Square Root")
print("7. Logarithm")

choice = input("Enter your choice (1/2/3/4/5/6/7): ")

if choice in ['1', '2', '3', '4', '5']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = num1 + num2
        print('%f + %f = %f' % (num1, num2, result))
    elif choice == '2':
        result = abs((num1) - (num2))
        print('%f - %f = %f' % (num1, num2, result))
    elif choice == '3':
        result = num1 * num2
        print('%f * %f = %f' % (num1, num2, result))
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print('%f / %f = %f' % (num1, num2, result))
        else:
            print("Error! Division by zero.")
    elif choice == '5':
        result = num1 % num2
        print('%f %% %f = %f' % (num1, num2, result))

elif choice == '6':
    num = float(input("Enter a number: "))
    result = math.sqrt(num)
    print('Square root of %f = %f' % (num,result))

elif choice == '7':
    num = float(input("Enter a number: "))
    result = math.log(num)
    print('Logarithm of %f = %f' % (num,result))

else:
    print("Invalid input")