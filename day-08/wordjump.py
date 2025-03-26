import random

#function to jumble the word
def jumble(w):
   temp=list(w)
   random.shuffle(temp)
   return ' '.join(temp)

path= r"C:\Users\237237\Desktop\anacondacode\day-08\word.txt"
f=open(path)
content=f.read()

print("Info content:", content)  #complete string here, debug the result
 

   #for every word in list of words
random.shuffle(content) 
for word in content:
   print("\n")
   

   #jumple the word
   jumbled_word =jumble(word)

   #show to the user
   print("Jumbled word:", jumbled_word)

   #ask user input
   user_word = input("Can you guess ->")

   #compare user input an dupdate points



 #show the Results

