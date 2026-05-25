import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from D_Sto_Auto import data_extract_byt

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

def cum_win_rate_byt():
    cumu_num = 0
    cum = 0
    cum_wn_r = []
    for s in game_status:
        cumu_num += 1
        if s == 1:
            cum += 1
        wr_p = (cum / cumu_num) * 100
        # print(f"{wr_p}%")
        cum_wn_r.append(wr_p)
    return cum_wn_r
# num=100
# sales_volume=np.random.normal(1000,200,num)
# unit_cost=np.random.uniform(5,15,num)
# price=20
# profit=(price-unit_cost)*sales_volume
#
# plt.hist(profit,bins=50,edgecolor='black')
# plt.title("Monte Carlo Simulation:Distribution of Profit")
# plt.xlabel("Profit")
# plt.ylabel("Frequency")
# plt.show()
# print(f"Mean Profit: ${np.mean(profit):,.2f}")
# print(f"5th percentile Profit: ${np.percentile(profit,5):,.2f}")
