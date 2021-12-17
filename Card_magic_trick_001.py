import random

raw_card = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "Jack", "King", "Queen", "Ace"]
card_suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

suits = random.choice(card_suits)
raw = random.choice(raw_card)

without_s = raw_card[:1]
removed_s = suits[:-1]
if raw in without_s:

    print(f"{raw} of {removed_s}")

else:

    print(f"{raw} of {suits}")
