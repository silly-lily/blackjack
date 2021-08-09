from collections import OrderedDict
import random
    


class Deck:

    def __init__(self):
        self.cards = []
        self.discarded = []
        
        for s in Suit.keys():
            for v in Value.keys():
                card = self.Card(s,v)
                self.cards.append(card)
                
        random.shuffle(self.cards)  

    def deal(self):
        
        if self.is_empty():
            self.remake_deck()

        card = self.cards.pop(0)
        self.discarded.append(card)
        return card
    
    def is_empty(self):

        if len(self.cards) == 0:
            return True
        else:
            return False

    def remake_deck(self):

        for c in self.discarded():
            self.discarded.remove(c)
            self.cards.append(c)
        
        random.shuffle(self.cards)



    class Card:

        def __init__(self,suit,value):
            self.card_suit = suit
            self.card_value = value

        def to_string(self):
            card_str = ''

            card_str+=self.card_value
            card_str+=' of '
            card_str+=self.card_suit
            card_str+=' '
            
            if self.card_value == 'ace':
                card_str+=str(Value[self.card_value])
            else:
                card_str+='('
                card_str+=str(Value[self.card_value])
                card_str+=')'
            
            return card_str



Suit = OrderedDict()
Suit['hearts'] = 'hearts'
Suit['diamonds'] = 'diamonds'
Suit['spades'] = 'two'
Suit['clubs'] = 'clubs'

Value = OrderedDict()
Value['ace'] = (1,11)
Value['two'] = 2
Value['three'] = 3
Value['four'] = 4
Value['five'] = 5
Value['six'] = 6
Value['seven'] = 7
Value['eight'] = 8
Value['nine'] = 9
Value['ten'] = 10
Value['jack'] = 10
Value['queen'] = 10
Value['king'] = 10