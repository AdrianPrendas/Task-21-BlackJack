
import functools 
import random

VALUES = [1,2,3,4,5,6,7,8,9,10,11,12,13]

KIND = [
    {"kind":"C"},
    {"kind":"D"},
    {"kind":"T"},
    {"kind":"P"},
]

DECK = [{"kind": k["kind"], "value": v} for k in KIND for v in VALUES]

class Player:
    def __init__(self, n):
        self.n = n
        self.hand = []

    def addCard(self, card):
        self.hand.append(card)

    def calculate(self):
        if len(self.hand) < 2:
            return 0
        values = list(map(lambda card: card["value"] ,self.hand))
        return functools.reduce(lambda a,b: a+b, values)

    def getMore(self):
        return True if self.calculate() < 16 else False

    def getTotal(self):
        values = list(map(lambda card: card["value"] ,self.hand))
        return functools.reduce(lambda a,b: a+b, values)

    def __str__(self):
        return f"id:{self.n} =>{self.hand}=> total: {self.getTotal()}"
    



if __name__ == "__main__":
    
    random.shuffle(DECK) #sorting the DECK to get random card

    n = int(input("how many players you want: "))
    
    house = Player("house")
    players = []

    for i in range(n):
        players.append(Player(i))

    while True:
        for i in range(n):
            if players[i].getMore():
                card = DECK.pop()
                print("card: ", card)
                players[i].addCard(card)
        if house.getMore():
            card = DECK.pop()
            print("card: ", card)
            house.addCard(card)

        more = list(map(lambda p: p.getMore(),players))
        more = list(map(lambda s: not s ,more))
        if all(more) and not house.getMore():
            break
    
    print("\n\n")
    print("players")
    for e in players:
        print(e)

    print("\n\n")
    print("house")
    print(house)

    filtering = [p for p in players if p.getTotal() <= 21]
    if house.getTotal() <= 21: 
        filtering.append(house)

    winner = max(filtering, key=lambda p:p.getTotal())


    print("\n\n")
    print("winner :", winner)


    