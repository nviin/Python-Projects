# Generate a ranom number 
# Loop
#     Ask: Guess the number?
#     if not a valid numer:
#         print an error
#     if guess<number:
#         print too low
#     if guess>number:
#         print too high
#     else:
#         print correct
#         break

#________________________CODE_________________________
import random

number_to_guess = random.randint(1, 100)  

while True:
    try:
        guess = int(input("Guess the number (1-100): "))
        if guess<number_to_guess:
                print("Too low!")
        elif guess>number_to_guess:
            print("Too high!")
        else:
             print("Correct!")
             break
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue  

    