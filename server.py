import secrets

from flask import Flask, jsonify, request, session

from cards import generate_deck, shuffle_deck
from game import deal_hand, find_sets, is_valid_set

app = Flask(__name__, static_folder="frontend", static_url_path="")
app.secret_key = secrets.token_hex(16)

games = {}


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/api/new-game", methods=["POST"])
def new_game():
    deck = generate_deck()
    shuffle_deck(deck)
    hand = deal_hand(deck, 12)

    game_id = secrets.token_hex(8)
    games[game_id] = {"deck": deck, "hand": hand}
    session["game_id"] = game_id

    return jsonify({"hand": [card.to_dict() for card in hand]})


@app.route("/api/guess", methods=["POST"])
def guess():
    game_id = session.get("game_id")
    game = games.get(game_id)
    if game is None:
        return jsonify({"error": "no active game"}), 400

    hand = game["hand"]
    deck = game["deck"]
    indices = request.get_json(force=True).get("indices", [])

    if len(indices) != 3 or any(i < 0 or i >= len(hand) for i in indices):
        return jsonify({"error": "invalid indices"}), 400

    chosen = [hand[i] for i in indices]
    valid = is_valid_set(*chosen)

    if valid:
        for card in chosen:
            hand.remove(card)
        hand.extend(deal_hand(deck, 3))

    game_over = not find_sets(hand) and not deck

    return jsonify({
        "valid": valid,
        "hand": [card.to_dict() for card in hand],
        "game_over": game_over,
        "cards_left_in_deck": len(deck),
    })


if __name__ == "__main__":
    app.run(debug=True)
