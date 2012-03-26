#!/usr/bin/env python

class GridBox():
    def __init__(self, data=None, loc=0):
        self.mark = False
        self.data = data
        self.loc = loc


from copy import deepcopy
        
class BingoCard():
    """
    A single bingo card
    """
    def __init__(self, size=5, data=range(1,50)):
        self.size = size
        self.card = [GridBox(item) 
                     for (_,item) 
                     in zip(xrange(size*size),data)]
        
    def markLoc(self, x, y):
        self.card[x + y*self.size].mark = True
    
    def match(self, item):
        return [x for x in self.card if x.data == item]
    
    def mark(self, item):
        def m(item):
            m.mark = True
        [m(x) for x in self.match(item)]
    
    def multiplicativeMark(self, item):
        """ Makes new card[s] """
        result = list()
        for loc in  [x.loc for x in self.match(item) if not x.mark]:
            result.append(deepcopy(self))
            result[-1].card[loc] = True
        return result
        
    def bingo(self):
        for i in xrange(self.size):
            start  = i * self.size
            end    = i * self.size + self.size
            horiz  = self.card[start:end]
            vert   = self.card[i::self.size]
            if all([x.mark for x in horiz]):
                return True
            if all([x.mark for x in vert]):
                return True
        return False
    
    def __str__(self):
        result = ""
        for j in xrange(self.size):
            for i in xrange(self.size):
                result += str(self.card[i + j*self.size])
            result += "\n"
        return result

    
class NonDeterministicFiniteStateBingoPlayer():
    """
    Given a bingo card with repeats, makes all possible choices
    simultaneously. Accomplishes this task by multiplying his card.
    """
    def __init__(self, card):
        self.cards = [card]
    
    def bingo(self):
        return any([card.bingo() for card in self.cards])

    def bingos(self):
        return [x for x in self.cards if x.bingo()]
    
    def mark(self, item):
        newCards = list()
        for card in self.cards:
            newCards += card.multiplicativeMark(item)
        self.cards = list(set(newCards))
    

from random import Random
from math import ceil

class BingoCardFactory():
    """
    Generates reproduceable random bingo cards
    """
    def __init__(self, seed=0, size=5, data=range(1,49)):
        self.size = size
        self.data = deepcopy(data)
        self.rng = Random()
        self.rng.seed(seed)

    def createBingoCard(self):
        data = deepcopy(self.data) * int(ceil( len(self.data) / float(self.size*self.size)))
        self.rng.shuffle(data)
        return BingoCard(self.size, data)

    def createBingoCards(self, num=10):
        return [self.createBingoCard() for i in xrange(num)]
