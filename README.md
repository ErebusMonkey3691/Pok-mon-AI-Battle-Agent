# Pok-mon-AI-Battle-Agent
### Heuristic-Based Decision Engines for Competitive 1v1 Singles

## Project Overview
This repository contains a battle agent designed to emulate the decision-making of competitive Pokémon Singles players. Unlike doubles, high-level Singles is defined by **Momentum Management** and **Predictive Switching**. This project implements a weighted heuristic engine that evaluates the board state not just for immediate damage, but for long-term "Win Condition" preservation.

The agent interacts with the Pokémon Showdown environment via the `poke-env` library, aiming to provide a human-like challenge by prioritizing strategic positioning over "Greedy" (max-damage) play.



## Core Features & Methodology
The agent’s "Smarter" logic focuses on three pillars of competitive 1v1 play:

* **Momentum & Switching:** The agent evaluates the "Switch-in Value" of every party member. It identifies if staying in leads to a "Forced Out" scenario and proactively switches to a counter-measure to maintain momentum.
* **Type-Matchup Calculus:** Moves beyond simple "Super Effective" checks. The heuristic weights both offensive pressure and defensive resistance to ensure the agent doesn't lose its "Checks" early in the match.
* **Risk/Reward Weighting:** Accounts for move accuracy and the "Stalling" potential of opponents. It recognizes when a high-power move is too risky compared to a consistent, accurate alternative.

## System Architecture
To ensure a rigorous experimental approach, the project is divided into modular scripts:

* **`agents.py`**: A centralized library containing agent classes (Random, Max-Damage, and Heuristic-based).
* **`benchmarks.py`**: A benchmarking harness used to cross-evaluate agent performance. By running thousands of trials, the system quantifies the "Win Rate Delta" provided by advanced heuristics.

## Technical Challenges
* **Information Scarcity:** Inferring an opponent's set (Items, EVs, and Abilities) through limited turn data—a core component of competitive 1v1.
* **Stochastic States:** Navigating turns where a single "Miss" or "Critical Hit" could shift the entire win-probability of the match.
* **Resource Preservation:** Calculating when it is mathematically better to "Sacrifice" a low-HP Pokémon to gain a "Clean Switch" for a teammate.

## Installation & Usage
1. **Prerequisites:** Python 3.8+ and a local [Pokémon Showdown Server](https://github.com/smogon/pokemon-showdown).
2. **Setup:**
   ```bash
   git clone [https://github.com/yourusername/Pok-mon-AI-Battle-Agent.git](https://github.com/yourusername/Pok-mon-AI-Battle-Agent.git)
   pip install -r requirements.txt
