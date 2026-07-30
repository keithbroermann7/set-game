from cards import Card


def is_valid_set(card1, card2, card3):
    attributes = ["number", "color", "shape", "shading"]
    for attribute in attributes:
        values = {getattr(card1, attribute), getattr(card2, attribute), getattr(card3, attribute)}
        if len(values) == 2:
            return False
    return True
