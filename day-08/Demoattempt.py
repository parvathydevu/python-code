import random
# function to jumble the word

def jumble(w):
    temp = list(w)
    random.shuffle(temp)
    return ''.join(temp)


# Welcome message

print("\n")
print("Welcome to the WORD JUMBLE GAME")
print("-" * 90)

print("The computer presents a jumbled word")
print("You need to guess it. For every correct guess")
print("you will be offered points")
print("-" * 90)

# Get the words and process it 
# Read words and hints from file
# Assuming words.txt format: "word:hint,word:hint,..."
path =r"C:\Users\237237\Desktop\anacondacode\day-08\word_clue.txt"
f = open(path)
content = f.read()
f.close()

# Process the content into a list of [word, hint] pairs
word_hint_pairs = [item.split(':') for item in content.split(',')]
random.shuffle(word_hint_pairs)
 
# Track scores
total_points = 0
first_attempts = 0
second_attempts = 0
 
# Game loop
for word, hint in word_hint_pairs:
    print("\n")
    jumbled_word = jumble(word)
    print(jumbled_word)
   
    # First attempt
    user_word = input("Can you guess? ")
    if user_word == word:
        total_points += 2
        first_attempts += 1
        print("\U00002705 Correct! (2 points)")
        continue
   
    # If first attempt fails, provide hint
    print("\U00002745 Wrong!")
    print(f"CLUE: '{hint}'")
   
    # Second attempt
    user_word = input("Take a second guess? ")
    if user_word == word:
        total_points += 2
        second_attempts += 1
        print("\U00002705 Correct! (1 point)")
    else:
        print("\U00002745 Incorrect! The word was:", word)
 
# Calculate and display results
print("\n" + "-" * 80)
print("Game Over! Here are your results:")
print(f"Total Points    = {total_points}")
print(f"First Attempts  = {first_attempts}")
print(f"Second Attempts = {second_attempts}")
 
# Determine grade
total_words = len(word_hint_pairs)  #length of total words in word_clue.txt
max_points = total_words * 2
percentage = (total_points / max_points) * 100
 
if percentage >= 90:
    grade = "A+ \U0001F31F"  # Star
elif percentage >= 80:
    grade = "A \U0001F44F"   # Clapping hands
elif percentage >= 70:
    grade = "B+ \U0001F60A"  # Smiling face
elif percentage >= 60:
    grade = "B \U0001F642"   # Slight smile
elif percentage >= 50:
    grade = "C \U0001F914"   # Thinking face
else:
    grade = "D \U0001F62D"   # Crying face
 
print(f"Overall Grade   = {grade}")
 
# Example content for words.txt:
# apple:This is a red fruit,banana:Yellow curved fruit,grape:Small round fruit