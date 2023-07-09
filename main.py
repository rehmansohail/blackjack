import random
import art


cardlist=["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]


def fill(li,cards):
    global score
    card=random.choice(cards)
    if card=="J"or card=="Q"or card=="K":
        score+=10
    elif card=="A":
        if score+11>21:
            score+=1
        else:
            score+=11
    else:
        score+=card
    li.append(card)
score=0
 
 
 
print(art.logo)
flag=input("Do you want to play blackjack? 'yes' or 'no'\n").lower()
while 1:
    
    a=False
    user_score=0
    dealer_score=0
    user_cards=[]
    dealer_cards=[]
    if flag=="no":
        break
    elif flag=="yes":
        #initial filling of user cards
        for i in range(2):
            score=0
            fill(user_cards,cardlist)
            user_score+=score
        #initial filling of dealer cards
        for i in range(2):
            score=0
            fill(dealer_cards,cardlist)
            dealer_score+=score
        
        if user_score==21 or dealer_score==21:
            a=True
            if user_score==dealer_score:
                print("Match tied")
                print("Your cards")
                print(user_cards)
                print(user_score)
                print("Dealer's cards")
                print(dealer_cards)
                print(dealer_score)
            elif user_score==21:
                print("You won")
                print("Your cards")
                print(user_cards)
                print(user_score)
                print("Dealer's cards")
                print(dealer_cards)
                print(dealer_score)
            else:
                print("You lost")
                print("Your cards")
                print(user_cards)
                print(user_score)
                print("Dealer's cards")
                print(dealer_cards)
                print(dealer_score) 
            flag=input("Do you want to play another game? 'yes' or 'no'\n").lower()
                
        
        if a==False:
            print("Your cards")
            print(user_cards)
            print(f"Your score is {user_score}")
            print(f"Dealer's first card is {dealer_cards[0]}")    
            # complete filling of dealer deck
            while dealer_score<17:
                score=0
                fill(dealer_cards,cardlist)
                dealer_score+=score
            cont=""
            cont=input("Do you want to hit a card? 'yes' or 'no'\n").lower()
            while 1:
                if cont=="no":
                    break
                elif cont=="yes":
                    score=0
                    fill(user_cards,cardlist)
                    user_score+=score
                    print("Your cards")
                    print(user_cards)
                    print(user_score)
                    if user_score>=21:
                        break
                    else:
                        cont=input("Do you want to hit a card? 'yes' or 'no'\n").lower()
                    
                else:
                    print("Invalid input")    
            
                
            #final check
            if user_score>21:
                print("You lost")
                print("Your cards")
                print(user_cards)
                print(user_score)
                print("Dealer's cards")
                print(dealer_cards)
                print(dealer_score)
            else:
                if dealer_score>21:
                    print("You won")
                    print("Your cards")
                    print(user_cards)
                    print(user_score)
                    print("Dealer cards")
                    print(dealer_cards)
                    print(dealer_score)
                    
                elif user_score>dealer_score:
                    print("You won")
                    print("Your cards")
                    print(user_cards)
                    print(user_score)
                    print("Dealer cards")
                    print(dealer_cards)
                    print(dealer_score)
                elif user_score<dealer_score:
                    print("You lost")
                    print("Your cards")
                    print(user_cards)
                    print(user_score)
                    print("Dealer cards")
                    print(dealer_cards)
                    print(dealer_score)
                else:
                    print("Match tied")
                    print("Your cards")
                    print(user_cards)
                    print(user_score)
                    print("Dealer cards")
                    print(dealer_cards)
                    print(dealer_score)
            flag=input("Do you want to play another game? 'yes' or 'no'\n").lower()
                    
    else:
        print("Invalid input")
        break