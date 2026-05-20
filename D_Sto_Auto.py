import sqlite3

conn = sqlite3.connect('assistedblackjackdata.db')

c = conn.cursor()


def insert_it(shoe_id, round_id, player_id, player_score, bet_amount, total_money, dealer_score, game_action,
              game_status):
    c.execute("""
    INSERT INTO table_data
    (
    Shoe_ID,
    Round_ID,
    Player_ID,
    Player_Score,
    Bet_Amount,
    Total_Money,
    Dealer_Score,
    Game_Action,
    Game_Status
    )
    VALUES
    (?,?,?,?,?,?,?,?,?)""",
              (shoe_id,
               round_id,
               player_id,
               player_score,
               bet_amount,
               total_money,
               dealer_score,
               game_action,
               game_status
               ))
    conn.commit()


def money_check_byt(player_id):
    c.execute("""
        SELECT Total_Money
        FROM table_data
        WHERE Player_ID = ?
        ORDER BY Round_ID DESC
        LIMIT 1
        """, (player_id,))

    result = c.fetchone()

    if result is None:
        return 1000
    return result[0]


def reset_cash():
    return [1000, 1000, 1000]


def shoe_check_byt():
    c.execute("""
    SELECT MAX(Shoe_ID) FROM table_data
    """)
    sh = c.fetchone()
    if sh[0] is None:
        return 1
    return sh[0] + 1


c.execute("""
CREATE TABLE IF NOT EXISTS table_data
    (
    Iteration INTEGER PRIMARY KEY AUTOINCREMENT,
    Shoe_ID INTEGER NOT NULL,
    Round_ID INTEGER NOT NULL,
    Player_ID INTEGER NOT NULL,
    Player_Score INTEGER NOT NULL CHECK(Player_Score >= 0),
    Bet_Amount INTEGER NOT NULL CHECK(Bet_Amount >= 0),
    Total_Money INTEGER NOT NULL,
    Dealer_Score INTEGER NOT NULL CHECK(Dealer_Score >= 0),
    Game_Action TEXT NOT NULL,
    Game_Status INTEGER NOT NULL CHECK(Game_Status IN (-1,0,1))
    )
""")
# CANNOT CHECK GAME ACTION FOR A VIABLE SOLUTION YET.

# Checking the function.
# print(shoe_check_byt())
# ___Hard Reset___:
# c.execute("DROP TABLE IF EXISTS table_data")
