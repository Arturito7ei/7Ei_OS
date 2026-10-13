# Silver Board Protocol

Consultation protocol, not a department and not a debate club. 7MAN convenes it for 777 Gates; any agent may convene it for a hard call that needs more than one archetype.

**Product repo (room, roster, skill):** [Arturito7ei/silver-board](https://github.com/Arturito7ei/silver-board) — private. Do not reimplement seats inside 7Ei_OS or Mission Control.

## What it is

An intelligence field of 50+ figures across six archetypes, chaired with Ray Dalio's method (radical truth, radical transparency, pain + reflection = progress). Charter Art. 1: it **speaks with one voice after resolving contradictions**. The output is a **Signal** (advice). Human override is absolute (Precedence 02).

It is never R or A on the org chart (vault `Company/Departments.md`, `Company/RACI-and-Task-Funnel.md`).

## When to convene

- 777 Venture Gate scoring (vault `Company/777-Venture-Gate.md`)
- Capital allocation, strategic pivot, partnership, or any decision where single-archetype thinking is insufficient (Charter Art. 5)

Do not convene for routine craft (7DEV architecture, 7OPS patch choice). That is department work.

## How (runtime)

1. Clone or open `Arturito7ei/silver-board`.
2. `npm start` → http://localhost:7770 (optional viewer; binds to 127.0.0.1).
3. In Claude Code in that repo: `/silver-board <decision>` or `/silver-board --mode 777-gate <candidate>`.
4. Ship the Signal in the originating channel. Cite `signal.md`. Do not present it as Thierry's decision.

Hard constraints (P01–P03) are pass/fail before any score. A fail is `DECLINE` and escalates 7LEX → Thierry.

## What does not belong here

The Node room, advisor brains, and session files stay in `silver-board`. This OS file is the pointer plus the rules every agent must not violate: one voice, not a roast; local default; no standing agent per advisor.
