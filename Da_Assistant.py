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
    initial_player_data = []
    player_hand_data = []
    player_score_data = []
    initial_dealer_data = []
    dealer_hand_data = []
    dealer_score_data = []
    game_action_data = []
    game_status_data = []
    for i in data:
        b = 0
        for j in i:
            match b:
                case 4:
                    initial_player_data.append(j)
                case 5:
                    player_hand_data.append(j)
                case 6:
                    player_score_data.append(j)
                case 9:
                    initial_dealer_data.append(j)
                case 10:
                    dealer_hand_data.append(j)
                case 11:
                    dealer_score_data.append(j)
                case 12:
                    game_action_data.append(j)
                case 13:
                    game_status_data.append(j)
            b += 1
    return initial_player_data, player_hand_data, player_score_data, initial_dealer_data, dealer_hand_data, dealer_score_data, game_action_data, game_status_data


def sorting_cards(input_cards):
    sorted_cards = sorted(input_cards, key=lambda card: sorting_order[card[1]])
    return sorted_cards


def assist_cc_byt(deck, pl_score):
    v_op = []
    v_sco = []
    tot_perc = 0.0
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
    print("The valid options are:", v_sco_sorted)
    for v in v_sco_sorted:
        dup = 1
        for dec in range(0, len(deck)):
            if v == deck[dec][1]:
                dup += 1
        perc = dup / len(deck) * 100
        print(f"{v} can show up {perc:.2f}% of the time with the next hit.")
        tot_perc += perc
    if tot_perc < 100:
        if tot_perc >= 60:
            print("You have a pretty good chance at winning this.")
        else:
            print("I'd recommend not hitting.")
        print(f"Successful hit chance is {tot_perc:.2f}% with the next hit.")
    else:
        print(f"You are guaranteed to not bust with the next hit.")


def assist_inherit_byt(p_hand, d_hand):
    iph_data, ph_data, ps_data, id_data, dh_data, ds_data, ga_data, gs_data = player_data_byt()
    poss_mo = []
    res_hand = []
    res_d_hand = []
    res_p_score = []
    res_d_score = []
    if len(p_hand) == 2:
        for i in range(0, len(gs_data)):
            if gs_data[i] == 1:
                if iph_data[i] == str(p_hand) and id_data[i] == str(d_hand):
                    poss_mo.append(ga_data[i])
                    res_hand.append(ph_data[i])
                    res_d_hand.append(dh_data[i])
                    res_p_score.append(ps_data[i])
                    res_d_score.append(ds_data[i])
    if not poss_mo or not res_hand or not res_d_hand:
        print("No results found.")
    else:
        print(len(poss_mo), "results found.")
        print(
            f"{"S.No.":<7} | {"Possible Moves":<20} | {"Result Hand in the instance":<53} | {"Resulting Player Score":<15} | {"Result Dealer Hand in the instance":<55} | {"Resulting Dealer Score":<15}")
        for i in range(0, len(poss_mo)):
            print(f"{"-" * 7} | {"-" * 20} | {"-" * 53} | {"-" * 22} | {"-" * 55} | {"-" * 22}")
            print(
                f"{i + 1:<7} | {poss_mo[i]:<20} | {res_hand[i]:<53} | {" ":<10} {res_p_score[i]:<12} | {res_d_hand[i]:<55} | {" ":<10} {res_d_score[i]:<12}")
        print("-" * 195)
