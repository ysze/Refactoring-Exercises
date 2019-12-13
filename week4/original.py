import random
from datetime import datetime


class cards():
    def __init__(self, deck=7):  # makes the deck
        klist = ['d'] * 13 + ['c'] * 13 + ['h'] * 13 + ['s'] * 13
        number = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
        keys = list(zip(klist, number))  # keys are made up of the suit and the value
        values = [deck] * 52  # dictionary values are the number of cards
        ddict = dict(zip(keys, values))
        self.ddict = ddict

    def deal(self):  # hands out card
        random.seed(datetime.now())  # generates random seed based on time
        keylist = list(self.ddict.keys())
        rip = random.sample(keylist, 1)  # picks random dictionary value
        cards.remove(self, rip)  # removes card from dicitonary
        return rip

    def checkhand(self, hand):  # checks value of hand
        total = 0
        acecheck = False
        for i in hand:  # adds up value of the cards
            if i[0][1] == 'J' or i[0][1] == 'Q' or i[0][1] == 'K':
                total += 10
            elif i[0][1] == 'A':  # automatically adds 11 if ace
                total += 11
                acecheck = True
            else:
                total += int(i[0][1])
        if acecheck == True and total > 21 or total == 17:  # checks if, when the ace value is 11, it is over 21 it will subtract 10
            total -= 10
        return total

    def checkdeck(self):  # checks how many cards are left
        return (sum(self.ddict.values()))

    def remove(self, victim):  # removes cards from dictionary at the end of round
        self.ddict[victim[0]] -= 1
        if self.ddict[victim[0]] == 0:  # checks if there is anymore cards of that suit and value
            del self.ddict[victim[0]]
