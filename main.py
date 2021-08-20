import random, time
TotalRounds = 0
Ai_wins = 0
Player_wins = 0
money = 0
def startMenu():
    global rounds, money
    print("Welcome to BlackJack")
    rounds = int(input('Enter rounds played:'))
    money = int(input('Enter total money:'))
    MainDraw()



def MainDraw():
    global total, BlackJack, money, bet
    global card
    global card2
    while True:
        bet = int(input('Enter bet:'))
        if bet > money:
            print(f'You cannot bet that much you can bet at most ${money}')
        else:
            money = money - bet
            break
    #player draw
    BlackJack = False
    card = random.randint(1,13)
    card2 = random.randint(1, 13)

    print('New Hand..')
    time.sleep(.3)

    if card == 11:
        card = 10
    if card == 12:
        card = 10
    if card == 1:
        card = 10

    if card2 == 11:
        card = 10
    if card2 == 12:
        card2 = 10
    if card2 == 1:
        card2 = 10

    if card == 13:
        print('You Got A Ace')
        print('1 or 11')
        try:
            while True:
                ace = int(input('>'))
                if ace == 1:
                    card = 1
                    break
                elif ace == 11:
                    card = 11
                    break
        except:
            ValueError
            print('enter 1 or 11')

    if card2 == 13:
        print('1 or 11')
        try:
            while True:
                ace2 = int(input('>'))
                if ace2 == 1:
                    card2 = 1
                    break
                elif ace2 == 11:
                    card2 = 11
                    break
        except:
            ValueError
            print('enter 1 or 11')

    total = card + card2
    print('Calculating cards...')
    time.sleep(.4)
    print(f'card 1 : {card}')
    print(f'card 2 : {card2}')
    print(f'total : {total}')


    if total > 21:
        print('Bust')
        print("""
        
        """)
        AIDraw()
    if total == 21:
        money = money + bet*2 + (bet/2)
        print("BlackJack")
        print(f'You won ${bet*2 + (bet/2)} with a total of {money}')
        BlackJack = True
        AIDraw()
    print("""


       """)
    time.sleep(1)
    AIDraw()


def AIDraw():
    global AItotal

    AIcard = random.randint(1, 13)
    AIcard2 = random.randint(1, 13)



    if AIcard == 12:
        AIcard = 10
    if AIcard == 11:
        AIcard = 10
    if AIcard == 1:
        AIcard = 10

    if AIcard2 == 12:
        AIcard2 = 10
    if AIcard2 == 11:
        AIcard2 = 10
    if AIcard2 == 1:
        AIcard2 = 10



    if AIcard == 13:
        AIcard = 11
    if AIcard2 == 13:
        AIcard2 = 11

    if AIcard == 11 and AIcard2 == 11:
        AIcard2 = 1
    time.sleep(.4)

    AItotal = AIcard + AIcard2
    print('Calculating ai cards cards...')
    time.sleep(.4)
    print(f'Ai card 1 : {AIcard}')
    print('Ai card2 :  hidden')
    print('total : ???')

    if AItotal == 21:
        print("BlackJack")
        print("""
        
        """)

    draw_card()



def draw_card():
    global total, card2, card, bust, money, bet
    bust = False
    print("""
    
    """)
    while True:
        print(f'you have {total}, hit or stand')
        action = input('>')

        if 'hit' in action:
            hit_card = random.randint(1, 13)
            if hit_card == 11:
                hit_card = 10
            if hit_card == 12:
                hit_card = 10
            if hit_card == 1:
                hit_card = 10
            if hit_card == 13:
                print('You Got A Ace')
                print('1 or 11')
                try:
                    while True:
                        ace = int(input('>'))
                        if ace == 1:
                            hit_card = 1
                            break
                        elif ace == 11:
                            hit_card = 11
                            break
                except:
                    ValueError
                    print('enter 1 or 11')

            total = total + hit_card

            time.sleep(.3)

            print(f'you have picked up {hit_card}')
            print(f'your total is {total}')

            if total > 21:
                print('Bust')
                time.sleep(.5)

                bust = True
                print("""
                
                """)
                ai_draw_card()
            if total == 21:
                print("BlackJack")
                money = money + bet * 2
                print(f'You won ${bet * 2 } with a total of {money}')

                time.sleep(.5)
                print("""

                                """)
                ai_draw_card()

        elif 'stand' in action:
            print('You chose stand')
            time.sleep(.5)
            print("""
            
            """)
            ai_draw_card()

        else:
            print('invalid command')
            print("""
               
     
           """)







def ai_draw_card():
    global AItotal, bust, AIblackJack, AIbust, total

    AIbust = False
    AIblackJack = False

    while True:
        time.sleep(1)
        if bust == True or AItotal > total:
            print(f'Ai chose stand with {AItotal}')
            print("""
            
            """)
            time.sleep(1)
            #Stand thing
            taly()

            break

        if AItotal <= total:
            time.sleep(1)
            ai_hit_card = random.randint(1, 13)
            if ai_hit_card == 11:
                ai_hit_card = 10
            if ai_hit_card == 12:
                ai_hit_card = 10
            if ai_hit_card == 1:
                ai_hit_card = 10
            if ai_hit_card == 13:
                if total > 10:
                    ai_hit_card = 1
                else:
                    ai_hit_card = 11
            print("Ai chose hit")
            AItotal += ai_hit_card
            time.sleep(1)
            print(f"they drew {ai_hit_card} with a total of ???? ")
            print("""
            
            """)
            if AItotal > 21:
                print('Bust')
                print("""
                
                
                """)
                time.sleep(1)
                AIbust = True
                taly()
            if AItotal == 21:
                print("BlackJack")
                print("""

                        """)

                time.sleep(1)
                AIblackJack = True
                taly()
            print("""

                  """)





def taly():
    global bust, AIblackJack, AIbust, BlackJack, total, AItotal, rounds, TotalRounds, Ai_wins, Player_wins, money, bet

    TotalRounds += 1


    if bust == True:
        print("Ai wins")
        print(f"you lost, you have ${money}")
        time.sleep(2)
        print("""

                """)


    elif AIblackJack and BlackJack:
        print("Tie")
        money = money + bet
        print(f'Push you have ${money}')
        time.sleep(2)
        print("""

                """)

    elif AIbust and bust:
        print("Tie")
        time.sleep(2)
        print("""

                """)



    elif BlackJack:
        Player_wins += 1
        print("You Win")
        time.sleep(2)
        print("""

                """)


    elif AIblackJack:
        Ai_wins += 1
        print("Ai wins")
        print(f"you lost, you have ${money}")
        time.sleep(2)
        print("""

                """)
    elif AIbust:
        Player_wins += 1
        print("You Win")
        money = money + bet * 2
        print(f'You won ${bet * 2} with a total of {money}')
        time.sleep(2)

    elif total > AItotal:
        Player_wins += 1
        print("You Win")
        money = money + bet * 2
        print(f'You won ${bet * 2} with a total of {money}')
        time.sleep(2)


    elif total < AItotal:
        Ai_wins += 1
        print("Ai wins")
        print(f"you lost, you have ${money}")
        time.sleep(2)
        print("""
        
        """)


    if TotalRounds == rounds:
        print("Round over")
        print(f"The score was {Player_wins} Player wins and {Ai_wins} Ai wins ")
        exit()


    MainDraw()








startMenu()
