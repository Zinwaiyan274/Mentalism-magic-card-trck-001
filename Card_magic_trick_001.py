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

    
    
    import speech_recognition as sr

card = ['ace of spade','ace of heart','ace of diamond','ace of club','two of spades','two of hearts','two of diamonds','two of clubs','three of spades','three of hearts','three of diamonds','three of clubs','four of spades','four of hearts','four of diamonds','four of clubs','five of spades','five of hearts','five of diamonds','five of clubs','six of spades','six of hearts','six of diamonds','six of clubs','seven of spades','seven of hearts','seven of diamonds','seven of clubs','eight of spades','eight of hearts','eight of diamonds','eight of clubs','nine of spades','nine of hearts','nine of diamonds','nine of clubs','ten of spades','ten of hearts','ten of diamonds','ten of clubs','jack of spades','jack of hearts','jack of diamonds','jack of clubs','queen of spades','queen of hearts','queen of diamonds','queen of clubs','king of spades','king of hearts','king of diamonds','king of clubs']

keyword = card


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)

    except:
        print("Sorry could not recognize what you said")
# text = str(text).lower()

print(text)


#
# if text in card:
#     print(f"volia! keyword is >>>{card}<<<< and you said >>>>{text}<<<<<")
# else:
#     ("Dammm")

# ___________________Not done yet_____________________





















































































































