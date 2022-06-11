import random

def Choose_Option():
    user_choice = input("Choose Rock, Paper or Scissors: ")
    if user_choice in ["Rock", "rock", "R", "r"]:
        user_choice = "R"
    elif user_choice in ["Paper", "paper", "P", "p"]:
        user_choice = "P"
    elif user_choice in ["Scissors", "scissors", "S", "s"]:
        user_choice = "S"
    else:
        print("Invalid option selected, please try again.")
        Choose_Option()
    return user_choice

def Computer_Option():
    cmp_choice = random.randint(1, 3)
    if cmp_choice == 1:
        cmp_choice = "R"
    elif cmp_choice == 2:
        cmp_choice = "P"
    else:
        cmp_choice = "S"
    return cmp_choice
    
while True:
    print("")

    user_choice = Choose_Option()
    cmp_choice = Computer_Option()

    print("")

    if user_choice == cmp_choice:
        print("computer: ", cmp_choice)
        print("player: ", user_choice)
        print("It's a Tie!")
            
    elif user_choice == "R":
        if cmp_choice == "P":
            print("computer: ", cmp_choice)
            print("player: ", user_choice)
            print("Paper beats Rock! You lose!")
                
        elif cmp_choice == "S":
            print("computer: ", cmp_choice)
            print("player: ", user_choice)
            print("Rock beats Scissors! You win!")

    elif user_choice == "P":
        if cmp_choice == "R":
            print("computer: ", cmp_choice)
            print("player: ", user_choice)
            print("Paper beats rock! You win!")
        
        elif cmp_choice == "S":
            print("computer: ", cmp_choice)
            print("player: ", user_choice)
            print("Scissors beats Paper! You lose!")

    elif user_choice == "S":
        if cmp_choice == "R":
            print("computer: ", cmp_choice)
            print("player: ", user_choice)
            print("Rock beats Scissors! You lose!")
            
        elif cmp_choice == "P":
            print("computer: ", cmp_choice)
            print("player: ", user_choice)
            print("Scissors beats Paper! You win!")
                
    user_choice = input("Do you want to play again? (y/n): ")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        print("You have ended the game. Thank you for Playing!")
        break
    else:
        print("Thank you for Playing!")
        break
    








                
