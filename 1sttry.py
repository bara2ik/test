import random


options = ['rock', 'paper', 'scissors']

def get_choice():
    
    player1 = input("enter the player's name: ")
    player2 = input("enter the 2ND player's name: ")
    while True:
        entry = input("enter  : rock, paper, scissors: ")
        entry1 = input("enter : rock, paper, scissors: ")
        choices = {'player1': entry , 'player2' : entry1}
        if entry  not in options or  entry1 not in options:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue
        choices = {'player1': entry , 'player2' : entry1}
        return choices






def getresult(choice1 ,choice2):
   
        
    if choice1 == choice2:
        print("tie")
    elif choice1 == 'rock' and choice2 == 'scissors':
        print('player1 wins')
    elif choice1 == 'paper' and choice2 == 'rock':
        print(' player1 wins')     
    elif choice1 == 'scissors' and choice2 == 'paper':
        print('player1 wins') 
    else:
        print("player2 wins") 
    
 



choice = get_choice()

print(getresult(choice['player1'], choice['player2']))



