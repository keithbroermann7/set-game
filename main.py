from cards import generate_deck, shuffle_deck
from game import deal_hand, find_sets, is_valid_set


def display_hand(hand):
    for i, card in enumerate(hand, start=1):
        print(f"{i}: {card}")


def play():
    deck = generate_deck()
    shuffle_deck(deck)
    hand = deal_hand(deck, 12)

    print("Welcome to Set! Enter three numbers (e.g. '1 5 9') to guess a set, or 'q' to quit.")

    while True:
        print()
        display_hand(hand)

        if not find_sets(hand) and not deck:
            print("No sets left in the hand and the deck is empty. Game over!")
            break

        guess = input("Your guess: ").strip()
        if guess.lower() == "q":
            print("Thanks for playing!")
            break

        try:
            indices = [int(token) - 1 for token in guess.split()]
            if len(indices) != 3:
                raise ValueError
            chosen = [hand[i] for i in indices]
        except (ValueError, IndexError):
            print("Please enter three valid numbers from the hand.")
            continue

        if is_valid_set(*chosen):
            print("Correct! That's a valid set.")
            for card in chosen:
                hand.remove(card)
            hand.extend(deal_hand(deck, 3))
        else:
            print("Not a valid set. Try again.")


if __name__ == "__main__":
    play()
