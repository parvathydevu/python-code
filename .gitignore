'''
    Jumbled Word: "otpcomure"
    Your Guess: "computer"
    ✅ Correct! 

'''

import random

# function to jumble the word

def jumble(w):
    temp = list(w)
    random.shuffle(temp)
    return ''.join(temp)


# Welcome message

print("\n")
print("Welcome to the WORD JUMBLE GAME")
print("-" * 80)

print("The computer presents a jumbled word")
print("You need to guess it. For every correct guess")
print("you will be offered a point")
print("-" * 80)

# Get the words and process it 
f = open("words.txt")
content = f.read()
f.close()

content = content.split(',')

# print("INFO content -> ", content)

points = 0

# for every word in list of words
random.shuffle(content)

for word in content:

    print("\n")

    # jumble the word
    jumbled_word = jumble(word)

    # show to the user
    print(jumbled_word)

    # ask user input
    user_word = input("Can you guess -> ")

    # compare user input and update points
    if(user_word == word):
        points += 1
        print("\U00002705 Correct")
    else:
        print("\U00002745 In-correct")

    

# show the results

print("-" * 80)

if(points > 6):
    print("You have played well")
else:
    print("You need to improve on your vocabulary")