import pytest

from cards import Card
from game import deal_hand, find_sets, is_valid_set


@pytest.mark.parametrize(
    "card1, card2, card3, expected",
    [
        # All four attributes all-different -> valid
        (
            Card(1, "red", "oval", "solid"),
            Card(2, "green", "diamond", "striped"),
            Card(3, "purple", "squiggle", "empty"),
            True,
        ),
        # All four attributes all-same -> valid
        (
            Card(1, "red", "oval", "solid"),
            Card(1, "red", "oval", "solid"),
            Card(1, "red", "oval", "solid"),
            True,
        ),
        # Number matches on two cards, differs on the third -> invalid
        (
            Card(1, "red", "oval", "solid"),
            Card(1, "green", "diamond", "striped"),
            Card(2, "purple", "squiggle", "empty"),
            False,
        ),
    ],
)
def test_is_valid_set(card1, card2, card3, expected):
    assert is_valid_set(card1, card2, card3) == expected


def test_find_sets_finds_the_one_valid_set_in_a_hand():
    hand = [
        Card(1, "red", "oval", "solid"),
        Card(2, "green", "diamond", "striped"),
        Card(3, "purple", "squiggle", "empty"),  # forms a set with the two above
        Card(1, "red", "oval", "striped"),  # doesn't pair into a set with anything above
    ]

    results = find_sets(hand)

    assert len(results) == 1
    assert set(results[0]) == {hand[0], hand[1], hand[2]}


def test_deal_hand_removes_dealt_cards_from_the_deck():
    deck = [Card(n, "red", "oval", "solid") for n in range(1, 11)]  # 10 fake cards

    hand = deal_hand(deck, 4)

    assert len(hand) == 4
    assert len(deck) == 6
    assert set(hand).isdisjoint(deck)
