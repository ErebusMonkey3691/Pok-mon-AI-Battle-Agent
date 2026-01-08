# Pok-mon-AI-Battle-Agent
### Heuristic-Based Strategic Modeling in 1v1 Competitive Singles

## Project Overview
This project features an autonomous battle agent developed to navigate the strategic complexities of competitive Pokémon Singles. Utilizing the `poke-env` library, the agent implements a custom decision engine that moves beyond simple "Greedy" algorithms. It incorporates statistical estimation and damage-calculus to emulate the predictive reasoning used by high-level players.



## Agent Logic & Architecture
The repository evaluates three distinct tiers of agent intelligence:

* **`MaxDamagePlayer` (The Baseline)**: A greedy agent that selects moves based solely on raw Base Power, failing to account for type resistances or defensive stats.
* **`SmarterGuy` (The Heuristic Engine)**: My primary contribution. This agent utilizes several sophisticated sub-modules to evaluate the board state:
    * **Statistical Inference**: Since opponent stats are hidden, the agent employs `hpCalc` and `defence_estimate` to approximate the target's HP and defensive bulk based on level and base species data.
    * **Damage Calculus (`damage_calc`)**: A reconstructed version of the Pokémon damage formula that accounts for STAB (Same Type Attack Bonus), Burn status, type multipliers, and even "low-roll" random variance to ensure conservative, reliable decision-making.
    * **KO-Priority Logic**: Before evaluating general moves, the agent checks if any available move is a guaranteed Knock Out (KO) based on its estimated damage, ensuring it never misses an opportunity to secure a kill.
    * **STAB-Preference Algorithm**: A filtering system that prioritizes moves with STAB bonuses when multiple super-effective or neutral options exist.

[Smarter Guy Decision Tree](https://github.com/ErebusMonkey3691/Pok-mon-AI-Battle-Agent/blob/main/docs/maxDamageV3DecisionTree.png)

## Technical Implementation
The core of the "Smarter" logic is built on **Weighted State Evaluation**. Rather than just looking at the current turn, the agent evaluates the *utility* of its moves:
1. **Tier 1 (Lethality)**: Can I KO the opponent right now?
2. **Tier 2 (Efficiency)**: Is there a Super-Effective move? If so, does it have STAB?
3. **Tier 3 (Neutral Pressure)**: If no advantage exists, which move provides the most consistent neutral damage?



## Key Achievements
* **Inference under Uncertainty**: Successfully implemented a system to estimate hidden opponent variables (EVs/IVs/Stats) to inform tactical choices.
* **Deterministic Modeling of Stochastic Events**: By assuming "low-roll" damage outcomes, the agent mitigates the risk of non-deterministic failure in critical turns.
* **Modular Benchmarking**: Designed a system to cross-evaluate these agents, quantifying the performance increase gained through heuristic state-estimation.

## Installation & Usage
1. **Prerequisites**: Python 3.8+ and a local Pokémon Showdown Server.
2. **Setup**:
   ```bash
   git clone [https://github.com/yourusername/Pok-mon-AI-Battle-Agent.git](https://github.com/yourusername/Pok-mon-AI-Battle-Agent.git)
   pip install -r requirements.txt
