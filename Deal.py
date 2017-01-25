#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 19:35:49 2017

@author: caplarn
"""
import scipy
import numpy as np
import matplotlib.pyplot as plt

#ProbabilityOfAceHigh=(scipy.special.binom(12, 4)-10)*(scipy.special.binom(4, 1)**5-4)/(scipy.special.binom(52, 5)
ProbabilityOfAceHigh=(scipy.special.binom(12, 4)-10)*(scipy.special.binom(4, 1)**5-4)/scipy.special.binom(52, 5)
ProbabilityOfOnePair=0.422569
ProbabilityOfTwoPair=0.047539
ProbabilityOfThree=0.021128
ProbabilityOfStraight=0.003925
ProbabilityOfFlush=0.001965
ProbabilityOfFullHouse=0.001441
ProbabilityOfFour=0.000240
ProbabilityOfStraightFlush=0.0000139
ProbabilityOfRoyalFlush=0.00000154
ProbabilityOfNothing=1-ProbabilityOfAceHigh-ProbabilityOfOnePair-ProbabilityOfTwoPair-ProbabilityOfThree-ProbabilityOfStraight-ProbabilityOfFlush-ProbabilityOfFullHouse-ProbabilityOfFour-ProbabilityOfStraightFlush-ProbabilityOfRoyalFlush
ListOfProbabilities=np.array([ProbabilityOfNothing,ProbabilityOfAceHigh,ProbabilityOfOnePair,ProbabilityOfTwoPair,ProbabilityOfThree,ProbabilityOfStraight,ProbabilityOfFlush,ProbabilityOfFullHouse,ProbabilityOfFour,ProbabilityOfStraightFlush,ProbabilityOfRoyalFlush])



def rake7(Jackpot,input):
    JackpotPrize=0.25*500+0.125*1000+0.125*2000+0.125*3000+0.125*4000+0.125*5000+0.125*Jackpot*0.5
    if input==7:

        ListOfPrizes7=np.array([0,0.01,0.02,0.07,0.25,0.50,1,5,30,250,JackpotPrize])
        return np.dot(ListOfProbabilities,ListOfPrizes7)
    else:
        ListOfPrizes70=np.array([0,0,0.1,0.7,3,10,25,75,300,JackpotPrize,JackpotPrize])
        return np.dot(ListOfProbabilities,ListOfPrizes70)

rake7 = np.vectorize(rake7, otypes=[np.float])
        
print(rake7(350000,7))        

xaxis = np.linspace(0, 500000, 10000)
result7 = rake7(xaxis,7)
result70 = rake7(xaxis,70)

plt.plot(xaxis,result7)
plt.plot(xaxis,result70)