import random
#amount of cards each have, if one person gets 52 cards then they win, if you win round your count increases by two
computer_card_number = 26
user_card_number = 26
playing = True

class Player:
    user_name = input("Please type your name here: ")
    print("User Name: " + user_name)

#stores card information
class Card:
    #setting value for each card, so can say if the cards value is higher than the other card you win
    #def __init__(self, name, val, suit):
    ##    self.val = val
#        self.suit = suit

    #name_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    #name_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    #suit_list = ["Hearts", "Spades", "Clubs", "Diamonds"]
     card_value = {
       ("1", 1),
       ("2", 2),
       ("3", 3),
       ("4", 4),
       ("5", 5),
       ("6", 6),
       ("7", 7),
       ("8", 8),
       ("9", 9),
       ("10", 10),
       ("J", 11),
       ("Q", 12),
       ("K", 13),
       ("A", 14)
     }
     for key in card_value:
         print("Name " + key[0])
         print(str(key[1]))

    #random_card = random.choice(card_value)
    #random_card_val = random.choice(list(card_value.values()))
    #random_card_key = random.choice(list(card_value.keys()))

    #print(random_card_val)
    #print(random.choice(str(card_value)))
#game functionality
class Game(Card):
    print("test card")
    # while playing == True:
    #     computer_hand = random_card_val
    #     user_hand = random_card_val
    #     if(computer_hand == user_hand):
    #         print("ahh")

        #playing = False

#adds or removes from deck if you win or lose
class Deck:
    print("test Deck")
