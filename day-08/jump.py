import random

# Function to jumble the word
def jumble(w):
    temp = list(w)
    random.shuffle(temp)
    return ''.join(temp)

path = r"C:\Users\237237\Desktop\anacondacode\day-08\word.txt"
with open(path) as f:
    content = f.read().split()  # Split the content into a list of words

print("Info content:", content)  # Complete string here, debug the result

points = 0  # Initialize points

# Shuffle the list of words
random.shuffle(content)

# For every word in the list of words
for word in content:
    jumbled_word = jumble(word)
    print("Jumbled word:", jumbled_word)
    user_word = input("Enter your answer: ").strip()
    if user_word == word:
        print("Correct!")
        points += 1
    else:
        print("Wrong! The correct word was:", word)

# Show the results
if points > 4:
    print("You have played well!")
else:
    print("Need to improve your vocabulary")