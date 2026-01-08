# -*- coding: utf-8 -*-
import asyncio
import time
import os, sys

from poke_env.player.player import Player
from poke_env.player.baselines import RandomPlayer
from poke_env.battle.pokemon_type import PokemonType
from poke_env.player.utils import cross_evaluate
from tabulate import tabulate
from agents.agents import SmarterGuy
from agents.agents import TestPlayer
from agents.agents import MaxDamagePlayer

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

async def main():
    start = time.time()
    
    # Create players.
    random_player = RandomPlayer(
    battle_format="gen8randombattle"
    )
    max_damage_player = MaxDamagePlayer(
        battle_format="gen8randombattle"
    )
    test_player = TestPlayer(
        battle_format="gen8randombattle"
    )
    smarter_player = SmarterGuy(
        battle_format="gen8randombattle"
    )

    # await smarter_player.battle_against(max_damage_player, n_battles=1)
    # print(
    #     "Max damage player won %d / 100 battles against random player [this took %f seconds]"
    #     % (
    #         smarter_player.n_won_battles, time.time() - start
    #     )
    # )

    players = [max_damage_player, test_player, smarter_player, random_player]

    cross_evaluation = await cross_evaluate(players, n_challenges=500)
    
    table = [["-"] + [p.username for p in players]]

    for p_1, results in cross_evaluation.items():
        table.append([p_1] + [cross_evaluation[p_1][p_2] for p_2 in results])

    print(tabulate(table))

    test_player = TestPlayer(
        battle_format="gen8randombattle"
    )
    
    # await test_player.accept_challenges(None,1)
    # print()

if __name__ == "__main__":
    asyncio.run(main())