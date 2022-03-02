import random
def computer_picky():
    raw_card = ["2", "3", "4", "5", "6", "7", "8", "9", "Jack", "King", "Queen", "Ace"]
    card_suits = [" Hearts", "Diamonds", "Spades", "Clubs"]
    suits = random.choice(card_suits)
    raw = random.choice(raw_card)
    without_s = raw_card[-1]
    removed_s = suits[:-1]
    if raw in without_s:
        print(f"{raw} of {removed_s}")
    else:
        print(f"{raw} of {suits}")

if __name__ == '__main__':
    computer_picky()

card_text = ['ace of spade', 'ace of heart', 'ace of diamond', 'ace of club', 'two of spades', 'two of hearts',
         'two of diamonds', 'two of clubs', 'three of spades', 'three of hearts', 'three of diamonds', 'three of clubs',
         'four of spades', 'four of hearts', 'four of diamonds', 'four of clubs', 'five of spades', 'five of hearts',
         'five of diamonds', 'five of clubs', 'six of spades', 'six of hearts', 'six of diamonds', 'six of clubs',
         'seven of spades', 'seven of hearts', 'seven of diamonds', 'seven of clubs', 'eight of spades',
         'eight of hearts', 'eight of diamonds', 'eight of clubs', 'nine of spades', 'nine of hearts',
         'nine of diamonds', 'nine of clubs', 'ten of spades', 'ten of hearts', 'ten of diamonds', 'ten of clubs',
         'jack of spades', 'jack of hearts', 'jack of diamonds', 'jack of clubs', 'queen of spades', 'queen of hearts',
         'queen of diamonds', 'queen of clubs', 'king of spades', 'king of hearts', 'king of diamonds', 'king of clubs']
card_num = ['ace of spade', 'ace of heart', 'ace of diamond', 'ace of club', '2 of spades', '2 of hearts',
                '2 of diamonds', '2 of clubs', '3 of spades', '3 of hearts', '3 of diamonds', '3 of clubs',
                '4 of spades', '4 of hearts', '4 of diamonds', '4 of clubs', '5 of spades', '5 of hearts',
                '5 of diamonds', '5 of clubs', '6 of spades', '6 of hearts', '6 of diamonds', '6 of clubs',
                '7 of spades', '7 of hearts', '7 of diamonds', '7 of clubs', '8 of spades',
                '8 of hearts', '8 of diamonds', '8 of clubs', '9 of spades', '9 of hearts',
                '9 of diamonds', '9 of clubs', '10 of spades', '10 of hearts', '10 of diamonds', '10 of clubs',
                'jack of spades', 'jack of hearts', 'jack of diamonds', 'jack of clubs', 'queen of spades',
                'queen of hearts',
                'queen of diamonds', 'queen of clubs', 'king of spades', 'king of hearts', 'king of diamonds',
                'king of clubs']
keywords= 'ace of spade' + 'ace of heart' + 'ace of diamond' + 'ace of club' + 'two of spades' + 'two of hearts' + 'two of diamonds' + 'two of clubs' + 'three of spades' + 'three of hearts'+ 'three of diamonds' + 'three of clubs' + 'four of spades' + 'four of hearts' + 'four of diamonds' + 'four of clubs' + 'five of spades' + 'five of hearts' + 'five of diamonds' +'five of clubs' +'six of spades' + 'six of hearts' + 'six of diamonds' + 'six of clubs' + 'seven of spades' + 'seven of hearts' + 'seven of diamonds'+ 'seven of clubs'+ 'eight of spades' +'eight of hearts' + 'eight of diamonds' + 'eight of clubs' + 'nine of spades' + 'nine of hearts' + 'nine of diamonds' + 'nine of clubs' + 'ten of spades' + 'ten of hearts' + 'ten of diamonds' +'ten of clubs' + 'jack of spades' + 'jack of hearts' + 'jack of diamonds' + 'jack of clubs' +'queen of spades' + 'queen of hearts' + 'queen of diamonds' + 'queen of clubs' +'king of spades' + 'king of hearts' + 'king of diamonds'+ 'king of clubs'+ '2 of spades' + '2 of hearts' + '2 of diamonds' + '2 of clubs' + '3 of spades' + '3 of hearts' + '3 of diamonds' + '3 of clubs' + '4 of spades' + '4 of hearts' + '4 of diamonds' + '4 of clubs' + '5 of spades' + '5 of hearts' + '5 of diamonds' + '5 of clubs' + '6 of spades' + '6 of hearts' + '6 of diamonds' + '6 of clubs' + '7 of spades' + '7 of hearts' +'7 of diamonds' + '7 of clubs' + '8 of spades' + '8 of hearts' + '8 of diamonds' + '8 of clubs' + '9 of spades' +'9 of hearts' + '9 of diamonds' + '9 of clubs' + '10 of spades' +'10 of hearts' + '10 of diamonds' + '10 of clubs'





keyword = card_num + card_text

