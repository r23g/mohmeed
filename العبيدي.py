import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    def __init__(self):
        suits = ['♠️', '♥️', '♦️', '♣️']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal(self, num):
        dealt_cards = self.cards[:num]
        self.cards = self.cards[num:]
        return dealt_cards

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.collected_cards = []

    def play_card(self, table_cards):
        for card in self.hand:
            if any(card.rank == table_card.rank for table_card in table_cards):
                self.hand.remove(card)
                matching_card = next(tc for tc in table_cards if tc.rank == card.rank)
                table_cards.remove(matching_card)
                self.collected_cards.extend([card, matching_card])
                print(f"{self.name} أخذ البطاقة: {card}")
                return
        
        card = self.hand.pop()
        table_cards.append(card)
        print(f"{self.name} لعب البطاقة: {card}")

    def calculate_points(self):
        
        return len(self.collected_cards)

class Game:
    def __init__(self, player_names):
        self.deck = Deck()
        self.players = [Player(name) for name in player_names]
        self.table_cards = self.deck.deal(4)
        for player in self.players:
            player.hand = self.deck.deal(4)

    def play(self):
        print(f"البطاقات على الطاولة: {[str(card) for card in self.table_cards]}")

        while any(player.hand for player in self.players):
            for player in self.players:
                if player.hand:
                    print(f"\nدور {player.name}!")
                    player.play_card(self.table_cards)

        print("\nانتهت اللعبة!")
        print("البطاقات المتبقية على الطاولة:", [str(card) for card in self.table_cards])

        
        for player in self.players:
            points = player.calculate_points()
            print(f"{player.name} جمع {points} نقاط.")


player_names = ["محمد", " علي", "العبيدي","امين"]
game = Game(player_names)
game.play()