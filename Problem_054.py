# Project Euler - Problem #54 - Poker Hands - Solved - 0.05s

import common_functions
from collections import Counter
from datetime import datetime
startTime = datetime.now()


high_card_points = 1
pair_points = 2
two_pair_points = 3
three_of_a_kind_points = 4
straight_points = 5
flush_points = 6
full_house_points = 7
four_of_a_kind_points = 8
straight_flush_points = 9
royal_flush_points = 10

card_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

all_cards = {
    'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, 
    '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

p1_wins = []
p2_wins = []
no_winner = []

def get_high_card(cards):
    card_vals = []
    for card in cards:
        card_val = all_cards[card]
        card_vals.append(card_val)

    for card, val in all_cards.items():
        if val == max(card_vals):
            #print("High Card:",card)
            return True

def get_pair(cards):
    pair = [x for x in cards if cards.count(x) > 1]
    if len(pair) == 2:
        #print("Pair of:", pair)
        return True
    else:
        return False

def get_two_pair(cards):
    two_pair = [x for x in cards if cards.count(x) > 1]
    if len(two_pair) == 4:
        if len(set(two_pair)) == 2:
            #print("Two Pair:",two_pair)
            return True
        else:
            return False
    else:
        return False

def get_three_of_a_kind(cards):
    three_of_a_kind = [x for x in cards if cards.count(x) > 1]
    if len(three_of_a_kind) == 3:
        #print("Three of a Kind:", three_of_a_kind)
        return True
    else:
        return False


def get_straight(cards):
    card_index = []
    for card in cards:
        #print("CARD:",card)
        index = card_order.index(card)
        card_index.append(index)
        #print("CARD INDEX:", card_index)

    if len(set(card_index)) == 5:
        if 0 not in card_index:
            if max(card_index) - min(card_index) == 4:
                #print("Straight:",card_index)
                return True
        else:
            if max(card_index) - min(card_index) == 4:
                #print("Straight:",card_index)
                return True
            elif 0 in card_index and 12 in card_index and 9 in card_index and 10 in card_index and 11 in card_index:
                #print("Straight:",card_index)
                return True


def get_flush(suits):
    if len(suits) == 5:
        if len(set(suits)) == 1:
            #print("Flush:",suits)
            return True
        else:
            return False

def get_full_house(cards):
    full_house = [x for x in cards if cards.count(x) > 1]
    if len(full_house) == 5:
        #print("Full House:", full_house)
        return True
    else:
        return False

def get_four_of_a_kind(cards):
    four_of_a_kind = [x for x in cards if cards.count(x) > 1]
    if len(four_of_a_kind) == 4:
        if len(set(four_of_a_kind)) == 1:
            #print("Four of a Kind:", four_of_a_kind)
            return True
        else:
            return False
    else:
        return False

def get_straight_flush(cards, suits):
    card_index = []
    if len(suits) == 5:
        if len(set(suits)) == 1:

            for card in cards:
                index = card_order.index(card)
                card_index.append(index)

                #print("CARD INDEX:",card_index)

                if 0 not in card_index:
                    if max(card_index) - min(card_index) == 4:
                        #print("Straight Flush:",card_index)
                        return True
                else:
                    if max(card_index) - min(card_index) == 4:
                        #print("Straight Flush:",card_index)
                        return True
                    elif 0 in card_index and 12 in card_index and 9 in card_index and 10 in card_index and 11 in card_index:
                        #print("Straight Flush:",card_index)
                        return True


def get_royal_flush(cards, suits):
    card_index = []
    if len(suits) == 5:
        if len(set(suits)) == 1:

            for card in cards:
                index = card_order.index(card)
                card_index.append(index)

                if 0 in card_index:
                    if max(card_index) - min(card_index) == 4:
                        #print("Royal Flush:",card_index)
                        return True

def tie_breaker(points, hand1_cards, hand2_cards, hand1_suits, hand2_suits):
    hand1_points = []
    hand2_points = []
    #print("Hand 1 Cards:",hand1_cards)
    #print("Hand 2 Cards:",hand2_cards)

    for card in hand1_cards:
        card_val = all_cards[card]
        hand1_points.append(card_val) 

    for card in hand2_cards:
        card_val = all_cards[card]
        hand2_points.append(card_val)

    # High Card / Straight / Flush
    if points == 1 or points == 5 or points == 6 or points == 9:
        if points == 1 or points == 6:
            p1_high_card = get_high_card(hand1_cards)
            p2_high_card = get_high_card(hand2_cards)

            if max(hand1_points) > max(hand2_points):
                #print("WINNER: Player 1")
                p1_wins.append(1)
            elif max(hand2_points) > max(hand1_points):
                #print("WINNER: Player 2")
                p2_wins.append(1)
            else:
                hand1_points.remove(max(hand1_points))
                hand2_points.remove(max(hand2_points))
                if max(hand1_points) > max(hand2_points):
                    #print("WINNER: Player 1")
                    p1_wins.append(1)
                elif max(hand2_points) > max(hand1_points):
                    #print("WINNER: Player 2")
                    p2_wins.append(1)

        elif points == 5 or points == 9:
            p1_card_index = []
            p2_card_index = []
            for card in hand1_cards:
                index = card_order.index(card)
                p1_card_index.append(index)

            #print("P1 Card Index:",p1_card_index)

            for card in hand2_cards:
                index = card_order.index(card)
                p2_card_index.append(index)
            #print("P2 Card Index:",p2_card_index)
            
            if 0 in p1_card_index or 0 in p2_card_index:
                if points == 5:
                    if 1 in p1_card_index or 1 in p2_card_index:
                        if max(p1_card_index) - min(p1_card_index) == 12:
                            hand1_points = [14]
                        if max(p2_card_index) - min(p2_card_index) == 12:
                            hand2_points = [14]
                    else:
                        if max(p1_card_index) - min(p1_card_index) == 12:
                            hand1_points = [5]
                        if max(p2_card_index) - min(p2_card_index) == 12:
                            hand2_points = [5]
                else:
                    if max(p1_card_index) - min(p1_card_index) == 12:
                        hand1_points = [5]
                    if max(p2_card_index) - min(p2_card_index) == 12:
                        hand2_points = [5]

                if max(hand1_points) > max(hand2_points):
                    #print("WINNER: Player 1")
                    p1_wins.append(1)
                elif max(hand2_points) > max(hand1_points):
                    #print("WINNER: Player 2")
                    p2_wins.append(1)
            else:
                
                if max(hand1_points) > max(hand2_points):
                    #print("WINNER: Player 1")
                    p1_wins.append(1)
                elif max(hand2_points) > max(hand1_points):
                    #print("WINNER: Player 2")
                    p2_wins.append(1)
    
    elif points == 2 or points == 3 or points == 4 or points == 7 or points == 8:
        
        pair1 = [x for x in hand1_cards if hand1_cards.count(x) > 1]
        pair2 = [x for x in hand2_cards if hand2_cards.count(x) > 1]
        pair1_val = []
        pair2_val = []
        pair1_min_val = []
        pair2_min_val = []

        #print("PAIR1:",pair1)
        #print("PAIR2:",pair2)

        # Pair or 3-of-a-kind or 4-of-a-kind
        if len(set(pair1)) == 1:
            #print("PAIR 1 MAX:", max(pair1))
            #print("PAIR 2 MAX:", max(pair2))
            
            for card in max(pair1):
                card_val = all_cards[card]
                pair1_val.append(card_val)

            for card in max(pair2):
                card_val = all_cards[card]
                pair2_val.append(card_val)

            if pair1_val > pair2_val:
                #print("WINNER: Player 1")
                p1_wins.append(1)
            elif pair2_val > pair1_val:
                #print("WINNER: Player 2")
                p2_wins.append(1)
            else:
                no_pairs1 = hand1_cards
                no_pairs2 = hand2_cards
                for card in pair1:
                    if card in hand1_cards:
                        no_pairs1.remove(card)
                for card in pair2:
                    if card in hand2_cards:
                        no_pairs2.remove(card)

                #print("NO PAIRS1:",no_pairs1)
                #print("NO PAIRS2:",no_pairs2)
                
                if 'A' in no_pairs1 and 'A' not in no_pairs2:
                    p1_wins.append(1)
                elif 'A' in no_pairs2 and 'A' not in no_pairs1:
                    p2_wins.append(1)
                else:
                    if max(no_pairs1) > max(no_pairs2):
                        #print("WINNER: Player 1")
                        p1_wins.append(1)
                    elif max(no_pairs2) > max(no_pairs1):
                        #print("WINNER: Player 2")
                        p2_wins.append(1)
   
        # Two Pair or (Full House)
        elif len(set(pair1)) == 2:
  
            #print("PAIR1:",pair1)
            #print("PAIR2:",pair2)

            for card in pair1:
                #print(card)
                card_val = all_cards[card]
                pair1_val.append(card_val)

            for card in pair2:
                #print(card)
                card_val = all_cards[card]
                pair2_val.append(card_val)

            if max(pair1_val) > max(pair2_val):
                #print("MAX PAIR1:",pair1_val)
                #print("MAX PAIR2:",pair2_val)
                #print("WINNER: Player 1")
                p1_wins.append(1)
            elif max(pair2_val) > max(pair1_val):
                #print("MAX PAIR3:",pair1_val)
                #print("MAX PAIR4:",pair2_val)
                #print("WINNER: Player 2")
                p2_wins.append(1)
            else:
                if min(pair1_val) > min(pair2_val):
                    #print("MAX PAIR5:",pair1_val)
                    #print("MAX PAIR6:",pair2_val)
                    #print("WINNER: Player 1")
                    p1_wins.append(1)
                elif min(pair2_val) > min(pair1_val):
                    #print("MAX PAIR7:",pair1_val)
                    #print("MAX PAIR8:",pair2_val)
                    #print("WINNER: Player 2")
                    p2_wins.append(1)
                else:
                    no_pairs1 = hand1_cards
                    no_pairs2 = hand2_cards

                    for card in pair1:
                        if card in hand1_cards:
                            no_pairs1.remove(card)
                    for card in pair2:
                        if card in hand2_cards:
                            no_pairs2.remove(card)

                    #print("NO PAIRS1:",no_pairs1)
                    #print("NO PAIRS2:",no_pairs2)
                    
                    if 'A' in no_pairs1 and 'A' not in no_pairs2:
                        p1_wins.append(1)
                    elif 'A' in no_pairs2 and 'A' not in no_pairs1:
                        p2_wins.append(1)
                    else:
                        if max(no_pairs1) > max(no_pairs2):
                            #print("WINNER: Player 1")
                            p1_wins.append(1)
                        elif max(no_pairs2) > max(no_pairs1):
                            #print("WINNER: Player 2")
                            p2_wins.append(1)

    elif points == 10:
        #print("SPLIT POT")
        no_winner.append(line_list)


with open('Problem_054_poker.txt') as f_open:
    for line in f_open:
        #print('\n',line)

        line_list = list(filter((' ').__ne__, line))

        # Start Test Section
        #hand = '6H 6C 9C 6D TH KD KS 9D KC AH'
        #line_list = list(filter((' ').__ne__, hand))


        joined_str = ''.join(line_list)
        hand1 = joined_str[0:10]
        hand2 = joined_str[10:]

        # ~~~~~PLAYER 1~~~~~
        #print("\nPlayer 1:", joined_str[0:10])
        hand1_cards = []
        hand1_suits = []

        for i in range(0,10,2):
            hand1_cards.append(hand1[i])

        for i in range(1,10,2):
            hand1_suits.append(hand1[i])

        # Player 1 High Card
        p1_high_card = get_high_card(hand1_cards)
        # Player 1 Pair
        p1_pair = get_pair(hand1_cards)
        # Player 1 Two Pair
        p1_two_pair = get_two_pair(hand1_cards)
        # Player 1 Three of a Kind
        p1_three_of_a_kind = get_three_of_a_kind(hand1_cards)
        # Player 1 Straight
        p1_straight = get_straight(hand1_cards)
        # Player 1 Flush
        p1_flush = get_flush(hand1_suits)
        # Player 1 Full House
        p1_full_house = get_full_house(hand1_cards)
        # Player 1 Four of a Kind
        p1_four_of_a_kind = get_four_of_a_kind(hand1_cards)
        # Player 12 Straight Flush
        p1_straight_flush = get_straight_flush(hand1_cards, hand1_suits)
        # Player 1 Royal Flush
        p1_royal_flush = get_royal_flush(hand1_cards, hand1_suits)

        # ~~~~~PLAYER 2~~~~~
        #print("\nPlayer 2:", joined_str[10:])
        hand2_cards = []
        hand2_suits = []

        for i in range(0,10,2):
            hand2_cards.append(hand2[i])
        for i in range(1,10,2):
            hand2_suits.append(hand2[i])

        # Player 2 High Card
        p2_high_card = get_high_card(hand2_cards)
        # Player 2 Pair
        p2_pair = get_pair(hand2_cards)
        # Player 21 Two Pair
        p2_two_pair = get_two_pair(hand2_cards)
        # Player 2 Three of a Kind
        p2_three_of_a_kind = get_three_of_a_kind(hand2_cards)
        # Player 2 Straight
        p2_straight = get_straight(hand2_cards)
        # Player 2 Flush
        p2_flush = get_flush(hand2_suits)
        # Player 2 Full House
        p2_full_house = get_full_house(hand2_cards)
        # Player 2 Four of a Kind
        p2_four_of_a_kind = get_four_of_a_kind(hand2_cards)
        # Player 2 Straight Flush
        p2_straight_flush = get_straight_flush(hand2_cards, hand2_suits)
        # Player 2 Royal Flush
        p2_royal_flush = get_royal_flush(hand2_cards, hand2_suits)

        #print("\nCOMPARISON PHASE")
        p1_points = []
        if p1_high_card == True:
            p1_points.append(high_card_points)
        if p1_pair == True:
            p1_points.append(pair_points)
        if p1_two_pair == True:
            p1_points.append(two_pair_points)
        if p1_three_of_a_kind == True:
            p1_points.append(three_of_a_kind_points)
        if p1_straight == True:
            p1_points.append(straight_points)
        if p1_flush == True:
            p1_points.append(flush_points)
        if p1_full_house == True:
            p1_points.append(full_house_points)
        if p1_four_of_a_kind == True:
            p1_points.append(four_of_a_kind_points)
        if p1_straight_flush == True:
            p1_points.append(straight_flush_points)
        if p1_royal_flush == True:
            p1_points.append(royal_flush_points)

        p2_points = []
        if p2_high_card == True:
            p2_points.append(high_card_points)
        if p2_pair == True:
            p2_points.append(pair_points)
        if p2_two_pair == True:
            p2_points.append(two_pair_points)
        if p2_three_of_a_kind == True:
            p2_points.append(three_of_a_kind_points)
        if p2_straight == True:
            p2_points.append(straight_points)
        if p2_flush == True:
            p2_points.append(flush_points)
        if p2_full_house == True:
            p2_points.append(full_house_points)
        if p2_four_of_a_kind == True:
            p2_points.append(four_of_a_kind_points)
        if p2_straight_flush == True:
            p2_points.append(straight_flush_points)
        if p2_royal_flush == True:
            p2_points.append(royal_flush_points)


        #print("Player 1 Score:",max(p1_points))
        #print("Player 2 Score:",max(p2_points))

        if max(p1_points) > max(p2_points):
            #print("WINNER: Player 1")
            p1_wins.append(1)
        elif max(p2_points) > max(p1_points):
            #print("WINNER: Player 2")
            p2_wins.append(1)
        else:
            #print("HAND IS A TIE. GO TO WHO HAS BETTER HAND")
            
            if max(p1_points) == 1:
                tie_breaker(max(p1_points),hand1_cards,hand2_cards,hand1_suits,hand2_suits)
            elif max(p1_points) == 2:
                tie_breaker(max(p1_points),hand1_cards,hand2_cards,hand1_suits,hand2_suits)
            elif max(p1_points) == 3:
                tie_breaker(max(p1_points),hand1_cards,hand2_cards,hand1_suits,hand2_suits)
            elif max(p1_points) == 4:
                tie_breaker(max(p1_points),hand1_cards,hand2_cards,hand1_suits,hand2_suits)
            elif max(p1_points) == 5:
                tie_breaker(max(p1_points),hand1_cards,hand2_cards,hand1_suits,hand2_suits)
            if max(p1_points) == 6:
                tie_breaker(max(p1_points),hand1_cards,hand2_cards,hand1_suits,hand2_suits)       
            elif max(p1_points) == 7:
                tie_breaker(max(p1_points),hand1_cards,hand2_cards,hand1_suits,hand2_suits)
            elif max(p1_points) == 8:
                tie_breaker(max(p1_points),hand1_cards,hand2_cards,hand1_suits,hand2_suits)
            elif max(p1_points) == 9:
                tie_breaker(max(p1_points),hand1_cards,hand2_cards,hand1_suits,hand2_suits)
            elif max(p1_points) == 10:
                tie_breaker(max(p1_points),hand1_cards,hand2_cards,hand1_suits,hand2_suits)

        # End Test Section


print("\nPlayer 1 Wins:", sum(p1_wins))
print("Player 2 Wins:", sum(p2_wins))
print("No Winner:",no_winner)

print('\nDuration: ')
print(datetime.now() - startTime)
