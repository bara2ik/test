
gameno = input("how mahy games do you want to play?")
n = int(0)
while n in range(int(gameno)):
    n += 1
    print("game number", n)
    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    vlaue_dict = {str(i): i for i in range(2, 11)}
    vlaue_dict.update({'J': 10, 'Q': 10, 'K': 10, 'A': 11})
    deck = [(rank, suit) for suit in suits for rank in ranks]
    import random
    random.shuffle(deck)
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
                break
        elif action == 's':
            print("You stand with a total of", total)
            break
        else:
            print("Invalid input. Please enter 'h' or 's'.")
    if total > 21:
        continue   
    hand1 = []
    hand1.append(deck.pop())
    hand1.append(deck.pop())
    print(hand1)
    total1 = sum(vlaue_dict[card[0]] for card in hand1)
    print(total1)            
    if total1 == 21:
        print("Blackjack! You lose.")
    elif total1 > 21:
        print("Bust! You win!")
    elif total1 < 21:
        while total1 < 21:
            if total1 < 17:
                hand1.append(deck.pop())
                total1 = sum(vlaue_dict[card[0]] for card in hand1)
                print("Dealer's hand:", hand1)
                print("Dealer's total is", total1)
                if total1 == 21:
                    print("Blackjack! You lose.")
                elif total1 > 21:
                    print("Bust! You win!") 
            elif total1 >= 17:
                print("Dealer stands with a total of", total1)
                break

    if total <= 21 and total1 <= 21:
        if total > total1:
            print("You win with a total of", total, "against dealer's", total1)
        elif total < total1:
            print("You lose with a total of", total, "against dealer's", total1)
        else:
            print("It's a tie with both at", total)

            



    
        