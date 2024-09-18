import random
print("Rules Of The Game are :\n rock vs scissor: rock wins\n scissor vs paper: scissor wins\n rock vs paper:  paper wins\n\t ENTER \n1 for rock\n2 for paper\n3 for scissor")

choice=int(input("enter choice:"))
if choice>3:
    print("ERROR\nplease enter a valid choice")

if choice==1:
    choice_name='ROCK'
elif choice==2:
    choice_name='PAPER'
elif choice==3:
    choice_name='SCISSOR'
    
print(f"users choice is {choice_name}'")
print("now its computers turn")

comp_choice=random.randint(0,3)
print(f"computers choice is {choice_name}'")

if comp_choice==choice:
    print("it's a draw ")
elif comp_choice==1 and choice==2:
    print("you won ")
elif comp_choice==2 and choice==1:
    print("you lost ")
elif comp_choice==2 and choice==3:
     print("you won ")
elif comp_choice==3 and choice==2:
    print("you lost ")    
elif comp_choice==3 and choice==1:
     print("you won ")
elif comp_choice==1 and choice==3:
    print("you lost ")