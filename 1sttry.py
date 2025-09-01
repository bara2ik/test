import random


options = ['rock', 'paper', 'scissors']
computer = random.choice(options)

player = input("enter your name: ")
choice = input("enter : rock, paper, scissors: ")





if choice not in options:
    print("Invalid choice! Please enter rock, paper, or scissors.")
elif choice == computer:
    print("tie")
elif choice == 'rock' and computer == 'scissors':
     print(player + ' wins')
elif choice == 'paper' and computer == 'rock':
    print(player + ' wins')     
elif choice == 'scissors' and computer == 'paper':
    print(player + ' wins') 
else:
    print("computer wins")  

print("computer chose: " + computer)

