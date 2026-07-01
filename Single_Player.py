from random import shuffle
from itertools import product
from D_Sto_Auto import shoe_check_byt
from D_Sto_Auto import money_check_byt
from Da_Assistant import assist_cc_byt
from Da_Assistant import assist_inherit_byt
from Monte_Carlo_Sim import simulation_mom

Developer_Mode = False
symbol = ["\u2663", "\u2665", "\u2666", "\u2660"]
score = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
deck = list()
discard_deck = list()
round_no = 0
for i in range(0, 6):
    deck_sample = list(product(symbol, score))
    for j in range(0, 52):
        deck.append(deck_sample.pop())
shuffle(deck)


def hit(n):
    for k in range(0, n):
        hand.append(deck.pop(0))
    return hand


def split(w, co):
    splits[w][co].append(player[w].pop(len(player[w]) - 1))
    return splits


def split_action(x, coun):
    p = 0
    if coun <= 3 and p != 1:
        if player[x][0][1] == player[x][1][1] and player[x][0][1] != "A":
            print("Split!")
            split(x, coun)
            gm_act[x].append("SP")
            money_calc("bet", x)
            print("Your current hand has now become", player[x], "And score is", current_score(x))
            print("Your split hand is", splits[x][coun], "And score is", split_score(x, coun))
            print("Your money after the split is:", total_money[x])
            coun += 1
        elif (player[x][0][1] == "K" or player[x][0][1] == "Q" or player[x][0][1] == "J" or player[x][0][
            1] == "10") and (
                player[x][1][1] == "K" or player[x][1][1] == "Q" or player[x][1][1] == "J" or player[x][1][
            1] == "10"):
            print("Split!")
            split(x, coun)
            gm_act[x].append("SP")
            money_calc("bet", x)
            print("Your current hand has now become", player[x], "And score is", current_score(x))
            print("Your split hand is", splits[x][coun], "And score is", split_score(x, coun))
            print("Your money after the split is:", total_money[x])
            coun += 1
        elif (player[x][0][1] == "A") and (player[x][0][1] == player[x][1][1]):
            print("Split!")
            split(x, coun)
            gm_act[x].append("SP")
            money_calc("bet", x)
            print("Your current hand has now become", player[x], "And score is", current_score(x))
            print("Your split hand is", splits[x][coun], "And score is", split_score(x, coun))
            print("Your money after the split is:", total_money[x])
            coun = 3
        else:
            print("Cannot Split due to difference in number. Try Again.")
    else:
        print("Maximum number of splits is 3. Try Again.")
    return coun


def hit_on_split(q, co):
    splits[q][co].append(deck.pop(0))
    return splits[q]


def current_score(p_num):
    play = player[p_num]
    s = 0
    l = len(play)
    ace = 0
    for aa in range(0, l):
        if play[aa][1] == "J" or play[aa][1] == "Q" or play[aa][1] == "K":
            s += 10
        elif play[aa][1] == "A":
            ace += 1
        else:
            s += int(play[aa][1])
    if ace != 0:
        for ab in range(0, ace):
            if s > 10:
                s += 1
            else:
                s += 11
    return s


def split_score(ac, countt):
    s = splits[ac][countt]
    sp_s = 0
    ace = 0
    for ac in s:
        if ac[1] == "J" or ac[1] == "Q" or ac[1] == "K":
            sp_s += 10
        elif ac[1] == "A":
            ace += 1
        else:
            sp_s += int(ac[1])
    if ace != 0:
        for ad in range(0, ace):
            if sp_s > 10:
                sp_s += 1
            else:
                sp_s += 11
    return sp_s


def dealer(ae):
    if ae != 0:
        for af in range(0, ae):
            d_hand.append(deck.pop(0))
    return d_hand


def dealer_score(dss):
    ace = list()
    for ag in range(0, len(d_hand)):
        if d_hand[ag][1] == "J" or d_hand[ag][1] == "Q" or d_hand[ag][1] == "K":
            dss += 10
        elif d_hand[ag][1] == "A":
            ace.append(d_hand[ag])
        else:
            dss += int(d_hand[ag][1])
    for ag in range(0, len(ace)):
        if dss > 10 and len(d_hand[ag]) > 2:
            dss += 1
        else:
            dss += 11
    return dss


def money_calc(op, ah):
    if split_score(ah, 0) == 0:
        match op:
            case "bet":
                print(f"Player {ah + 1} has bet", bet)
                total_bet[ah] += bet
                total_money[ah] -= bet
            case "pay":
                print(f"Player {ah + 1} has been paid", pay)
                total_money[ah] += pay
    else:
        match op:
            case "bet":
                print("You have bet", bet)
                split_total_bet[ah] += bet
                total_money[ah] -= bet
            case "pay":
                print("You have been paid", pay)
                total_money[ah] += pay


shoe_no = shoe_check_byt()
while len(deck) >= 75:
    hand, hand1, hand2, hand3, d_hand, split_1_1, split_1_2, split_1_3, split_2_1, split_2_2, split_2_3, split_3_1, split_3_2, split_3_3 = list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list(), list()
    score1, score2, score3 = 0, 0, 0
    round_no += 1
    player = [hand1, hand2, hand3]
    p_score = [score1, score2, score3]
    splits = [[split_1_1, split_1_2, split_1_3], [split_2_1, split_2_2, split_2_3],
              [split_3_1, split_3_2, split_3_3]]
    sp_score = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    gm_sts = [0, 0, 0]
    gm_act = [[], [], []]
    ds, p_number, = 0, 0
    a, lo, d_loop = 1, 1, 11
    total_bet, split_total_bet = [0, 0, 0], [0, 0, 0]
    sp_hit, loop = "", ""
    total_money = [0, 0, 0]
    if Developer_Mode:
        player[0] = [('♠', '5'), ('♥', '6')]
        # d_hand = [('♦', '6')]
        total_money[0] = 2000
    else:
        for i in range(0, 3):
            total_money[i] = money_check_byt(i + 1)
            player[i] = list(hit(2))
            p_score[i] = int(current_score(i))
            print("Player", i + 1, "You've been dealt:", player[i], "And your score is", p_score[i])
            hand.clear()
    print("The dealer's cards:", dealer(1), "And score is:", dealer_score(0))
    for i in range(0, 3):
        c = count = 0
        b = 1
        bet = int(input("How much would you like to bet? "))
        money_calc("bet", i)
        if (p_score[i]) == 22:
            print("Player", i + 1, "'s turn.")
            print("Player", i + 1, "your current hand is:", player[i], "score is:", current_score(i))
            gm_act[i].append("BJ")
            print("BLACKAJACKKKKKK")
        else:
            while a != 0:
                print("Player", i + 1, "'s turn.")
                print("Player", i + 1, "your current hand is:", player[i], "score is:", current_score(i))
                if b == 1:
                    print("Player", i + 1, "What would you like to do?(H=Hit, S=Stand, Double=D, Split=SP)")
                else:
                    print("Would you like to hit again, stand or split?(Hit=H,Stand=S,Split=SP)")
                assist_cc_byt(deck, current_score(i))
                assist_inherit_byt(player[i], dealer(0))
                simulation_mom(deck, player[i], dealer(0))
                choice = input()
                match choice.upper():
                    case "H":
                        b += 1
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
                        gm_act[i].append("S")
                        break
                    case "D":
                        if b != 1:
                            print("Doubling after hitting not allowed.")
                            break
                        else:
                            print("Double!")
                            gm_act[i].append("D")
                            bet = 100
                            money_calc("bet", i)
                            print("So, Bet doubled to", 2 * bet)
                            player[i].append(hit(1).pop())
                            print("Your current hand is", player[i], "And score is", current_score(i))
                            break
                    case "SP":
                        c = split_action(i, count)
                        continue
        if split_score(i, 0) != 0:
            for j in range(0, c):
                b = 1
                sp_score[i][j] = split_score(i, j)
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
                            gm_act[i].append("H")
                            split_one = hit_on_split(j, count)
                            if (split_score(i, 0)) > 21:
                                print("Your split hand no.", j + 1, "is", splits[i][j], "And score is",
                                      split_score(i, j))
                                print("Bussssssstttt")
                                break
                            else:
                                print("Your split hand no.", j + 1, "is", splits[i][j], "And score is",
                                      split_score(i, j))
                        case "S":
                            gm_act[i].append("S")
                            break
                        case "SP":
                            if "A" in splits[i][j]:
                                split_one = hit_on_split(i, j)
                                gm_act[i].append("H")
                                print("Your current hand is", splits[i][j], "And score is", split_score(i, j))
                                print("Maximum number of hits for aces reached.")
                                break
                            else:
                                c = split_action(i, count)
                        case "D":
                            if b != 1:
                                print("Doubling after hitting not allowed.")
                                break
                            else:
                                print("Double!")
                                gm_act[i].append("D")
                                # noinspection PyUnboundLocalVariable
                                print("Bet doubled to", 2 * bet)
                                bet = 2 * bet
                                money_calc("bet", i)
                                split_one = hit_on_split(j, count)
                                print("Your split hand no.", j + 1, "is", splits[i][j], "And score is",
                                      split_score(i, j))
                                break
    print("The dealer's cards:", d_hand, "And score is:", dealer_score(0))
    while dealer_score(0) < 17:
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
    print("The dealer's final hand is:", dealer(0), "And score is:", dealer_score(0))
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
                gm_sts[i] = 1
            elif current_score(i) < dealer_score(0) <= 21:
                print("Dealer Wins. Player", i + 1, "loses.")
                gm_sts[i] = -1
            elif dealer_score(0) < current_score(i) <= 21:
                print("Dealer Loses. Player", i + 1, "wins.")
                pay = 2 * total_bet[i]
                money_calc("pay", i)
                gm_sts[i] = 1
            elif current_score(i) == dealer_score(0) and dealer_score(0) <= 21:
                print("Dealer and Player", i + 1, "tie.")
                pay = total_bet[i]
                money_calc("pay", i)
                gm_sts[i] = 0
            else:
                print("Dealer Wins. Player", i + 1, "busts.")
                gm_sts[i] = -1
    for i in range(0, 3):
        print("Player", i + 1, "'s money now:", total_money[i])
