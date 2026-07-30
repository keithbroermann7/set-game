# Set game — learning project

## About me
I work in finance, not tech. I'm building this project to gain broad,
well-rounded fluency in how a tech/internet-native company actually operates —
the stack, the tools, and the workflows across engineering, data, product, and
ops — so I could be versatile and useful across many functions at a startup or
tech company. This isn't about targeting one role (like PM); it's about
understanding the whole shape of the operation. I'm not trying to become a
proficient hand-coder. Assume no prior coding background — explain jargon the
first time it comes up.

## How I want to work
- I care more about the higher-level workflows, tools, and concepts (git/
  GitHub, testing, APIs, databases, deployment/CI-CD, etc.) than about writing
  code syntax myself — the kind of thing that's easily replaced by tools like
  Claude Code. Optimize explanations for that: what the tool/workflow is, what
  problem it solves, why it's structured the way it is, tradeoffs involved.
- Still explain the concept in plain English before writing code, and don't
  just dump finished code silently — but it's fine for Claude to write the
  actual code; I don't need to hand-write it to learn from this project.
- Feel free to branch into adjacent topics even if it's a tangent from the
  literal next coding step — things like how teams structure code review, how
  on-call/incidents work, build-vs-buy decisions, why data teams and eng teams
  sometimes clash. That connective tissue is often as valuable as the code
  itself, given my goal above.
- I have a rudimentary software engineering background. Actively surface and
  explain terminology as it comes up in our actual work — especially words
  that get thrown around on tech podcasts/news without being explained (e.g.
  "mocking," "CLI," "stdlib," "state," "idempotent," "race condition"). Tie
  the definition to the concrete thing we just did, not an abstract
  dictionary definition. Don't wait for me to ask — flag it proactively.
- Keep steps small. Confirm things are working before moving to the next step.
- When introducing a new tool/concept (e.g. testing, APIs, databases), briefly
  explain what problem it solves before using it.
- Whenever a roadmap item in the Status section below is completed, update
  that section (what's done, what's next) as part of the same commit —
  proactively, without being asked. Keep it accurate; don't let it drift.

## Project goal
Build the card game Set end-to-end, as a vehicle to learn: Python, frontend,
backend/APIs, databases, analytics/event tracking, data warehousing, and
deployment/CI-CD. Full roadmap logic lives in this repo as we build it.

## Status
- Phase 0 (Git/GitHub/VS Code setup): done
- Phase 1 (game logic in Python): in progress
  - `cards.py`: Card class + generate_deck() — done, committed
  - `game.py`: is_valid_set(card1, card2, card3) — done, committed. Checks
    that for each of the 4 attributes (number, color, shape, shading), the
    three cards are either all the same or all different.
  - `game.py`: find_sets(cards) — done, committed. Given a hand of dealt
    cards, uses itertools.combinations to check every group of 3 against
    is_valid_set() and returns the valid ones.
  - `cards.py`: shuffle_deck(deck) — done. Thin wrapper on random.shuffle().
  - `game.py`: deal_hand(deck, count=12) — done. Removes and returns `count`
    cards from the front of the deck (mutates the deck in place).
  - `main.py`: CLI entry point — done. play() deals 12 cards, loops letting
    the player guess 3 card numbers, checks with is_valid_set(), replaces
    correct guesses with fresh cards from the deck, ends when the deck is
    empty and no sets remain. Known simplification: real Set lets you
    request 3 extra cards when the current hand has no valid set — not
    implemented yet.
  - Phase 1 is now functionally playable end-to-end via `python3 main.py`.
  - Next: not yet decided — could be Phase 1 polish (e.g. the "no sets,
    deal 3 more" rule above, or a hint/reveal command), or moving into
    Phase 2 (frontend/backend) per the roadmap in Project goal.

## Tech decisions so far
- Language: Python
- No frontend/backend/DB built yet — those come in later phases.