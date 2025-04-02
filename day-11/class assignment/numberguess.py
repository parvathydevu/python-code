import random

class GuessNumber(object):
    #constructor
    def __init__(self, name,lower=1,higher=100,max_attempts=10):
        self.name=name
        self.lower=lower
        self.higher=higher
        self.max_attempts=max_attempts
        self.target=random.randint(self.lower,self.higher)
        self.attempts=0
    #member function
    def guess(self,number):
        self.attempts += 1
        if number < self.target:
            return "Lower"
        elif number > self.target:
            return "Higher"
        else:
            return "Correct"
    def run(self):
        print(f"Computer has chosen a number between {self.lower} and {self.higher}. Can you guess it? {self.max_attempts} guesses.")
        while self.attempts < self.max_attempts:
            user_input = int(input("-> "))
            result = self.guess(user_input)  #pass user input value to guess function
            print(result)

            if result == "Correct":
                print(f"Gamer {self.name}:- Number of attempts: {self.attempts}/{self.max_attempts}")
                print("Excellent playing!")
                break
        else:
            print(f"Sorry {self.name}, you've used all {self.max_attempts} attempts. The correct number was {self.target}.")
# Test
if __name__ == "__main__":
    player_name = input("Enter your name: ")
    ob1 = GuessNumber(player_name)
    ob1.run()
        
 
        