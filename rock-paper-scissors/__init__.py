import check50
from re import escape

@check50.check()
def exists():
    """rps.py exists"""
    check50.exists("rps.py")
    # Include testing.py so we can monkey-patch randint
    check50.include("testing.py")


@check50.check(exists)
def test_invalid_input():
    """rps.py rejects invalid input"""
    check50.run("python3 rps.py").stdin("cat", prompt=True).stdout(
        regex("Choose rock, paper, or scissors"), "Choose rock, paper, or scissors:"
    ).kill()


@check50.check(exists)
def test_valid_move():
    """rps.py accepts a valid move and prints a round result"""
    check50.run("python3 testing.py").stdin("rock", prompt=True).stdout(
        regex("Computer chose"), "Computer chose", regex=True
    ).kill()


@check50.check(test_valid_move)
def test_player_win():
    """rps.py outputs 'You win!' when player wins"""
    # Our monkey-patched randint returns 3 (scissors)
    check50.run("python3 testing.py").stdin("rock", prompt=True).stdout(
        regex("You win!"), "You win!", regex=True
    ).exit()


@check50.check(test_valid_move)
def test_player_loss():
    """rps.py outputs 'You lose!' when player loses"""
    # Monkey-patched randint returns 1 (rock)
    check50.run("python3 testing.py").stdin("scissors", prompt=True).stdout(
        regex("You lose!"), "You lose!", regex=True
    ).exit()


@check50.check(test_valid_move)
def test_tie():
    """rps.py outputs 'It's a tie!' when moves are equal"""
    # Monkey-patched randint returns 2 (paper)
    check50.run("python3 testing.py").stdin("paper", prompt=True).stdout(
        regex("It's a tie!"), "It's a tie!", regex=True
    ).exit()


def regex(text):
    """match case-insensitively with any characters on either side"""
    return rf"(?i)^.*{escape(text)}.*$"
