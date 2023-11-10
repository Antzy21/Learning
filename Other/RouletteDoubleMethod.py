import random

def spin(bet):
    if random.randint(0,1):
        return bet*2
    else:
        return 0

def rounds(Capital, pGain = 10):
    bet = 1
    initialCapital = Capital
    while Capital < initialCapital*(1+pGain/100):
        #print("Bet: ",bet," Capital: ",C)
        spinResult = spin(bet)
        if Capital < bet:
            return(Capital)
        else:
            Capital += -bet
        if spinResult != 0:
            Capital += spinResult
            bet = 1
        else:
            bet = bet*2
    return(Capital)

def iteration(Capital, percentGain, i = 1000):
    failures = 0
    successes = 0
    for x in range(0, i):
        turn = rounds(Capital, percentGain)
        if turn < Capital:
            failures += 1
        else:
            successes += 1
    return(successes/i)

Capital = 100
percentGainTarget = 20
averageSuccessRate = 0
for x in range(1000):
    averageSuccessRate += iteration(Capital, percentGainTarget)
averageSuccessRate = round(averageSuccessRate, 3)
print(averageSuccessRate,"%")
