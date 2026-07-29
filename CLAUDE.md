# Set game — learning project

## About me
I work in finance, not tech. I'm building this project to learn to code and to
understand software infrastructure well enough to work as a PM or generalist at
a tech company / startup. Assume no prior coding background — explain jargon
the first time it comes up.

## How I want to work
- Explain the concept in plain English FIRST, then write the code together.
- Don't just hand me finished code — walk through the "why" behind each design
  choice, especially anything a PM would need to understand (tradeoffs, why
  something is hard, why it's structured this way).
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