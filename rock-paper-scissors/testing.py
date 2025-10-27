import random

# Predefine computer moves for multiple rounds
# Round 1: tie
# Round 2: player wins
# Round 3: computer wins
computer_moves = ["rock", "scissors", "paper"]

def choice_mock(options):
    return computer_moves.pop(0)

random.choice = choice_mock

# Import the student's rps.py
import importlib.util
import sys

spec = importlib.util.spec_from_file_location("rps", "rps.py")
rps = importlib.util.module_from_spec(spec)
sys.modules["rps"] = rps
spec.loader.exec_module(rps)
