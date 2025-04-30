# Loop
    # Ask: Roll the dice?
    # If user enters Yes(y)
    #      Generate two random numbers
    #      print them
    #If user enters No(n)
    #      print thankyou message
    #      Terminate
    #Else
    #      print invalid choice

#_______________________CODE_________________________

import random    #used for generating pseudo-random numbers or making random selections

counter=0

while True:
    choice = input("Roll the dice (y/n)").lower()
    if choice == 'y':
        die1=random.randint(1,8)
        die2=random.randint(1,8)
        print(f'{die1},{die2}')
        counter+=1
    elif choice == 'n':
        print("Thank you for playing")
        print("The dice has been rolled",counter,"times")
        break
    else:
        print('invalid choice')






