import random

print("Rules Of The Game are:\n rock vs scissor: rock wins\n scissor vs paper: scissor wins\n rock vs paper: paper wins\n\t ENTER \n1 for rock\n2 for paper\n3 for scissor")

choice = int(input("Enter choice: "))
if choice < 1 or choice > 3:
    print("ERROR\nPlease enter a valid choice")
else:
    if choice == 1:
        choice_name = 'ROCK'
    elif choice == 2:
        choice_name = 'PAPER'
    elif choice == 3:
        choice_name = 'SCISSOR'
    
    print(f"User's choice is {choice_name}")
    print("Now it's computer's turn...")

    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'ROCK'
    elif comp_choice == 2:
        comp_choice_name = 'PAPER'
    elif comp_choice == 3:
        comp_choice_name = 'SCISSOR'
    
    print(f"Computer's choice is {comp_choice_name}")

    if comp_choice == choice:
        print("It's a draw!")
    elif (comp_choice == 1 and choice == 2) or (comp_choice == 2 and choice == 3) or (comp_choice == 3 and choice == 1):
        print("You won!")
    else:
        print("You lost!")
