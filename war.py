#amount of cards each have, if one person gets 52 cards then they win, if you win round your count increases by two
computer_card_number = 26
user_card_number = 26

class Player:
    user_name = input("Please type your name here: ")
    print("User Name: " + user_name)

class Card:
    #setting value for each card, so can say if the cards value is higher than the other card you win
    card_value = {
      "1": 1,
      "2": 2,
      "3": 3,
      "4": 4,
      "5": 5,
      "6": 6,
      "7": 7,
      "8": 8,
      "9": 9,
      "10": 10,
      "J": 11,
      "Q": 12,
      "K": 13,
      "A": 14
    }

    print(card_value)

class Deck:
    print("test deck")

class Game:
    print("test game")
