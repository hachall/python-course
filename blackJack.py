import random as r
import time as t
import sys
AllCards = ['?_D', '2_D', '3_D', '4_D', '5_D', '6_D', '7_D', '8_D', '9_D', '+_D', 'J_D', 'Q_D', 'K_D',
            '?_H', '2_H', '3_H', '4_H', '5_H', '6_H', '7_H', '8_H', '9_H', '+_H', 'J_H', 'Q_H', 'K_H',
            '?_C', '2_C', '3_C', '4_C', '5_C', '6_C', '7_C', '8_C', '9_C', '+_C', 'J_C', 'Q_C', 'K_C',
            '?_S', '2_S', '3_S', '4_S', '5_S', '6_S', '7_S', '8_S', '9_S', '+_S', 'J_S', 'Q_S', 'K_S',]
currentCards = AllCards
Hand = []
hitting = 'yes'
playerAnswer = ''
selectedCard = ''
currentNumb = ''
currentTotal = 0
Acing = 'no'
AcingAmount = 0
dealerTotal = 0
dead = 0
blackjacked = 0
money = 10000
wager = 0
moneyLost = 0

def end(b):
    global money
    global wager
    global dead
    global currentCards
    global Hand
    global hitting
    global playerAnswer
    global selectedCard
    global currentNumb
    global currentTotal
    global Acing
    global AcingAmount
    global dealerTotal
    global playerAnswer
    global blackjacked
    global moneyLost
    hitting = 'no'
    if Acing == 'yes':
        if AcingAmount == 1:
            if currentTotal+11 < 22:
                playerAnswer = input('Would you like your ace to be 1 or 11 (l or h)?')
            else:
                playerAnswer = 'l'
        elif AcingAmount == 2:
            if currentTotal+12 < 22:
                playerAnswer = input('Would you like your aces to be two or 12 (l or h)?')
            else:
                playerAnswer = 'l'
        elif AcingAmount == 3:
            if currentTotal+13 < 22:
                playerAnswer = input('Would you like your aces to be three or 13 (l or h)?')
            else:
                playerAnswer = 'l'
        else:
            if currentTotal+14 < 22:
                playerAnswer = input('Would you like your aces to be four or 14 (l or h)?')
            else:
                playerAnswer = 'l'
        if playerAnswer == 'h':
            currentTotal = currentTotal+(11+(AcingAmount-1))
        else:
            currentTotal = currentTotal + AcingAmount
    dead = 1
    t.sleep(1)
    if blackjacked == 0:
        dealerTotal = r.randint(15, 20)
    if b == 'no':
        print('Okay then, let\'s see what the dealer has...')
        t.sleep(1)
        print('The dealer had: ' + str(dealerTotal))
        t.sleep(1)
        if dealerTotal > currentTotal:
            print('Aaaah, he\'s too good!')
            t.sleep(1)
            print('He takes the money, and now you have £' + str(money))
            moneyLost = moneyLost + wager
        elif dealerTotal == currentTotal:
            print('You both tie!')
            t.sleep(1)
            print('No one gets the money...')
            money = money + wager
        else:
            print('Wow! You did well!')
            t.sleep(1)
            print('You get £' + str(wager*2) + '!')
            money = money + (wager*2)
            t.sleep(1)
            print('You now have ' + str(money))
        t.sleep(1)
        
    elif b == 'yes':
        print('Let\'s see what the dealer had then...')
        t.sleep(1)
        print(dealerTotal)
        t.sleep(1)
        print('Well, that doesn\'t even matter, you lost...')
        t.sleep(1)
        print('He takes your wager, and now you have £' + str(money))
        moneyLost = moneyLost + wager
        hitting = 'no'
    else:
        dealerTotal = r.randint(1, 10)
        if dealerTotal == 3:
            print('He had a blackjack! Your money does not get altered...')
            wager = 0
        else:
            dealerTotal = r.randint(13, 20)
            t.sleep(1)
            print('Damn, it looks like he had ' + str(dealerTotal))
            t.sleep(1)
            print('You lose £' + str(wager/2) + '...')
            moneyLost = wager/2
            money = money - (wager/2)
    currentCards = AllCards
    Hand = []
    hitting = 'yes'
    playerAnswer = ''
    selectedCard = ''
    currentNumb = ''
    currentTotal = 0
    Acing = 'no'
    AcingAmount = 0
    dealerTotal = 0
    blackjacked = 0
    wager = 0
    playerAnswer = input('Play again? (Y = yes, N = no)')
    if playerAnswer == 'N':
        hitting = 'no'
        print('You ended with £' + str(money) + ', you started with £10,000, and you lost £' + str(moneyLost))
    else:
        dead = 0
        hitting = 'no'
playerAnswer = input('Welcome to BlackJack! Type R for the rules or S to start (Any + means 10, and any ? means an ace)')

if playerAnswer == 'R':
    print("""Okay, here are the rules:
            The aim is to get your hand as close to 21 as possible (or 21)
            On your turn, you can either stand or hit.
            Stand means keep your cards, hit means take another card
            If you hit, and the total of your cards is over 21, your bust
            id your bust, then you automatically lose
            if you stand, and your closer to 21 than him, then you win.
            If he is closer, you lose
            A king, queen or jack all mean 10
            Finally, an ace can mean a one or an 11 (you can choose)
            Wagering lots of money is risky, but you could win lots
            Wagering a small amount ensures that you don't lose too much
            You start off with £10,000 in you bank
            You can also change what an aces value is throughout the game
            If the dealer flips up an ace, then you can do one of these:
                1)Call insurance, making your bet turn into a half bet,
                and if the dealer does have a blackjack, then you get
                your whole wager returned and nothing lost (I)
                2) You can play on, thinking that the dealer does not
                have a blackjack. If he does, then you lose one and a
                half of your bet...
            (Additionly, this is the card layout: <TYPE>_<SUITE-INITIAL>)
            Any '+' means it's a 10, any '?' means it's an ace""")
while playerAnswer == 'S' or playerAnswer == 'Y':
    if money > 0:
        playerAnswer = int(input('How much do you want to wager for this round? You have £'+str(money)))
        if int(playerAnswer) > money:
            print('You don\'t have that much money! Automatically wagering £100...')
            wager = 100
            money = money - 100
        elif 1 > int(playerAnswer):
            print('You have to wager something! Automatically wagering £100...')
            wager = 100
            money = money - 100
        else:
            wager = int(playerAnswer)
            money = money - wager
        hitting = 'yes'
    else:
        t.sleep(1)
        print('Sorry, but it looks like you\'re broke. Maybe the casino life just isn\'t for you.')
        dead = 1
        hitting = 'no'
        playerAnswer = 'N'
        sys.exit()
    while hitting == 'yes':
        t.sleep(1)
        playerAnswer = input('Stand (s) or Hit (h)?')
        if playerAnswer == 's' or playerAnswer == 'S':
            end('no')
        elif playerAnswer == 'h' or playerAnswer == 'H':
            print('Okay, let\'s see your hand now...')
            selectedCard = r.choice(currentCards)
            Hand.append(selectedCard)
            currentCards.remove(selectedCard)
            currentTotal = 0
            for x in range(0, len(Hand)):
                selectedCard = Hand[x]
                currentNumb = selectedCard[:1]
                if currentNumb == '?':
                    if x == (len(Hand)-1):
                        Acing = 'yes'
                        AcingAmount = AcingAmount + 1
                elif currentNumb == '+':
                    currentTotal = currentTotal + 10
                elif currentNumb == "Q" or currentNumb == "J" or currentNumb == "K":
                    currentTotal = currentTotal + 10
                else:
                    currentTotal = currentTotal + int(currentNumb)
            t.sleep(1)
            print(Hand)
            t.sleep(1)
            if Acing == 'yes':
                if AcingAmount == 1:
                    print('You can either have a total of ' + str(currentTotal+1) + ' or ' + str(currentTotal+11))
                elif AcingAmount == 2:
                    print('You can either have a total of ' + str(currentTotal+2) + ' or ' + str(currentTotal+12))
                elif AcingAmount == 3:
                    print('You can either have a total of ' + str(currentTotal+3) + ' or ' + str(currentTotal+13))
                else:
                    print('You can either have a total of ' + str(currentTotal+4) + ' or ' + str(currentTotal+14))
            else:
                print('Which has a total of: ' + str(currentTotal))
            if Acing == 'no':
                if currentTotal > 21:
                    t.sleep(2)
                    print('Your bust!')
                    end('yes')
            else:
                if AcingAmount == 1 and (currentTotal+1) > 21:
                    t.sleep(2)
                    print('Your bust!')
                    end('yes')
                elif AcingAmount == 2 and (currentTotal+2) > 21:
                    t.sleep(2)
                    print('Your bust!')
                    end('yes')
                elif AcingAmount == 3 and (currentTotal+3) > 21:
                    t.sleep(2)
                    print('Your bust!')
                    end('yes')
                elif AcingAmount == 4 and (currentTotal+4) > 21:
                    t.sleep(2)
                    print('Your bust!')
                    end('yes')
            if dead == 0:
                t.sleep(1)
                print('You opponent draws a card...')
                selectedCard = r.randint(0, 10)
                if blackjacked == 0:
                    if selectedCard == 0:
                        t.sleep(2)
                        playerAnswer = input('He flips up a card, revealing an ace. Do you want to call insurance (I) or keep playing (P)?')
                        if playerAnswer == 'I':
                            t.sleep(1)
                            print('You call insurance, hoping he has blackjack. Let\'s take a look...')
                            end('other')
                        else:
                            t.sleep(1)
                            print('Okay, but he might have a blackjack...')
                            blackjacked = 1
                            dealerTotal = r.randint(1, 6)
                            if dealerTotal == 3:
                                blackjacked = 1
                            else:
                                blackjacked = 0
