from random import shuffle

class Card:
    def __init__(self, suit, value):
        self.suit = suit.lower()
        self.value = value

    def __repr__(self):
        value = self.value
        if value == 1:
            value = "Ace"
        elif value == 11:
            value = "Jack"
        elif value == 12:
            value = "Queen"
        elif value == 13:
            value = "King"

        return "{} of {}".format(value, self.suit)

class Deck:
    def __init__(self, name=""):
        self.stack = []
        self.name = name

    def handleDeck(self):
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        for suit in suits:
            for value in range(1, 14):
                self.stack.append(Card(suit, value)) 

    def shuffle(self, amount=1):
        for i in range(0, amount):
            shuffle(self.stack)

    def deal(self, amount, stack, position=-1):
        for i in range(0, amount):
            dealt = self.stack[0:1]
            self.stack = self.stack[1:]
            for i in dealt:
                stack.stack.insert(position, i)

    def halfDeck(self, stack1, stack2):
        while len(self.stack) > 0:
                self.deal(1, stack1)
                self.deal(1, stack2)

    def __str__(self):
        spaces = ""
        print(self.name)
        for card in self.stack:
          print(spaces, card)
        return ""

def mainPlay(deck):
    play1 = deck.stack[0].value
    print("Your card:", deck.stack[0])
    play2 = deck.stack[1].value
    print("Computer card:", deck.stack[1])
    if play1 > play2:
        return "play1"
    elif play2 > play1:
        return "play2"
    else:
        return "draw"

deck = Deck()  
deck.handleDeck() 
deck.shuffle(amount=5)  
playerHand = Deck() 
computerHand = Deck()
deck.halfDeck(playerHand, computerHand)

print('The Game of the day is War!')
wait = input("press ENTER to start")  

while True:
    playerHand.shuffle()
    computerHand.shuffle()
    print("-----------------------------------------")
    print()
    print("You have", len(playerHand.stack), "cards")
    deck.stack = []  
    wait = input("press ENTER to play a card")
    print()

    playerHand.deal(1, deck) 
    computerHand.deal(1, deck) 
    while True:
        logic = mainPlay(deck)  
    
        if logic == "play1":
            print("You won this round")
            print("You won the following cards:")
            print(deck)
            deck.deal(len(deck.stack), playerHand)
            break
        elif logic == "play2":
            print("The computer wins this round")
            print("Computer won the following cards:")
            print(deck)
            deck.deal(len(deck.stack), computerHand)
            break

        elif logic == "draw":
            print("AND IT'S A DRAW!")
            wait = input("press ENTER to play a card facedown")
            playerHand.deal(1, deck) 
            wait = input("press ENTER to play a card faceup")
            print()
            playerHand.deal(1, deck, 0)  
            computerHand.deal(1, deck)
            computerHand.deal(1, deck, 0)
            print("Your opponent played two cards")

    if len(playerHand.stack) == 0: 
        print("You have lost!")
        wait = input("the game is over, press ENTER to quit")
        break
    elif len(computerHand.stack) == 0:  
        print("You win this game")
        wait = input("the game is over, press ENTER to quit")
        break
