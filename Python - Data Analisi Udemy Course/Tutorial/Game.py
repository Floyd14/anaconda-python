# Imports
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

def two_dice_roll(n):
    """ Roll 2 dice n number of times and get sum """
    d1 = np.random.random_integers(1,6,n)
    d2 = np.random.random_integers(1,6,n)
    dice_sum = d1 + d2
    return dice_sum

def craps_game(N,intial_bet,bankroll):
    """ Simulates N number of craps games """
    print ('starting bankroll is= ' + str(bankroll))
    bankroll_tracker = [bankroll]
    # For N number of Craps games
    for game in range(0,N):
        
        bet = intial_bet
        bankroll -= bet
        
        # Come out roll
        dval = two_dice_roll(1)

        # Lose on 7 or 11
        if dval == 7 or dval == 11:
            status = 'loss'
            
        # Win on 2 or 3
        elif dval == 2 or dval == 3: #Push/Tie on 12
            status = 'win'
        # Create Point Marker
        else:
            status = 'come_point'
            #play don't pass odds 5x
            
            odds_played = True
            # Take out from your bankroll
            bankroll -= (5*bet)
            # Then place your odds bets
            bet = (5*bet) + bet
            dpoint = dval

        # Point roll
        while status == 'come_point':
            add_roll = two_dice_roll(1)

            # Lose if point is hit
            if add_roll == dpoint:
                status = 'loss'
                
            # Win if 7 is rolled
            elif add_roll == 7:
                status = 'win'

        if status == 'win':
            #win_count += 1
            bankroll += 2*bet
            bankroll_tracker.append(bankroll)
            
        else:
            bankroll_tracker.append(bankroll)
            pass
        
    plt.plot(range(N+1),bankroll_tracker)          
    return bankroll

craps_game(50,10,250)
