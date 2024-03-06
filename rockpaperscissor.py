import random
user_choice=int(input("Enter Your choice:Type 0 for Rock,1 for Paper,2 for Scissors: "))
if user_choice >=3 or user_choice<0 :
    print("Invalid number!!")
else:
    computer_choice=random.randint(0,2)
    print("computer choice:",computer_choice)
    if computer_choice==user_choice:
        print("It is a Draw!!")
    elif computer_choice>user_choice:
        print("You Lose.")
    elif user_choice>computer_choice:
        print("You Win.")
    elif computer_choice==0 and user_choice==2:
        print("You Lose.")
    elif user_choice==0 and computer_choice==2:
        print("You Win.")