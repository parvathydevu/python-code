import prime  #call that prime.py- user defined module is prime, it is an another code..
# Program to take user input and filter all prime numbers
# Also print the missing prime numbers in the range
import copy

# input
print("Enter your data: ")
userData = []
while True:
    userInput = input(" -> ")
    if(userInput == "!"):
        break
    else:
        if(userInput.isdigit()):
            userData.append(int(userInput))


# processing

minInput = min(userData)
maxInput = max(userData)
allPrimes = prime.getAllprime(minInput, maxInput + 1) # tuple (n, [])
userPrimes = []
for number in userData:
    if(prime.checkprime(number)):
        userPrimes.append(number)

userPrimes = list(set(userPrimes))
print("INFO: userPrimes -> ", userPrimes)

# Yeshwath
missing = list(copy.deepcopy(allPrimes))[1] # makes a proper copy
print("INFO: missingPrimes -> ", missing)
for item in userPrimes:
    missing.remove(item)

# Akshay
missingPrimes2 = [item for item in allPrimes[1] if item not in userPrimes]

# Purushotham
missingPrimes3 = set(userPrimes) ^ set(allPrimes[1])

missingPrimesCount = allPrimes[0] - len(userPrimes)

# output

print('-' * 80)
print(" Missing Primes Count : ", missingPrimesCount)
print(" Missing Primes       : ", missing)
print(" Missing Primes       : ", missingPrimes2)
print(" Missing Primes       : ", missingPrimes3)


'''
[19, 37, 47]

[11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

[11, 13, 17, 23, 29, 31,  41, 43]

'''