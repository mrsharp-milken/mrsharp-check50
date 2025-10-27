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
    # Run testing.py with any scenario (e.g., player_wins)
    run = check50.run("python3 testing.py player_wins")
    # Enter an invalid move first
    run.stdin("cat", prompt=True).stdout(
        regex("Choose rock, paper, or scissors"), "Choose rock, paper, or scissors:"
    )
    # Then enter a valid move so the game continues
    run.stdin("rock", prompt=True).stdout(
        regex("Computer chose rock"), regex=True
    )
    run.stdout(regex("It's a tie!"), regex=True)
    run.kill()


@check50.check(exists)
def test_player_wins():
    """Player wins a full best-of-3 game"""
    run = check50.run("python3 testing.py player_wins")
    # Round 1: tie
    run.stdin("rock", prompt=True).stdout(regex("Computer chose rock"), regex=True)
    run.stdout(regex("It's a tie!"), regex=True)
    # Round 2: player win
    run.stdin("rock", prompt=True).stdout(regex("Computer chose scissors"), regex=True)
    run.stdout(regex("You win!"), regex=True)
    # Round 3: player win, match ends
    run.stdin("rock", prompt=True).stdout(regex("Computer chose paper"), regex=True)
    run.stdout(regex("You win!"), regex=True)
    run.stdout(regex("won the match"), regex=True).exit()


@check50.check(exists)
def test_computer_wins():
    """Computer wins a full best-of-3 game"""
    run = check50.run("python3 testing.py computer_wins")
    # Round 1: tie
    run.stdin("rock", prompt=True).stdout(regex("Computer chose rock"), regex=True)
    run.stdout(regex("It's a tie!"), regex=True)
    # Round 2: computer win
    run.stdin("rock", prompt=True).stdout(regex("Computer chose paper"), regex=True)
    run.stdout(regex("You lose!"), regex=True)
    # Round 3: computer win, match ends
    run.stdin("rock", prompt=True).stdout(regex("Computer chose scissors"), regex=True)
    run.stdout(regex("You lose!"), regex=True)
    run.stdout(regex("won the match"), regex=True).exit()


@check50.check(exists)
def test_tie_rounds():
    """Full game with multiple ties before a win"""
    run = check50.run("python3 testing.py tie_rounds")
    # Round 1: tie
    run.stdin("rock", prompt=True).stdout(regex("Computer chose rock"), regex=True)
    run.stdout(regex("It's a tie!"), regex=True)
    # Round 2: tie
    run.stdin("rock", prompt=True).stdout(regex("Computer chose rock"), regex=True)
    run.stdout(regex("It's a tie!"), regex=True)
    # Round 3: player win, match ends
    run.stdin("rock", prompt=True).stdout(regex("Computer chose scissors"), regex=True)
    run.stdout(regex("You win!"), regex=True)
    run.stdout(regex("won the match"), regex=True).exit()


def regex(text):
    """match case-insensitively with any characters on either side"""
    return rf"(?i)^.*{escape(text)}.*$"
