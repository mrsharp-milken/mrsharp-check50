import random
import sys

# Determine scenario from command-line argument
scenario = sys.argv[1]  # e.g., "player_wins", "computer_wins", "tie_rounds"

if scenario == "player_wins":
    # Sequence of computer moves for full game
    # Round 1: tie, Round 2: player win, Round 3: player win
    computer_moves = ["rock", "scissors", "paper"]
elif scenario == "computer_wins":
    # Round 1: tie, Round 2: computer win, Round 3: computer win
    computer_moves = ["rock", "paper", "scissors"]
elif scenario == "tie_rounds":
    # Round 1: tie, Round 2: tie, Round 3: player win
    computer_moves = ["rock", "rock", "scissors"]
else:
    computer_moves = ["rock", "scissors", "paper"]  # default

def choice_mock(options):
    return computer_moves.pop(0)

# Monkey-patch random.choice
random.choice = choice_mock

# Import student's rps.py
import importlib.util
import sys
spec = importlib.util.spec_from_file_location("rps", "rps.py")
rps = importlib.util.module_from_spec(spec)
sys.modules["rps"] = rps
spec.loader.exec_module(rps)
