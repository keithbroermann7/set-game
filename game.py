from itertools import combinations

from cards import Card


def is_valid_set(card1, card2, card3):
    attributes = ["number", "color", "shape", "shading"]
    for attribute in attributes:
        values = {getattr(card1, attribute), getattr(card2, attribute), getattr(card3, attribute)}
        if len(values) == 2:
            return False
    return True


def find_sets(cards):
    valid_sets = []
    for card1, card2, card3 in combinations(cards, 3):
        if is_valid_set(card1, card2, card3):
            valid_sets.append((card1, card2, card3))
    return valid_sets
