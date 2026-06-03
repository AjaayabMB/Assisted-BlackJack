# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_absolute_error, r2_score
# from Monte_Carlo_Sim import cum_win_rate_byt
from D_Sto_Auto import data_extract_byt

sorting_order = {
    "A": 0,
    "K": 1,
    "Q": 2,
    "J": 3,
    "10": 4,
    "9": 5,
    "8": 6,
    "7": 7,
    "6": 8,
    "5": 9,
    "4": 10,
    "3": 11,
    "2": 12
}


def player_data_byt():
    data = data_extract_byt()
    player_score = []
    split_score = []
    dealer_score = []
    game_action = []
    game_status = []
    for i in data:
        b = 0
        for j in i:
            match b:
                case 4:
                    player_score.append(j)
                case 5:
                    split_score.append(j)
                case 8:
                    dealer_score.append(j)
                case 9:
                    game_action.append(j)
                case 10:
                    game_status.append(j)
            b += 1


def sorting_cards(input_cards):
    sorted_cards = sorted(input_cards, key=lambda card: sorting_order[card[1]])
    return sorted_cards


def assist_cc_byt(deck, pl_score):
    v_op = []
    v_sco = []
    tot_perc=0.0
    sorted_deck = sorting_cards(deck)
    for sd in range(0, len(sorted_deck)):
        sc_tbd, scor, ac = 0, 0, 0
        if sorted_deck[sd][1] in ["J", "Q", "K"]:
            scor += 10
        elif sorted_deck[sd][1] == "A":
            ac += 1
        else:
            scor += int(sorted_deck[sd][1])
        sc_tbd = pl_score + scor
        if ac != 0:
            for j in range(0, ac):
                if sc_tbd > 10:
                    sc_tbd += 1
                else:
                    sc_tbd += 11
        if sc_tbd <= 21:
            v_op.append(sorted_deck[sd])
    v_op_set = set(v_op)
    v_op_sorted = sorting_cards(v_op_set)
    for sc in range(0, len(v_op_sorted)):
        if v_op_sorted[sc][1] not in v_sco:
            v_sco.append(v_op_sorted[sc][1])
    v_sco_uni = set(v_sco)
    v_sco_li = list(v_sco_uni)
    v_sco_sorted = sorted(v_sco_li, key=lambda card: sorting_order[card])
    print("The options are:", v_sco_sorted)
    for v in v_sco_sorted:
        dup = 1
        for dec in range(0, len(deck)):
            if v == deck[dec][1]:
                dup += 1
        perc = dup / len(deck) * 100
        print(f"{v} can show up {perc:.2f}% of the time with the next hit.")
        tot_perc+=perc
    if tot_perc < 100:
        print(f"Successful hit chance is {tot_perc:.2f}% with the next hit.")
    else:
        print(f"You are guaranteed to not bust with the next hit.")

# print(cum_win_rate_byt())
