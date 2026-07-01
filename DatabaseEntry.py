from random import shuffle
from itertools import product
from D_Sto_Auto import shoe_check_byt
from D_Sto_Auto import insert_it
# from D_Sto_Auto import reset_cash
from D_Sto_Auto import money_check_byt
# from Da_Assistant import assist_cc_byt

def hit(n):
    for aa in range(0, n):
        hand.append(deck.pop(0))
    return hand


def split(ab, coun):
    splits[ab][coun].append(player[ab].pop(len(player[ab]) - 1))
    return splits


def split_action(ac, cou):
    ad = 0
    if cou <= 3 and ad != 1:
        if player[ac][0][1] == player[ac][1][1] and player[ac][0][1] != "A":
            print("Split!")
            split(ac, cou)
            gm_act[ac].append("SP")
            money_calc("bet", ac)
            print("Your current hand has now become", player[ac], "And score is", current_score(ac))
            print("Your split hand is", splits[ac][cou], "And score is", split_score(ac, cou))
            print("Your money after the split is:", total_money[ac])
            cou += 1
        elif (player[ac][0][1] == "K" or player[ac][0][1] == "Q" or player[ac][0][1] == "J" or player[ac][0][
            1] == "10") and (
                player[ac][1][1] == "K" or player[ac][1][1] == "Q" or player[ac][1][1] == "J" or player[ac][1][
            1] == "10"):
            print("Split!")
            split(ac, cou)
            gm_act[ac].append("SP")
            money_calc("bet", ac)
            print("Your current hand has now become", player[ac], "And score is", current_score(ac))
            print("Your split hand is", splits[ac][cou], "And score is", split_score(ac, cou))
            print("Your money after the split is:", total_money[ac])
            cou += 1
        elif (player[ac][0][1] == "A") and (player[ac][0][1] == player[ac][1][1]):
            print("Split!")
            split(ac, cou)
            gm_act[ac].append("SP")
            money_calc("bet", ac)
            print("Your current hand has now become", player[ac], "And score is", current_score(ac))
            print("Your split hand is", splits[ac][cou], "And score is", split_score(ac, cou))
            print("Your money after the split is:", total_money[ac])
            cou = 3
        else:
            print("Cannot Split due to difference in number. Try Again.")
    else:
        print("Maximum number of splits is 3. Try Again.")
    return cou


def hit_on_split(ae, countt):
    splits[ae][countt].append(deck.pop(0))
    return splits[ae]


def current_score(p_num):
    play = player[p_num]
    s = 0
    l = len(play)
    ace = 0
    for af in range(0, l):
        if play[af][1] == "J" or play[af][1] == "Q" or play[af][1] == "K":
            s += 10
        elif play[af][1] == "A":
            ace += 1
        else:
            s += int(play[af][1])
    if ace != 0:
        for ag in range(0, ace):
            if s > 10:
                s += 1
            else:
                s += 11
    return s


def split_score(ah, co):
    s = splits[ah][co]
    sp_s = 0
    ace = 0
    for ah in s:
        if ah[1] == "J" or ah[1] == "Q" or ah[1] == "K":
            sp_s += 10
        elif ah[1] == "A":
            ace += 1
        else:
            sp_s += int(ah[1])
    if ace != 0:
        for ai in range(0, ace):
            if sp_s > 10:
                sp_s += 1
            else:
                sp_s += 11
    return sp_s


def dealer(lop):
    if lop != 0:
        for aj in range(0, lop):
            d_hand.append(deck.pop(0))
    return d_hand


def dealer_score(dss):
    ace = list()
    for aj in range(0, len(d_hand)):
        if d_hand[aj][1] == "J" or d_hand[aj][1] == "Q" or d_hand[aj][1] == "K":
            dss += 10
        elif d_hand[aj][1] == "A":
            ace.append(d_hand[aj])
        else:
            dss += int(d_hand[aj][1])
    for aj in range(0, len(ace)):
        if dss > 10 and len(d_hand[aj]) > 2:
            dss += 1
        else:
            dss += 11
    return dss


def basic_strategy(play, sco, d_sco):
    for _ in play:
        if "A" not in play:
            if sco > 17:
                return "S"
            elif 12 < sco < 17 and 1 < d_sco < 7:
                return "S"
            elif sco == 12 and 3 < d_sco < 7:
                return "S"
            elif ((sco == 11) or (sco == 10 and 1 < d_sco < 10) or (sco == 9 and 2 < d_sco < 7)) and len(play) < 3:
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
    return None


def money_calc(op, al):
    if split_score(al, 0) == 0:
        match op:
            case "bet":
                print(f"Player {al + 1} has bet", bet)
                total_bet[al] += bet
                total_money[al] -= bet
            case "pay":
                print(f"Player {al + 1} has been paid", pay)
                total_money[al] += pay
    else:
        match op:
            case "bet":
                print("You have bet", bet)
                split_total_bet[al] += bet
                total_money[al] -= bet
            case "pay":
                print("You have been paid", pay)
                total_money[al] += pay



for loop in range(0, 10000):
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

    # Cash reset:
    # total_money = reset_cash()
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
        # game_data = {}
        ds, p_number, = 0, 0
        a, lo, d_loop = 1, 1, 1
        total_bet, split_total_bet = [0, 0, 0], [0, 0, 0]
        sp_hit, loop = "", ""
        total_money = [0, 0, 0]
        initial_player_hand, initial_dealer_hand, ip, dea = [[], [], []], list(), list(), list()
        # Card Deal:
        for i in range(0, 3):
            total_money[i] = money_check_byt(i + 1)
            player[i] = list(hit(2))
            p_score[i] = int(current_score(i))
            print("Player", i + 1, "You've been dealt:", player[i], "And your score is", p_score[i])
            hand.clear()
            ip.append(player[i][0])
            initial_player_hand[i].append(ip.pop())
            ip.append(player[i][1])
            initial_player_hand[i].append(ip.pop())

        print("The dealer's cards:", dealer(1), "And score is:", dealer_score(0))
        dea.append(dealer(0))
        initial_dealer_hand.append(dea.pop())
        # Player moves:
        for i in range(0, 3):
            c = count = 0
            b = 1
            print("Your current money amount is:", total_money[i])
            # R.I.P HERE LIES THE CHOICE TO BET
            # print("How much would you like to bet?")
            # bet=input()
            # Automation
            bet = 100
            money_calc("bet", i)
            if (p_score[i]) == 21:
                print("Player", i + 1, "'s turn.")
                print("Player", i + 1, "your current hand is:", player[i], "score is:", current_score(i))
                gm_act[i].append("BJ")
                print("BLACKAJACKKKKKK")
            else:
                while a != 0:
                    print("Player", i + 1, "'s turn.")
                    print("Player", i + 1, "your current hand is:", player[i], "score is:", current_score(i))
                    # Assistant:
                    # assist_cc_byt(deck, current_score(i))
                    if b == 1:
                        print("Player", i + 1, "What would you like to do?(H=Hit, S=Stand, Double=D, Split=SP)")
                    else:
                        print("Would you like to hit again, stand or split?(Hit=H,Stand=S,Split=SP)")
                    # RIP Here lies choice.
                    # choice = input()
                    # Automation:
                    choice = basic_strategy(player[i], current_score(i), dealer_score(0))
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
                                    print("Bet doubled to", 2 * bet)
                                    bet = 100
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
            action = str(gm_act[i])
            i_p_h = str(initial_player_hand[i])
            p_h = str(player[i])
            i_d_h = str(initial_dealer_hand)
            d_h = str(dealer(0))
            insert_it(shoe_no, round_no, i + 1, i_p_h, p_h, current_score(i), total_bet[i], total_money[i],
                      i_d_h, d_h, dealer_score(0),
                      action,
                      gm_sts[i])
