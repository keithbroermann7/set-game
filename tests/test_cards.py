from cards import generate_deck, shuffle_deck


def test_generate_deck_has_81_cards():
    deck = generate_deck()
    assert len(deck) == 81


def test_generate_deck_has_no_duplicates():
    deck = generate_deck()
    unique_cards = {(c.number, c.color, c.shape, c.shading) for c in deck}
    assert len(unique_cards) == 81


def test_shuffle_deck_keeps_same_cards():
    deck = generate_deck()
    before = {(c.number, c.color, c.shape, c.shading) for c in deck}

    shuffle_deck(deck)

    after = {(c.number, c.color, c.shape, c.shading) for c in deck}
    assert len(deck) == 81
    assert before == after
