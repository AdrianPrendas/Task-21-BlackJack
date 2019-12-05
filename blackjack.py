
import functools 

VALUES = [1,2,3,4,5,6,7,8,9,10,11,12,13]

KIND = [
{"kind":"C"},
{"kind":"D"},
{"kind":"T"},
{"kind":"P"},
]

DECK = [
    {"kind": k["kind"], "value": v} for k in KIND for v in VALUES
]


#for e in DECK:
#        print(e)
#    print(len(DECK))

class Player:
    def __init__(self, n):
        self.n = n
        self.hand = []

    def getCard(self, card):
        self.hand.append(card)

    def calculate(self):
        if len(self.hand) < 2:
            return 0
        return functools.reduce(lambda a,b: a["value"]+b["value"], self.hand)

    def getMore(self):
        return True if self.calculate() < 16 else False

    def __str__(self):
        return f"{self.hand}"
    
        




if __name__ == "__main__":
    n = input("how many players you want: ")
    n = int(n)
    players = []
    house = Player(666)


    #init players
    for i in range(n):
        players.append(Player(i))


    while True:
        for i in range(n):
            if players[i].getMore():
                cart = DECK.pop()
                print("cart: ", cart)
                players[i].getCard(cart)
        if house.getMore():
            cart = DECK.pop()
            print("cart: ", cart)
            house.getCard(cart)

        more = list(map(lambda p: p.getMore(),players))
        more = list(map(lambda s: not s ,more))
        if all(more) and not house.getMore():
            break
    
    print("players")
    for e in players:
        print(e)

    print("\n\n")
    print("house")
    print(house)

        
        
        
            




    #p = Player(1)
    #p.getCard(DECK[len(DECK)-1])
    #p.getCard(DECK[len(DECK)-2])
    #print(p.getMore())

    

    