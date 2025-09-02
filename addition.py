suits = ['spades', 'hearts', 'diamonds', 'clubs']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
vlaue_dict = {str(i): i for i in range(2, 11)}
vlaue_dict.update({'J': 10, 'Q': 10, 'K': 10, 'A': 11})
deck = [(rank, suit) for suit in suits for rank in ranks]
import random
random.shuffle(deck)
print(deck)
print(vlaue_dict)
print(len(deck))
hand = []
hand.append(deck.pop())
hand.append(deck.pop())
print(hand)
total = sum(vlaue_dict[card[0]] for card in hand)
print(total)            
if total == 21:
    print("Blackjack! You win!")
elif total > 21:

    print("Bust! You lose!")
else:
    print("Your total is", total)
while total < 21:
    action = input("Do you want to hit or stand? (h/s): ")
    if action == 'h':
        hand.append(deck.pop())
        total = sum(vlaue_dict[card[0]] for card in hand)
        print("Your hand:", hand)
        print("Your total is", total)
        if total == 21:
            print("Blackjack! You win!")
        elif total > 21:
            print("Bust! You lose!")
    elif action == 's':
        print("You stand with a total of", total)
        break
    else:
        print("Invalid input. Please enter 'h' or 's'.")
    print("Bust! You lose!")
        break
        