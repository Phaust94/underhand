# every card in-game

# basic class for the cards; order determines how a card is shuffled into the deck, options are the displayed options:
# the text is the description of the option; the first list in an option is what needs to be given, ordered by:
# [relic, money, cultist, food, suspicion, cultists/prisoners]; the second list is what is taken, ordered by:
# [relic, money, cultist, food, suspicion, death, win] where death is a game over and win is a win; the final list is
# extra cards put into the deck for choosing the option (the 3 numbers before the insert determine how many of those
# cards should be put in; the number at the end is for foresight (0 is none, 1 is foresight, 2 is foresight with
# discard); identifier is just the card id; dupelimit is how many of the same card can be in the deck, these will
# usually be 1 or 999; edit: we have to put '0o' in front of any number for inserts because we might not have a 3 digit
# number insert and python WILL return an error if we have 0s in front of ints without '0o'

class Card(object):
    def __init__(self, identifier=0, order='card', option1=None, option2=None, option3=None, dupelimit=999):
        self.identifier = identifier
        self.order = order
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.dupelimit = dupelimit

        if option1 is None:
            option1 = ['Death', [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, False, ''], ['0o020 wrath', '0o001 necro'], 0]
        if option2 is None:
            option2 = ['Curses', [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, False, ''],
                       ['0o009 necro', '0o001 RhybaxxEvent2'], 1]
        if option3 is None:
            option3 = ['Exped', [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, False, ''],
                       ['0o005 wrath', '0o021 RhybaxxEvent2'], 2]


class TravelingSalesperson(Card):
    def __init__(self):
        super().__init__()
        self.identifier = 1
        self.order = 'card'
        self.option1 = ['Buy Supplies', [0, 2, 0, 0, 0, 0], [0, 0, 0, 1, 0, False, ''], [], 0]
        self.option2 = ['Sell Supplies', [0, 0, 0, 2, 0, 0], [0, 1, 0, 0, 0, False, ''], [], 0]
        self.option3 = ['Decline to Trade', [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, False, ''], [], 0]
