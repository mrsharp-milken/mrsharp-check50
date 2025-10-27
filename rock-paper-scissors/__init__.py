import check50
from re import escape

@check50.check()
def exists():
    """rps.py exists"""
    check50.exists("rps.py")
    check50.include("testing.py")


@check50.check(exists)
def test_invalid_input():
    """rps.py rejects invalid input"""
    check50.run("python3 rps.py").stdin("cat", prompt=True).stdout(
        regex("Choose rock, paper, or scissors"), "Choose rock, paper, or scissors:"
    ).kill()


@check50.check(exists)
def test_full_game():
    """rps.py correctly plays a best-of-3 game with tie, player win, and computer win"""
    # Player inputs designed to test the sequence:
    # Round 1: tie → player inputs "rock"
    # Round 2: player win → player inputs "rock"
    # Round 3: computer win → player inputs "rock"
    inputs = ["rock", "rock", "rock"]

    run = check50.run("python3 testing.py")
    for i in inputs:
        run.stdin(i, prompt=True)

    # Check outputs for each round
    run.stdout(regex("Computer chose rock"), "Computer chose rock", regex=True)
    run.stdout(regex("It's a tie!"), "It's a tie!", regex=True)
    run.stdout(regex("Computer chose scissors"), "Computer chose scissors", regex=True)
    run.stdout(regex("You win!"), "You win!", regex=True)
    run.stdout(regex("Computer chose paper"), "Computer chose paper", regex=True)
    run.stdout(regex("You lose!"), "You lose!", regex=True)

    # Check that the final match ends
    run.stdout(regex("won the match"), "won the match", regex=True).exit()


def regex(text):
    """match case-insensitively with any characters on either side"""
    return rf"(?i)^.*{escape(text)}.*$"
