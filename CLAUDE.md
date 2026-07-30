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
  - Next: not yet decided — options include dealing/shuffling logic (deal 12
    cards from a shuffled deck, the realistic entry point for actually
    playing), or a simple CLI loop to play-test the game end-to-end.

## Tech decisions so far
- Language: Python
- No frontend/backend/DB built yet — those come in later phases.