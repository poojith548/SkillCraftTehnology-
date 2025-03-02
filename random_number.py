import random

def main():
    number_to_guess = random.randint(1, 100)
    user_guess = 0
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    
    while user_guess != number_to_guess:
        user_guess = int(input("Enter your guess: "))
        attempts += 1
        
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number: {number_to_guess}")
            print(f"It took you {attempts} attempts.")
            
if _name_ == "_main_":
    main()