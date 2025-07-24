import random
import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty_type = input("Choose a difficulty. Type 'easy' or 'hard': ")
comp_choice = random.randint(1, 100)

if difficulty_type == "easy":
    num_of_attempts = 10
elif difficulty_type == "hard":
    num_of_attempts = 5
else:
    print("Invalid input. Exiting.")
    exit()

def guess_the_num(user_num):
    if user_num < comp_choice:
        print("Too low.\nGuess again.")
        return False
    elif user_num > comp_choice:
        print("Too high.\nGuess again.")
        return False
    else:
        print(f"You got it! The answer was {comp_choice}")
        return True

for attempt in range(num_of_attempts, 0, -1):
    print(f"You have {attempt} attempts remaining to guess the number.")
    num = int(input("Make a guess: "))
    if guess_the_num(num):
        break
else:
    print(f"You've run out of guesses. The number was {comp_choice}.")
