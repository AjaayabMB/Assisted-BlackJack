from random import shuffle
from itertools import product
import sys

symbol = ["\u2663", "\u2665", "\u2666", "\u2660"]
score = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
ds, p_number, = 0, 0
a, lo, d_loop = 1, 1, 1
total_money = [1000, 1000, 1000]
total_bet, split_total_bet = [0, 0, 0], [0, 0, 0]
sp_hit, loop = "", ""
hand, hand1, hand2, hand3, d_hand, split_1_1, split_1_2, split_1_3, split_2_1, split_2_2, split_2_3, split_3_1, split_3_2, split_3_3, deck = list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list()
score1, score2, score3 = 0, 0, 0
player = [hand1, hand2, hand3]
p_score = [score1, score2, score3]
splits = [[split_1_1, split_1_2, split_1_3], [split_2_1, split_2_2, split_2_3], [split_3_1, split_3_2, split_3_3]]
gm_sts = [0, 0, 0]
gm_act = [[], [], []]
for i in range(0, 6):
    deck_sample = list(product(symbol, score))
    for j in range(0, 52):
        deck.append(deck_sample.pop())
shuffle(deck)


def hit(n):
    for i in range(0, n):
        hand.append(deck.pop(0))
    return hand


def split(i, count):
    splits[i][count].append(player[i].pop(len(player[i]) - 1))
    return splits


def split_action(i, count):
    a = 0
    if count <= 3 and a != 1:
        if player[i][0][1] == player[i][1][1] and player[i][0][1] != "A":
            print("Split!")
            split(i, count)
            money_calc("bet", i)
            print("Your current hand has now become", player[i], "And score is", current_score(i))
            print("Your split hand is", splits[i][count], "And score is", split_score(i, count))
            print("Your money after the split is:", money[i])
            count += 1
        elif (player[i][0][1] == "K" or player[i][0][1] == "Q" or player[i][0][1] == "J" or player[i][0][
            1] == "10") and (
                player[i][1][1] == "K" or player[i][1][1] == "Q" or player[i][1][1] == "J" or player[i][1][
            1] == "10"):
            print("Split!")
            split(i, count)
            money_calc("bet", i)
            print("Your current hand has now become", player[i], "And score is", current_score(i))
            print("Your split hand is", splits[i][count], "And score is", split_score(i, count))
            print("Your money after the split is:", money[i])
            count += 1
        else:
            print("Cannot Split due to difference in number. Try Again.")
    else:
        print("Maximum number of splits is 3. Try Again.")
    return count


def hit_on_split(i, count):
    splits[i][count].append(deck.pop(0))
    return splits[i]


def current_score(p_number):
    play = player[p_number]
    s = 0
    l = len(play)
    ace = 0
    for i in range(0, l):
        if play[i][1] == "J" or play[i][1] == "Q" or play[i][1] == "K":
            s += 10
        elif play[i][1] == "A":
            ace += 1
        else:
            s += int(play[i][1])
    if ace != 0:
        for j in range(0, ace):
            if s > 10:
                s += 1
            else:
                s += 11
    return s


def split_score(i, count):
    s = splits[i][count]
    sp_s = 0
    ace = 0
    for i in s:
        if i[1] == "J" or i[1] == "Q" or i[1] == "K":
            sp_s += 10
        elif i[1] == "A":
            ace += 1
        else:
            sp_s += int(i[1])
        for j in range(0, ace):
            if sp_s > 10:
                sp_s += 1
            else:
                sp_s += 11
    return sp_s


def dealer(lo):
    for i in range(0, lo):
        d_hand.append(deck.pop(0))
    return d_hand


def dealer_score(ds):
    ace = list()
    for i in range(0, len(d_hand)):
        if d_hand[i][1] == "J" or d_hand[i][1] == "Q" or d_hand[i][1] == "K":
            ds += 10
        elif d_hand[i][1] == "A":
            ace.append(d_hand[i])
        else:
            ds += int(d_hand[i][1])
    for i in range(0, len(ace)):
        if ds > 10 and len(d_hand[i]) > 2:
            ds += 1
        else:
            ds += 11
    return ds


def basic_strategy(i, sco, d_sco):
    play = player[i]
    for j in play:
        if "A" not in play:
            if sco > 17:
                return "S"
            elif 12 < sco < 17 and 1 < d_sco < 7:
                return "S"
            elif sco == 12 and 3 < d_sco < 7:
                return "S"
            elif (sco == 11) or (sco == 10 and 1 < d_sco < 10) or (sco == 9 and 2 < d_sco < 7):
                return "D"
            else:
                return "H"
        else:
            if sco > 19:
                return "S"
            elif sco == 18:
                if 1 < d_sco < 9:
                    return "S"
                elif d_sco in [9, 10, 11]:
                    return "H"
            elif 12 < sco < 18:
                return "H"
            elif sco == 18 and 2 < d_sco < 7:
                return "D"
            elif ("7" in play and 2 < d_sco < 7) or ("6" in play and 2 < d_sco < 7) or (
                    "5" in play and 3 < d_sco < 7) or ("4" in play and 3 < d_sco < 7) or (
                    "3" in play and 4 < d_sco < 7) or ("2" in play and 4 < d_sco < 7):
                return "D"
        if play[0][1] == play[1][1]:
            if sco == 20:
                return "S"
            elif play[0][1] == "5":
                return "D"
            elif (play[0][1] in ["A", "8"]) or (play[0][1] in ["2", "3"] and 1 < d_sco < 8) or (
                    play[0][1] in ["6"] and 1 < d_sco < 7) or (play[0][1] in ["7"] and 1 < d_sco < 8) or (
                    (play[0][1] in ["9"]) and (1 < d_sco < 7 or 7 < d_sco < 10)):
                if d_sco in [7, 10, 11]:
                    return "S"
                else:
                    return "SP"


def money_calc(op, i):
    if split_score(i, 0) == 0:
        match op:
            case "bet":
                print(f"Player {i + 1} has bet", bet)
                total_bet[i] += bet
                total_money[i] -= bet
            case "pay":
                print(f"Player {i + 1} has been paid", pay)
                total_money[i] += pay
    else:
        match op:
            case "bet":
                print("You have bet", bet)
                split_total_bet[i] += bet
                total_money[i] -= bet
            case "pay":
                print("You have been paid", pay)
                total_money[i] += pay


for i in range(0, 3):
    player[i] = list(hit(2))
    p_score[i] = int(current_score(i))
    print("Player", i + 1, "You've been dealt:", player[i], "And your score is", p_score[i])
    hand.clear()

print("The dealer's cards:", dealer(1), "And score is:", dealer_score(0))

# Player moves:
for i in range(0, 3):
    c = count = 0
    b = 1
    # R.I.P HERE LIES THE CHOICE TO BET
    # print("How much would you like to bet?")
    # bet=input()
    # Automation
    bet = 100
    money_calc("bet", i)
    if (p_score[i]) == 21:
        print("Player", i + 1, "'s turn.")
        print("Player", i + 1, "your current hand is:", player[i], "score is:", current_score(i))
        print("BLACKAJACKKKKKK")
    else:
        while a != 0:
            print("Player", i + 1, "'s turn.")
            print("Player", i + 1, "your current hand is:", player[i], "score is:", current_score(i))
            if b == 1:
                print("Player", i + 1, "What would you like to do?(H=Hit, S=Stand, Double=D, Split=SP)")
                b += 1
            else:
                print("Would you like to hit again, stand or split?(Hit=H,Stand=S,Split=SP)")
            # RIP Here lies choice.
            # choice = input()
            # Automation:
            choice = basic_strategy(i, current_score(i), dealer_score(0))
            match choice.upper():
                case "H":
                    print("Hit!")
                    gm_act[i].append("H")
                    player[i].append(hit(1).pop())
                    if (current_score(i)) > 21:
                        print("Your new hand is", player[i], "And score is", current_score(i))
                        print("Busssssss")
                        if split_score(i, 0) == 0:
                            break
                        else:
                            print("Dealer Wins first hand.")
                            break
                    else:
                        print("Your current hand is", player[i], "And score is", current_score(i))
                        continue
                case "S":
                    print("Stand!")
                    break
                case "D":
                    if b != 1:
                        print("Doubling after hitting not allowed.")
                        break
                    else:
                        print("Double!")
                        print("Bet doubled to", 2 * bet)
                        bet = 100
                        money_calc("bet", i)
                        player[i] = hit(1)
                        print("Your current hand is", player[i], "And score is", current_score(i))
                        break
                case "SP":
                    c = split_action(i, count)
                    continue
    if split_score(i, 0) != 0:
        for j in range(0, c):
            b = 1
            while a != 0:
                print("Your split hand no.", j + 1, "is", splits[i][j], "And score is", split_score(i, j))
                if b == 1:
                    sp_hit = input(
                        "Would you like to hit or stand on your split hand?(Hit=H, Stand=S,Split=SP,Double=D)")
                    b += 1
                else:
                    sp_hit = input("Would you like to hit again, stand or split?(Hit=H,Stand=S,Split=SP)")
                match sp_hit.upper():
                    case "H":
                        split_one = hit_on_split(j, count)
                        if (split_score(i, 0)) > 21:
                            print("Your split hand no.", j + 1, "is", splits[i][j], "And score is", split_score(i, j))
                            print("Bussssssstttt")
                            break
                        else:
                            print("Your split hand no.", j + 1, "is", splits[i][j], "And score is", split_score(i, j))
                    case "S":
                        break
                    case "SP":
                        if "A" in splits[i][j]:
                            split_one = hit_on_split(i, j)
                            print("Your current hand is", splits[i][j], "And score is", split_score(i, j))
                            print("Maximum number of hits for aces reached.")
                            break
                    case "D":
                        if b != 1:
                            print("Doubling after hitting not allowed.")
                            break
                        else:
                            print("Double!")
                            print("Bet doubled to", 2 * bet)
                            bet = 100
                            money_calc("bet", i)
                            split_one = hit_on_split(j, count)
                            print("Your split hand no.", j + 1, "is", splits[i][j], "And score is", split_score(i, j))
                            break
print("The dealer's cards:", d_hand, "And score is:", dealer_score(0))
while dealer_score(0) <= 17:
    h = 0
    for i in range(0, len(d_hand)):
        if d_hand[i][1] != "A" and dealer_score(0) < 17:
            h = 0
        elif d_hand[i][1] == "A" and dealer_score(0) <= 17:
            h = 1
        else:
            h = 2
    if h == 0:
        print("Dealer drawing.")
        print("The dealer's cards:", dealer(1), "And score is:", dealer_score(0))
    elif h == 1:
        print("Dealer drawing.")
        print("The dealer's cards:", dealer(1), "And score is:", dealer_score(0))
    else:
        break
    print("Dealer stops drawing.")
if dealer_score(0) > 21:
    print("Dealer Busts.")
    for i in range(0, 3):
        print("Player", i + 1, "'s cards:", player[i], "And score is:", current_score(i))
        if current_score(i) > 21:
            print("Player", i + 1, "loses too.")
        else:
            print("Dealer Busts. Player", i + 1, "wins.")
            pay = 2 * total_bet[i]
            money_calc("pay", i)
            gm_sts[i] = 1
else:
    for i in range(0, 3):
        print("Player", i + 1, "'s cards:", player[i], "And score is:", current_score(i))
        if current_score(i) == 21 and len(player[i]) == 2:
            pay = total_bet[i] + 1.5 * total_bet[i]
            money_calc("pay", i)
        elif current_score(i) < dealer_score(0) <= 21:
            print("Dealer Wins. Player", i + 1, "loses.")
        elif dealer_score(0) < current_score(i) <= 21:
            print("Dealer Loses. Player", i + 1, "wins.")
            pay = 2 * total_bet[i]
            money_calc("pay", i)
            gm_sts[i] = 1
        elif current_score(i) == dealer_score(0) and dealer_score(0) <= 21:
            print("Dealer and Player", i + 1, "tie.")
            pay = 2 * total_bet[i]
            money_calc("pay", i)
            gm_sts[i] = 1
        else:
            print("Dealer Wins. Player", i + 1, "busts.")
for i in range(0, 3):
    print("Player", i + 1, "'s money now:", total_money[i])
game_data = {"dealer_score": dealer_score(0)}
for i in range(0, 3):
    game_data[f"Player_Score_{i + 1}"] = current_score(i)
    game_data[f"Total_Money_{i + 1}"] = total_money[i]
    game_data[f"Game_Status_{i + 1}"] = gm_sts[i]
    game_data[f"Game_Action_{i + 1}"] = gm_act[i]
    # print(f"For player {i+1}:")
    # print(game_data[f"Player_Score_{i + 1}"])
    # print(game_data[f"Total_Money_{i + 1}"])
    # print(game_data[f"Game_Status_{i + 1}"])
    # print(game_data[f"Game_Action_{i + 1}"])
