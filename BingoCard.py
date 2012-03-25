#!/usr/bin/env python

class GridBox():
    def __init__(self, data=None):
        self.mark = False
        self.data = data


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
    
    def mark(self, item):
        for box in self.card:
            if item == self.card.data:
                box.mark = True
    
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


from random import Random
from copy import deepcopy
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
