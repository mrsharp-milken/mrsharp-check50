import check50
from re import escape
import builtins

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
def test_tie():
    """rps.py outputs 'It's a tie!' when moves are equal"""
    # Monkey-patch computer move for this round
    import testing
    testing.computer_moves = ["rock"]
    
    check50.run("python3 testing.py").stdin("rock", prompt=True).stdout(
        regex("Computer chose rock"), "Computer chose rock", regex=True
    ).stdout(
        regex("It's a tie!"), "It's a tie!", regex=True
    ).exit()


@check50.check(exists)
def test_player_win():
    """rps.py outputs 'You win!' when player beats computer"""
    import testing
    testing.computer_moves = ["scissors"]
    
    check50.run("python3 testing.py").stdin("rock", prompt=True).stdout(
        regex("Computer chose scissors"), "Computer chose scissors", regex=True
    ).stdout(
        regex("You win!"), "You win!", regex=True
    ).exit()


@check50.check(exists)
def test_player_loss():
    """rps.py outputs 'You lose!' when computer beats player"""
    import testing
    testing.computer_moves = ["paper"]
    
    check50.run("python3 testing.py").stdin("rock", prompt=True).stdout(
        regex("Computer chose paper"), "Computer chose paper", regex=True
    ).stdout(
        regex("You lose!"), "You lose!", regex=True
    ).exit()


def regex(text):
    """match case-insensitively with any characters on either side"""
    return rf"(?i)^.*{escape(text)}.*$"
