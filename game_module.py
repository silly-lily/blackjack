import deck_module as dm
from collections import OrderedDict
import math
import time

deck = dm.Deck()
BLACKJACK = 21

class Game: 

    def __init__(self):
        
        self.uh = self.User_Hand()
        self.ah = self.AI_Hand()

        self.user_turn()
        time.sleep(1)

        self.ai_turn()
        time.sleep(1)

        print(self.calc_game())
        print('user score: '+str(self.uh.score))
        print('ai score: '+str(self.ah.score))
        
        time.sleep(3)
        for i in range(0,20):
            print()
        
        
    
    def calc_game(self):

        if self.uh.get_status() == 'busted':
            return 'user lost'
        elif self.uh.get_status() == 'blackjack':
            return 'user won'
        elif self.ah.get_status() == 'busted':
            return 'user won'
        elif self.uh.score < self.ah.score:
            return 'user lost'
        elif self.uh.score > self.ah.score:
            return 'user won'
        else:
            return 'tie'

    def user_turn(self):
        
        print(self.uh.to_string())
        print()

        while self.uh.get_status() == 'under' and self.uh.should_hit():
            self.uh.hit()
            print(self.uh.to_string())
            print()
        
        print(self.uh.get_status())
        print()

    def ai_turn(self):
        print(self.ah.to_string())
        print()

        while self.uh.get_status() == 'under' and self.ah.get_status() == 'under' and self.ah.should_hit():
            self.ah.hit()
            print(self.ah.to_string())
            print()

        print(self.ah.get_status())
        print()


    
    class Hand:

        def __init__(self):
            self.cards = []
            self.score = 0

            # All hands start w/ 2 cards
            self.hit()
            self.hit()

        def to_string(self):
            
            h_str = ''

            for c in self.cards:
                h_str+=c.to_string()
                h_str+=', '

            h_str+='\n'
            h_str+=str(self.score)

            return h_str

        def hit(self):

            c = deck.deal()
            self.cards.append(c)
            self.score = self.calc_score()

        def calc_score(self):

            score = 0
            aces = 0 # have 2 diff. values 

            for c in self.cards:
                if c.card_value  == 'ace':
                    aces+=1
                else:
                    score+=dm.Value[c.card_value]

            for ace in range(0,aces):
                if score+max(dm.Value['ace'])+(aces-ace)*min(dm.Value['ace']) > 21:
                    score+=min(dm.Value['ace'])
                else:
                    score+=max(dm.Value['ace'])
            
            return score

        def get_status(self):

            if self.score == BLACKJACK:
                return 'blackjack'
            elif self.score > BLACKJACK:
                return 'busted'
            else:
                return 'under'

    class User_Hand(Hand):

        def __init__(self):
            super().__init__() 

        def to_string(self):

            uh_str = ''
            uh_str+='user hand:\n'

            return uh_str+super().to_string()

        def should_hit(self):

            print('hit? (y/n)')
            ans = input()

            if ans == 'y':
                return True
            elif ans == 'n':
                return False
            else:
                return self.should_hit()

    class AI_Hand(Hand):

        def __init__(self):
            super().__init__() 

        def to_string(self):

            uh_str = ''
            uh_str+='ai hand:\n'

            return uh_str+super().to_string()

        def should_hit(self):

            pred_card_val = 0

            for c in deck.cards:
                if c.card_value == 'ace':
                    pred_card_val+=min(dm.Value[c.card_value])
                else:
                    pred_card_val+=dm.Value[c.card_value]

            pred_card_val = math.ceil(pred_card_val/len(deck.cards))

            if self.score+pred_card_val > BLACKJACK:
                return False
            else:
                return True



Hand_Status = OrderedDict()
Hand_Status['busted'] = -1
Hand_Status['under'] = 0
Hand_Status['blackjack'] = 1

Game_Status = OrderedDict()
Game_Status['user won'] = -1
Game_Status['tie'] = 0
Game_Status['ai won'] = 1