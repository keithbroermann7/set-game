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

Concretely, I'm evaluating roles like "Deployment Strategist" / "AI
Strategist" — customer- and business-facing roles embedded with enterprise
clients, bridging what customers need with what product/engineering teams
build, requiring product fluency (no coding) but real comfort with AI
concepts and the modern agentic AI stack. Given that, weight these a bit
higher when relevant, beyond generic full-stack breadth:
- Evals, model validation, and model behavior — distinct from the
  deterministic software testing we've done (pytest checks "is this
  correct?"; evals are about judging AI output where there's often no single
  right answer). Worth covering as its own topic, not folded into testing.
- The agentic AI tooling landscape (Claude Code, Cowork, Cursor, Lovable,
  Zapier/n8n, etc.) — note explicitly when something we're doing (like
  directing Claude Code to build this project) is itself real experience
  with this category of tool, and stay ready to explain how adjacent tools
  in that landscape relate/compare, even ones we're not using directly here.
- Enterprise deployment / B2B SaaS concepts, when we reach the deployment
  phase of the roadmap — treat that phase as high-value, not a formality.

## How I want to work
- STANDING PRIORITY, crystal clear, applies for the whole life of this
  project: as we keep building, keep teaching me the fundamental concepts of
  technology/software/the stack more broadly — not a fixed list (server,
  HTTP, and data center are just examples of the kind of thing, not the
  whole scope), but whatever foundational concept is actually relevant to
  whatever part of the roadmap we're working on at the time. Always tie each
  one back to *why the tech stack is structured the way it is today* (what
  problem it solved, what came before it, why it won out). This isn't a
  phase-one-only thing; it should continue at every step, including deep
  dives (see below), for as long as we're building this.
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
- I have a rudimentary software engineering background and I'm intentionally
  "vibe coding" this project (having Claude write the code rather than
  learning to write it myself). I do NOT want to end up with blind spots as
  a result — I want to understand how code is written, organized, tested,
  and discussed at roughly the level a working engineer takes for granted,
  even though I'm not the one typing it. Two layers to cover, proactively,
  without me having to ask:
  1. Terminology — words that get thrown around on tech podcasts/news
     without being explained (e.g. "mocking," "CLI," "stdlib," "state,"
     "idempotent," "race condition").
  2. Implicit practices/conventions — things a working engineer does
     automatically and would never think to explain because it's second
     nature to them, but that are real blind spots for someone who has only
     ever seen AI-generated code appear (e.g. why/when real projects have an
     automated test suite instead of one-off manual checks, what a
     virtual environment is and why it exists, what code review normally
     catches, what CI/CD does, dev vs. staging vs. prod environments, why
     dependency versions get pinned). Point these out when they're actually
     relevant to what we're doing, not as an abstract lecture — and call out
     explicitly when something we're doing is a shortcut/simplification a
     real team wouldn't take, so I know it's there.
  Keep it concept-level: why something exists, what problem it solves, what
  breaks without it, what blind spot it closes. Do NOT narrate mechanics or
  implementation details (e.g. don't explain command-line workarounds, don't
  restate "I ran X and it did Y" when the tool call already shows that).
  Pick the 1-2 highest-value teaching moments per chunk of work, not
  everything possible — brief and selective beats exhaustive.
  When a genuinely significant concept comes up (e.g. HTTP, databases,
  containers), give the short version, then explicitly ask if I want to go
  deeper (history, why it was invented, why it matters today) — I enjoy that
  context a lot and want deep dives available throughout, not just early on.
  Don't dump it unprompted, but don't assume I don't want it either — just
  ask. Log completed deep dives in "Concepts covered" below so future
  sessions build on them rather than re-explaining from zero — but I don't
  mind overlap/repetition when it comes up again, since repetition helps me
  actually learn it. Feel free to reference or briefly recap a past deep
  dive when a new topic connects to it.
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
  - Testing: `venv/` (virtual environment, gitignored) + `requirements.txt`
    (pinned deps: pytest and its transitive dependencies) + `tests/`
    (test_cards.py, test_game.py — 8 tests, all passing) + `conftest.py` at
    repo root (empty; makes top-level modules importable from tests/). Run
    with `venv/bin/pytest -v` (or `source venv/bin/activate && pytest -v`).
  - Phase 1 complete.
- Phase 2 (frontend + backend API): in progress
  - `server.py`: Flask backend. POST /api/new-game deals a hand and starts a
    session (signed cookie holding a game_id; actual deck/hand state lives
    server-side in an in-memory `games` dict keyed by that id). POST
    /api/guess validates 3 chosen indices with is_valid_set(), replaces
    correct guesses via deal_hand(), returns updated hand as JSON.
  - `cards.py`: added Card.to_dict() to serialize a card to JSON.
  - `frontend/index.html`: static single-file frontend (HTML/CSS/JS, no
    build step). Renders 12 cards as SVG (shape/color/shading/number drawn
    to spec), click 3 to guess, calls the API via fetch, re-renders on
    response. Verified end-to-end in-browser.
  - Known simplifications (real team wouldn't ship these): `secret_key` is
    randomly regenerated on every server restart, silently invalidating all
    active sessions; `games` dict is in-memory only — a restart wipes every
    in-progress game (a database/session-store would fix both, later
    roadmap phase); card `<div>`s aren't real `<button>`s, so they're not
    keyboard- or screen-reader-accessible.
  - To run locally: `venv/bin/python3 server.py`, then visit
    http://127.0.0.1:5000/
  - "No sets on the board" button — done. POST /api/claim-no-set: if the
    board truly has no valid set, clears + refills the front row (first 3
    cards, board is a 3-per-row x 4-row grid so this matches a real deal
    batch) and reports it; if a set does exist, no state change, just
    reports how many sets are actually there. No penalty for a wrong claim.
  - `tests/test_server.py`: added, using Flask's test client (in-process,
    no real server needed) — covers new-game, guessing (including that a
    correct guess replaces only the guessed positions, see below), claiming
    no-set when a set exists, and claiming no-set correctly (verified
    against a real 12-card no-set hand found by brute-force search). 12
    tests total, all passing.
  - Fixed: a correct guess used to remove matched cards by identity and
    append replacements at the end, which silently reshuffled every other
    card's position. Now replaces in place at the exact guessed indices
    (and shrinks the hand instead of leaving stale cards if the deck runs
    out mid-guess) — matches "No sets" front-row replacement's approach.
  - Next: not yet decided — could be Phase 2 polish (accessibility fix
    above, visual polish), or moving into later roadmap phases (database,
    deployment/CI-CD).

## Concepts covered (deep dives)
Running log so future sessions build on these instead of re-explaining from
scratch. Repetition/overlap on request is welcome, not a problem.
- Git basics: commit vs. push, local vs. remote (GitHub), working tree states.
- Testing: mocking/test doubles, deterministic seeds, pytest conventions
  (test discovery, assert, parametrize), why automated test suites beat
  one-off manual checks, CI (what it is, why it exists).
- Python packaging: virtual environments (what problem they solve),
  requirements.txt and dependency pinning, stdlib vs. third-party packages,
  .gitignore and regenerable artifacts (__pycache__, .pytest_cache, venv/).
- State & mutation: mutating in place vs. returning a new value, what
  "state" means.
- HTTP: what it is, full history (Tim Berners-Lee/CERN 1989-91, HTTP 0.9
  through HTTP/3), why it's stateless and what that trade-off bought, status
  codes/methods at a glance.
- Client-server model: mainframes/dumb terminals -> PCs -> client-server
  split; sessions/cookies as the fix for statelessness.
- Servers, data centers, and cloud computing: what a "server" means (role
  vs. machine), physical data centers, cloud providers renting virtual
  machines, what "serverless" is.
- DNS: how a domain name resolves to an IP address, registrars/ICANN.
- APIs as a contract between frontend and backend; CLI vs. GUI vs. API.

## Tech decisions so far
- Language: Python
- No frontend/backend/DB built yet — those come in later phases.