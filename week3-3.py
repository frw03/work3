# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:27:34 2024

@author: student
"""

import random

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [rank for rank in ranks for _ in range(4)]

random.shuffle(deck)

player_hands = [[], [], [], []]

for i in range(len(deck)):
    player_hands[i % 4].append(deck[i])

for hand in player_hands:
    hand.sort(key=lambda card: ranks.index(card))

for i, hand in enumerate(player_hands):
    print(f"玩家 {i+1} 的手牌：")
    for card in hand:
        print(card, end=" ")
    print()