import random
import sys
import builtins

# Determine scenario from command-line argument
scenario = sys.argv[1] if len(sys.argv) > 1 else "player_wins"

# Define full sequences of computer moves for each scenario
if scenario == "player_wins":
    # Round 1: tie, Round 2: player win, Round 3: player win
    computer_moves = ["rock", "scissors", "paper"]
elif scenario == "computer_wins":
    # Round 1: tie, Round 2: computer win, Round 3: computer win
    computer_moves = ["rock", "paper", "scissors"]
elif scenario == "tie_rounds":
    # Round 1: tie, Round 2: tie, Round 3: player win
    computer_moves = ["rock", "rock", "paper", "paper", "scissors", "scissors"]
elif scenario == "invalid_input":
    # Use one move; test will send bad input first
    computer_moves = ["rock"]
else:
    computer_moves = ["rock", "scissors", "paper"]

# Monkey-patch random.choice globally
original_choice = random.choice
def choice_mock(options):
    return computer_moves.pop(0)
random.choice = choice_mock

# Monkey-patch input to handle bad input automatically if needed
original_input = builtins.input

# Import student's rps.py
import importlib.util
spec = importlib.util.spec_from_file_location("rps", "rps.py")
rps = importlib.util.module_from_spec(spec)
sys.modules["rps"] = rps
spec.loader.exec_module(rps)
