# Set game — learning project

## About me
I work in finance, not tech. I'm building this project to understand software
infrastructure well enough to work as a PM or generalist at a tech company /
startup — I'm not trying to become a proficient hand-coder. Assume no prior
coding background — explain jargon the first time it comes up.

## How I want to work
- I care more about the higher-level workflows, tools, and concepts (git/
  GitHub, testing, APIs, databases, deployment/CI-CD, etc.) than about writing
  code syntax myself — the kind of thing that's easily replaced by tools like
  Claude Code. Optimize explanations for that: what the tool/workflow is, what
  problem it solves, why it's structured the way it is, tradeoffs a PM would
  care about.
- Still explain the concept in plain English before writing code, and don't
  just dump finished code silently — but it's fine for Claude to write the
  actual code; I don't need to hand-write it to learn from this project.
- Keep steps small. Confirm things are working before moving to the next step.
- When introducing a new tool/concept (e.g. testing, APIs, databases), briefly
  explain what problem it solves before using it.

## Project goal
Build the card game Set end-to-end, as a vehicle to learn: Python, frontend,
backend/APIs, databases, analytics/event tracking, data warehousing, and
deployment/CI-CD. Full roadmap logic lives in this repo as we build it.

## Status
- Phase 0 (Git/GitHub/VS Code setup): done
- Phase 1 (game logic in Python): in progress
  - `cards.py`: Card class + generate_deck() — done, committed
  - Next: write `is_valid_set(card1, card2, card3)` — checks that for each of
    the 4 attributes (number, color, shape, shading), the three cards are
    either all the same or all different.

## Tech decisions so far
- Language: Python
- No frontend/backend/DB built yet — those come in later phases.