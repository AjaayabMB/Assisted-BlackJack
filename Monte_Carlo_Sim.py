from random import choice

values = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}


def basic_strategy(play, sco, d_sco):
    for pl in play:
        if "A" not in pl:
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


def dealer_sim(dealer_hand, deck):
    de_hand = dih_building(dealer_hand)
    d_card = choice(deck)
    while score_calc(de_hand) < 17:
        de_hand.append(d_card)
    return de_hand


def dih_building(deck):
    return deck.copy()


def choice_action(ch, deck, player):
    hand = dih_building(player)
    card = choice(deck)
    match ch:
        case "H":
            score_calc(hand)
            if score_calc(hand) <= 21:
                hand.append(card)
            return hand
        case "D":
            hand.append(card)
            return hand
        case "S":
            return hand
    return None


def score_calc(player):
    s = 0
    k = 0
    ace = 0
    for i in player:
        if i[1] == "A":
            ace += 1
        else:
            s += values[i[1]]
        k += 1
    if ace != 0:
        for j in range(0, ace):
            if s > 10:
                s += 1
            else:
                s += 11
    return s


def simulation_mom(deck, player_hand, dealer_hand):
    # count = {
    #     "1": 0,
    #     "2": 0,
    #     "3": 0,
    #     "4": 0,
    #     "5": 0,
    #     "6": 0,
    #     "7": 0,
    #     "8": 0,
    #     "9": 0,
    #     "10": 0,
    # }

    # for i in deck:
    #     if i[1] in ["10", "J", "Q", "K"]:
    #         count["10"] += 1
    #     elif i[1] == "2":
    #         count["2"] += 1
    #     elif i[1] == "3":
    #         count["3"] += 1
    #     elif i[1] == "4":
    #         count["4"] += 1
    #     elif i[1] == "5":
    #         count["5"] += 1
    #     elif i[1] == "6":
    #         count["6"] += 1
    #     elif i[1] == "7":
    #         count["7"] += 1
    #     elif i[1] == "8":
    #         count["8"] += 1
    #     elif i[1] == "9":
    #         count["9"] += 1
    #     elif i[1] == "A":
    #         count["1"] += 1
    ev = {
        "H": 0,
        "S": 0,
        "D": 0
    }
    wins = [0, 0, 0]
    losses = [0, 0, 0]
    draws = [0, 0, 0]
    bol = True
    if (score_calc(player_hand) < 21) or (score_calc(player_hand) == 21 and len(player_hand) > 2):
        for h in range(0, 10000):
            test_h = choice_action("H", deck, player_hand)
            sc_t_h = score_calc(test_h)
            if sc_t_h > 21:
                ev["H"] -= 1
                losses[0] += 1
                continue
            else:
                d_hand = dealer_sim(dealer_hand, deck)
                sc_t_d = score_calc(d_hand)
            while bol:
                test_h = choice_action(basic_strategy(test_h, score_calc(test_h), sc_t_d), deck, test_h)
                bol = basic_strategy(test_h, score_calc(test_h), sc_t_d) not in ["S", None, "D", "SP"]
            sc_t_h = score_calc(test_h)
            if sc_t_h > 21 >= sc_t_d:
                ev["H"] -= 1
                losses[0] += 1
            elif sc_t_h < sc_t_d <= 21:
                ev["H"] -= 1
                losses[0] += 1
            elif sc_t_d > 21 >= sc_t_h:
                ev["H"] += 1
                wins[0] += 1
            elif 21 >= sc_t_h > sc_t_d:
                ev["H"] += 1
                wins[0] += 1
            elif 21 >= sc_t_h == sc_t_d:
                ev["H"] += 0
                draws[0] += 1
        for d in range(0, 10000):
            test_d = choice_action("D", deck, player_hand)
            sc_t_do = score_calc(test_d)
            if sc_t_do > 21:
                ev["D"] -= 1
                losses[2] += 1
                continue
            else:
                d_hand = dealer_sim(dealer_hand, deck)
            sc_t_d = score_calc(d_hand)
            if sc_t_do > 21 >= sc_t_d:
                ev["D"] -= 2
                losses[2] += 1
            elif sc_t_do < sc_t_d <= 21:
                ev["D"] -= 2
                losses[2] += 1
            elif sc_t_d > 21 >= sc_t_do:
                ev["D"] += 2
                wins[2] += 1
            elif 21 >= sc_t_do > sc_t_d:
                ev["D"] += 2
                wins[2] += 1
            elif 21 >= sc_t_do == sc_t_d:
                ev["D"] += 0
                draws[2] += 1
    else:
        ev["H"] = float("-inf")
        ev["D"] = float("-inf")
    for s in range(0, 10000):
        test_s = choice_action("S", deck, player_hand)
        sc_t_s = score_calc(test_s)
        if sc_t_s > 21:
            ev["S"] -= 1
            losses[1] += 1
            continue
        else:
            d_hand = dealer_sim(dealer_hand, deck)
        sc_t_d = score_calc(d_hand)
        if sc_t_s > 21 >= sc_t_d:
            ev["S"] -= 1
            losses[1] += 1
        elif sc_t_s < sc_t_d <= 21:
            ev["S"] -= 1
            losses[1] += 1
        elif sc_t_d > 21 >= sc_t_s:
            ev["S"] += 1
            wins[1] += 1
        elif 21 >= sc_t_s > sc_t_d:
            ev["S"] += 1
            wins[1] += 1
        elif 21 >= sc_t_s == sc_t_d and len(test_s) >= 2:
            ev["S"] += 0
            draws[1] += 1
        elif 21 >= sc_t_s > sc_t_d and len(test_s) == 2:
            ev["S"] += 1
            wins[1] += 1

    final_ev = {
        "H": ev["H"] / 10000,
        "S": ev["S"] / 10000,
        "D": ev["D"] / 10000
    }
    rec_act = max(ev, key=ev.get)
    if rec_act == "H":
        print(f"Recommended action is \n\bHITTING.")
    elif rec_act == "S":
        print(f"Recommended action is \n\bSTANDING.")
    else:
        print(f"Recommended action is \n\bDOUBLING.")
    print(f"\n Final Stats:")
    print(f"\nHIT")
    print(f"Win Rate: {wins[0] / 100:.4f}")
    print(f"Draw Rate: {draws[0] / 100:.4f}")
    print(f"Loss Rate: {losses[0] / 100:.4f}")
    if final_ev["H"] > 0:
        confidence = 100 - (1 - final_ev["H"]) * 50
    elif final_ev["H"] < 0:
        confidence = (1 - final_ev["H"]) * 50
    else:
        confidence = 50
    print(f"Confidence: {confidence:.4f}%")
    print(f"\nSTAND")
    print(f"Win Rate: {wins[1] / 100:.4f}")
    print(f"Draw Rate: {draws[1] / 100:.4f}")
    print(f"Loss Rate: {losses[1] / 100:.4f}")
    if final_ev["S"] > 0:
        confidence = 100 - (1 - final_ev["S"]) * 50
    elif final_ev["S"] < 0:
        confidence = (final_ev["S"] + 1) * 50
    else:
        confidence = 50
    print(f"Confidence: {confidence:.4f}%")
    print(f"\nDOUBLE")
    print(f"Win Rate: {wins[2] / 100:.4f}")
    print(f"Draw Rate: {draws[2] / 100:.4f}")
    print(f"Loss Rate: {losses[2] / 100:.4f}")
    if final_ev["D"] > 0:
        confidence = 100 - (1 - final_ev["D"]) * 50
    elif final_ev["D"] < 0:
        confidence = (1 - final_ev["D"]) * 50
    else:
        confidence = 50
    print(f"Confidence: {confidence:.4f}%")
