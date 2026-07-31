from cards import Card
from server import app, games

NO_SET_HAND = [
    (3, "green", "squiggle", "empty"),
    (1, "purple", "diamond", "striped"),
    (2, "red", "oval", "striped"),
    (3, "purple", "diamond", "solid"),
    (3, "red", "squiggle", "striped"),
    (3, "green", "diamond", "striped"),
    (3, "red", "oval", "solid"),
    (2, "green", "oval", "solid"),
    (1, "red", "diamond", "solid"),
    (2, "green", "squiggle", "striped"),
    (3, "purple", "oval", "solid"),
    (2, "green", "oval", "empty"),
]


def make_client():
    app.testing = True
    return app.test_client()


def test_new_game_deals_12_cards():
    client = make_client()
    res = client.post("/api/new-game")
    assert res.status_code == 200
    assert len(res.get_json()["hand"]) == 12


def test_claim_no_set_when_a_set_exists():
    client = make_client()
    client.post("/api/new-game")  # a fresh 12-card hand almost always has a set

    res = client.post("/api/claim-no-set")
    data = res.get_json()

    assert data["correct_claim"] is False
    assert data["num_sets"] >= 1


def test_guess_valid_set_replaces_only_the_guessed_positions():
    client = make_client()
    client.post("/api/new-game")

    hand_attrs = [
        (1, "red", "oval", "striped"),  # 0
        (2, "red", "oval", "striped"),  # 1
        (1, "red", "oval", "solid"),  # 2 -- part of the valid set
        (3, "red", "oval", "striped"),  # 3
        (1, "green", "oval", "solid"),  # 4
        (2, "green", "squiggle", "striped"),  # 5 -- part of the valid set
        (2, "purple", "squiggle", "empty"),  # 6
        (3, "green", "diamond", "solid"),  # 7
        (1, "purple", "squiggle", "solid"),  # 8
        (3, "purple", "diamond", "empty"),  # 9 -- part of the valid set
        (2, "green", "diamond", "empty"),  # 10
        (3, "red", "squiggle", "empty"),  # 11
    ]
    with client.session_transaction() as session:
        game_id = session["game_id"]
    games[game_id]["hand"] = [Card(*attrs) for attrs in hand_attrs]

    res = client.post("/api/guess", json={"indices": [2, 5, 9]})
    data = res.get_json()

    assert data["valid"] is True
    result_hand = data["hand"]
    assert len(result_hand) == 12

    for i in [0, 1, 3, 4, 6, 7, 8, 10, 11]:
        actual = result_hand[i]
        assert (actual["number"], actual["color"], actual["shape"], actual["shading"]) == hand_attrs[i]

    for i in [2, 5, 9]:
        actual = result_hand[i]
        assert (actual["number"], actual["color"], actual["shape"], actual["shading"]) != hand_attrs[i]


def test_claim_no_set_when_none_exist_clears_front_row():
    client = make_client()
    client.post("/api/new-game")

    with client.session_transaction() as session:
        game_id = session["game_id"]
    games[game_id]["hand"] = [Card(*attrs) for attrs in NO_SET_HAND]

    res = client.post("/api/claim-no-set")
    data = res.get_json()

    assert data["correct_claim"] is True
    assert len(data["hand"]) == 12
    # the front row (first 3 cards) should no longer match the original no-set hand
    original_front_row = {NO_SET_HAND[0], NO_SET_HAND[1], NO_SET_HAND[2]}
    new_front_row = {
        (c["number"], c["color"], c["shape"], c["shading"]) for c in data["hand"][:3]
    }
    assert new_front_row.isdisjoint(original_front_row)
