#give each player a random card, if the card value is higher than the other persons then lower the count of loser by two and incease winner by two, when one person has 0 or less they lose, then implement tie system
#instead of you say the user_name
#seperate in classes
from threading import Thread, Event
import time
import random
#amount of cards each have, if one person gets 52 cards then they win, if you win round your count increases by two
computer_card_number = 26
computer_card_number_str = str(computer_card_number)

user_card_number = 26
user_card_number_str = str(user_card_number)
playing = True
i = 0

#stores card information
class Game:
    #setting value for each card, so can say if the cards value is higher than the other card you win
    #def __init__(self, name, val):
    ##    self.val = val
    user_name = input("Please type your name here: ")
    print("User Name: " + user_name)
    while playing == True:
        name_list_player = random.choice(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
        name_list_player_str = str(name_list_player)
        if(name_list_player_str == "11"):
            name_list_player_str = "J"
        elif(name_list_player_str == "12"):
            name_list_player_str = "Q"
        elif(name_list_player_str == "13"):
            name_list_player_str = "K"
        elif(name_list_player_str == "14"):
            name_list_player_str = "A"

        name_list_computer = random.choice(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
        name_list_computer_str = str(name_list_computer)

        if(name_list_computer_str == "11"):
            name_list_computer_str = "J"
        elif(name_list_computer_str == "12"):
            name_list_computer_str = "Q"
        elif(name_list_computer_str == "13"):
            name_list_computer_str = "K"
        elif(name_list_computer_str == "14"):
            name_list_computer_str = "A"

        if(name_list_player > name_list_computer):
            user_card_number = user_card_number + 1
            computer_card_number = computer_card_number - 1

            print(user_name + " won this hand! "  + user_name + "'s " + name_list_player_str + " card was higher than the computer's " + name_list_computer_str + " card")
            print(user_name + " currently has " + str(user_card_number) + " cards")
            print("The computer currently has " + str(computer_card_number) + " cards")
        elif(name_list_player < name_list_computer):
            user_card_number = user_card_number - 1
            computer_card_number = computer_card_number + 1

            print(user_name + " lost this hand! " + user_name + "'s " + name_list_player_str + " card was lower than the computer's " + name_list_computer_str + " card")
            print(user_name + " currently has " + str(user_card_number) + " cards")
            print("The computer currently has " + str(computer_card_number) + " cards")
        else:
            print("there was a tie!")
            name_list_player_tie = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
            name_list_player_tie_str = str(name_list_player_tie)
            if(name_list_player_tie_str == "11"):
                name_list_player_tie_str = "J"
            elif(name_list_player_tie_str == "12"):
                name_list_player_tie_str = "Q"
            elif(name_list_player_tie_str == "13"):
                name_list_player_tie_str = "K"
            elif(name_list_player_tie_str == "14"):
                name_list_player_tie_str = "A"

            name_list_computer_tie = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
            name_list_computer_tie_str = str(name_list_computer_tie)
            if(name_list_computer_tie_str == "11"):
                name_list_computer_tie_str = "J"
            elif(name_list_computer_tie_str == "12"):
                name_list_computer_tie_str = "Q"
            elif(name_list_computer_tie_str == "13"):
                name_list_computer_tie_str = "K"
            elif(name_list_computer_tie_str == "14"):
                name_list_computer_tie_str = "A"

            if(name_list_player_tie > name_list_computer_tie):
                user_card_number = user_card_number + 3
                computer_card_number = computer_card_number - 3

                print(user_name + " won this hand! " + user_name + "'s " + name_list_player_tie_str + " card was higher than the computer's " + name_list_computer_tie_str + " card")
                print(user_name + " currently has " + str(user_card_number) + " cards")
                print("The computer currently has " + str(computer_card_number) + " cards")
            elif(name_list_player_tie < name_list_computer_tie):
                user_card_number = user_card_number - 3
                computer_card_number = computer_card_number + 3

                print(user_name + " lost this hand! " + user_name + "'s " + name_list_player_tie_str + " card was lower than the computer's " + name_list_computer_tie_str + " card")
                print(user_name + " currently has " + str(user_card_number) + " cards")
                print("The computer currently has " + str(computer_card_number) + " cards")

        if(computer_card_number < 1):
            print(user_name + " WINS :)")
            playing = False
        elif(user_card_number < 1):
            print(user_name + " LOSES :(")
            playing = False

    #name_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
     # card_value = {
     #   ("1", 1),
     #   ("2", 2),
     #   ("3", 3),
     #   ("4", 4),
     #   ("5", 5),
     #   ("6", 6),
     #   ("7", 7),
     #   ("8", 8),
     #   ("9", 9),
     #   ("10", 10),
     #   ("J", 11),
     #   ("Q", 12),
     #   ("K", 13),
     #   ("A", 14)
     # }
     # for key in card_value:
     #     name_and_val = random.choice(key)
     #     name = random.choice(key[0])
     #     value = key[1]
     #
     # name_and_val = random.choice(card_value)
     # print(name_and_val)

    #random_card = random.choice(card_value)
    #random_card_val = random.choice(list(card_value.values()))
    #random_card_key = random.choice(list(card_value.keys()))

    #print(random_card_val)
    #print(random.choice(str(card_value)))
#game functionality

#adds or removes from deck if you win or lose
