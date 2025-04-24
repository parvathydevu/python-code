#program to convert temperature from C to F and vice versa

'''1. Convert C to F
2. Convert F to C
3.Enter the Celcius value=100'''

#input

print("Temperature converison app\n")
print("1. Convert C to F")
print("2. Convert F to C")
choice=int(input("Your choice->"))

#process
if (choice ==1):
    temp=float(input("Enter a celcius value:"))
    res= temp*1.8+32
elif (choice ==2):
    temp=float(input("Enter a farenheit value:"))
    res=(temp-32)/1.8
else:
    print('Invalid')

#output
print("------------------------------------------")
print(res)