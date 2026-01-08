# -*- coding: utf-8 -*-
import asyncio
from poke_env.player.baselines import RandomPlayer
from poke_env.player.utils import cross_evaluate
from poke_env.ps_client import AccountConfiguration
from tabulate import tabulate
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

async def main():
    # Create three random players
    players = [
        RandomPlayer(max_concurrent_battles=10,account_configuration=AccountConfiguration(f"RandomPlayer{i+1}", "SecretPassword!")) for i in range(3)
    ]
    # Make these players all play against each other 20 times.
    cross_evaluation = await cross_evaluate(players, n_challenges=20)
    # Tabulating
    # Defines a header for displaying the results
    table = [["-"] + [p.username for p in players]]

    # Adds one line per player with corresponding results
    for p_1, results in cross_evaluation.items():
        table.append([p_1] + [cross_evaluation[p_1][p_2] for p_2 in results])

    # Displays results in a nicely formatted table.
    print(tabulate(table))

if __name__ == "__main__":
    asyncio.run(main())



    