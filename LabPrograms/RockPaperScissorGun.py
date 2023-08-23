#Implementation of Rock Paper Scissor Game
import random

def TheGame():
    while True:
        print("Enter your Choice\n" + "1: Rock\n2: Paper\n3: Scissor\n4: Gun")
        choice = int(input())
        while choice>4 or choice<1:
            choice = int(input("Enter a valid choice" +"1: Rock\n2: Paper\n3: Scissor\n"))
        comp_choice = random.randint(1,4)
        while comp_choice == choice:
            comp_choice = random.randint(1,4)

        if choice == 1:
            sel_choice= 'Rock'
        elif choice == 2:
            sel_choice= 'Paper'
        elif choice == 3:
            sel_choice= 'Scissors'
        else:
            sel_choice= 'Gun'   
        print(name,","+ "Your choice is ",sel_choice , ",Now it's Computer's turn")
        
        if comp_choice == 1:
            comp_choice_name = 'rocks'
        elif comp_choice == 2:
            comp_choice_name = 'papers'
        elif comp_choice == 3:
            comp_choice_name = 'scissors'
        else:
            comp_choice_name = 'Gun'
        print("Computer choosed",comp_choice_name)

        if sel_choice == comp_choice:
            print("It's a draw.")
            result = 0
        #"1: Rock\n2: Paper\n3: Scissor
        if (choice ==1 and comp_choice==2):
            print("Computer Wins")
            result =  -1
        if (choice ==2 and comp_choice==1):
            print(name," You won buddyy. Hurrayyy!!!!!")
            result = 1

        if (choice ==3 and comp_choice==1):
            print("Computer Wins")
            result =  -1
        if (choice ==1 and comp_choice==3):
            print(name," You won buddyy. Hurrayyy!!!!!")
            result = 1

        if (choice ==2 and comp_choice==3):
            print("Computer Wins")
            result =  -1
        if (choice ==3 and comp_choice==2):
            print("You won buddyy. Hurrayyy!!!!!")
            result = 1

        if (choice ==4 and comp_choice==1):
            print("You won buddyy. Hurrayyy!!!!!")
            result = 1

        if (choice ==1 and comp_choice==4):
            print("Computer Wins")
            result =  -1

        if (choice ==2 and comp_choice==4):
            print("You won buddyy. Hurrayyy!!!!!")
            result = 1

        if (choice ==4 and comp_choice==2):
            print("Computer Wins")
            result =  -1

        if (choice ==4 and comp_choice==3):
            print("You won buddyy. Hurrayyy!!!!!")
            result = 1

        if (choice ==3 and comp_choice==4):
            print("Computer Wins")
            result =  -1
        
        if (result == 0  or result == -1):
            print("Better luck next time :(")
        else:
            print("Congrats", name,","+ "You have made it!!!")
        
        print("Do you wanna play again? Press(Y/N)")
        ch = input()
        if ch =="N":
            break
        else:
            pass

# result = 0
name = input("What's your name boss?\n")
print("\nHi", name, ",Welcome to the Rock paper Scissor Water Gun game!!!")
print("We do have some rules. Do you wanna go through the rules? \n Press 1 for Yes or 2 for Skip")
ch = int(input())
if ch ==1:
    print("The rules are as following: " + "\nRock vs Paper-> Paper wins"+ "\nRock vs Scissor-> Rock wins"+ "\nPaper vs Scissor-> Scissor wins"+ "\nRock vs Gun-> Gun wins" + "\nPaper vs Gun-> Paper wins" + "\nScissor vs Gun-> Gun wins")
else:
    pass
print("Are you ready!!\n Press 1 for Yes or 2 for No, will come back later.")
ch = int(input())
if ch ==1:
    TheGame()
    print("Thanks for playing", name,".Come again:)")
else:
    print("Okay.Come again. Waiting to play with you buddy.")


