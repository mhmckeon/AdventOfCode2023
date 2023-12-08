# Day 7
# Part 1
from collections import Counter

input = "input/day7.txt"
with open(input) as f:
    lines = f.read().split("\n")

cards = {}
for line in lines:
    hand, number = line.split(" ")
    cards[hand] = int(number)

high, pair, pair2, kind3, kind4, kind5, fullH = ([] for x in range(7))

cardsKeys = list(cards.keys())
for card in cardsKeys:
    tempCount =dict(Counter(card))

    if len(tempCount) == 5:
        high.append(card)
    elif len(tempCount) == 4:
        pair.append(card)
    elif len(tempCount) == 1:
        kind5.append(card)
    else:
        tempCount= (sorted(list(tempCount.values()),reverse=True))
        if tempCount.count(2) == 2:
            pair2.append(card)
        elif tempCount.count(4) == 1:
            kind4.append(card)
        elif tempCount.count(1) == 2:
            kind3.append(card)
        else:
            fullH.append(card)

cardValue = {
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "T":10,
    "J":11,
    "Q":12,
    "K":13,
    "A":14
    }
    
sor = False
def sortCards(listofCards):
        count = 0
        if  len(listofCards) < 2:
            return listofCards
        while sor == False:
            for cardIndex in range(1,len(listofCards)):
                if count > len(listofCards):
                    return listofCards
                for x in range(5):
                    if cardValue[listofCards[cardIndex-1][x]] < cardValue[listofCards[cardIndex][x]]:
                        count += 1
                        break
                    if cardValue[listofCards[cardIndex-1][x]] > cardValue[listofCards[cardIndex][x]]:
                        listofCards[cardIndex-1], listofCards[cardIndex] = listofCards[cardIndex], listofCards[cardIndex-1]
                        count = 0
                        break

allOutcomes = [high, pair, pair2, kind3, fullH, kind4, kind5]

def solver(allOutcomes):
    total = 0
    cardNum = 1
    for eachItem in allOutcomes:
        sortCards(eachItem)
        for card in eachItem:
            total += (cards[card]*cardNum)
            cardNum += 1
    return total

print("total day 1 Part 1: ", solver(allOutcomes))


# Part 2
high, pair, pair2, kind3, kind4, kind5, fullH = ([] for x in range(7))

cardValue = {
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "T":10,
    "J":1,
    "Q":12,
    "K":13,
    "A":14
    }

cardsKeys = list(cards.keys())
for card in cardsKeys:
    if "J" in card:
        tempCount = dict(Counter(card))
        numOfJ = card.count("J")
        del tempCount["J"]
        if numOfJ == 5:
            kind5.append(card)
            continue
        max_key = max(tempCount, key=tempCount.get)
        tempCount[max_key] += numOfJ
    else:
        tempCount = dict(Counter(card))
    if len(tempCount) == 5:
        high.append(card)
    elif len(tempCount) == 4:
        pair.append(card)
    elif len(tempCount) == 1:
        kind5.append(card)

    else:
        tempCount= (sorted(list(tempCount.values()),reverse=True))
        if tempCount.count(2) == 2:
            pair2.append(card)
        elif tempCount.count(4) == 1:
            kind4.append(card)
        elif tempCount.count(1) == 2:
            kind3.append(card)
        else:
            fullH.append(card)

allOutcomes = [high, pair, pair2, kind3, fullH, kind4, kind5]

print("Part 2 Total:", solver(allOutcomes))
