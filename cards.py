import random


class Card:
    def __init__(self, number, color, shape, shading):
        self.number = number
        self.color = color
        self.shape = shape
        self.shading = shading

    def __repr__(self):
        return f"Card({self.number}, {self.color}, {self.shape}, {self.shading})"


def generate_deck():
    numbers = [1, 2, 3]
    colors = ["red", "green", "purple"]
    shapes = ["oval", "diamond", "squiggle"]
    shadings = ["solid", "striped", "empty"]

    deck = []
    for number in numbers:
        for color in colors:
            for shape in shapes:
                for shading in shadings:
                    deck.append(Card(number, color, shape, shading))
    return deck


def shuffle_deck(deck):
    random.shuffle(deck)


if __name__ == "__main__":
    deck = generate_deck()
    print(f"Total cards in deck: {len(deck)}")
    print("First 3 cards:")
    for card in deck[:3]:
        print(card)