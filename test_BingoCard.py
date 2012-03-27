#!/usr/bin/env python

from BingoCard import BingoCardFactory, NDFSBingoPlayer

f = BingoCardFactory(size=5, data=range(1,10))
players = [NDFSBingoPlayer(x) for x in f.createBingoCards(10)]

import random
seq = [1,2,3,4,5,6,7,8,9]
random.shuffle(seq)
print seq

print players

print players[0].bingo()

for i in seq:
    [x.mark(i) for x in players]
    print sum([len(x.cards) for x in players])
    print "bingos:", len([x for x in players if x.bingo()])
    
