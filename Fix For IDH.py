#This was done with the help of ChatGPT
import sqlite3
import ast

conn = sqlite3.connect("assistedblackjackdata.db")
c = conn.cursor()

c.execute("""
SELECT rowid, Initial_Dealer_Hand
FROM table_data
""")

for rowid, hand_text in c.fetchall():

    hand = ast.literal_eval(hand_text)


    first_card = [hand[0][0]]

    c.execute("""
    UPDATE table_data
    SET Initial_Dealer_Hand = ?
    WHERE rowid = ?
    """, (str(first_card), rowid))

conn.commit()
conn.close()