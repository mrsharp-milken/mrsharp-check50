import check50
from re import escape

@check50.check()
def exists():
    """rps.py exists"""
    check50.exists("rps.py")
    check50.include("testing.py")

@check50.check(exists)
def test_invalid_input():
    """rps.py reprompts when user enters invalid input"""
    run = check50.run("python3 testing.py invalid_input")

    # Try to send invalid input — don't wait for a prompt (handles both styles)
    run.stdin("cat")

    # Expect the exact invalid message
    run.stdout("Invalid choice, try again.\n", "Invalid choice, try again.")

    run.kill()


@check50.check(exists)
def test_player_wins():
    """Player wins a full best-of-3 game"""
    run = check50.run("python3 testing.py player_wins")

    # Round 1: tie
    run.stdin("rock")  # don't wait for prompt — supports both input styles
    run.stdout("Computer chose rock.", "Computer chose rock.")
    run.stdout("It's a tie!\n", "It's a tie!")

    # Round 2: player wins
    run.stdin("rock")
    run.stdout("Computer chose scissors.", "Computer chose scissors.")
    run.stdout("You win this round!\n", "You win this round!")

    # Round 3: player wins (match ends)
    run.stdin("scissors")
    run.stdout("Computer chose paper.", "Computer chose paper.")
    run.stdout("You win this round!\n", "You win this round!")
    run.stdout("You won the match!", "You won the match!")

    run.exit(0)



@check50.check(exists)
def test_computer_wins():
    """Computer wins a full best-of-3 game"""
    run = check50.run("python3 testing.py computer_wins")

    # Round 1: tie
    run.stdin("rock")
    run.stdout("Computer chose rock.", "Expected computer’s move (round 1)")
    run.stdout("It's a tie!\n", "Expected tie message (round 1)")

    # Round 2: computer wins
    run.stdin("rock")
    run.stdout("Computer chose paper.", "Expected computer’s move (round 2)")
    run.stdout("You lose this round!\n", "Expected loss message (round 2)")

    # Round 3: computer wins again, match ends
    run.stdin("paper")
    run.stdout("Computer chose scissors.", "Expected computer’s move (round 3)")
    run.stdout("You lose this round!\n", "Expected loss message (round 3)")
    run.stdout("The computer won the match.", "Expected final match result")

    run.exit(0)


@check50.check(exists)
def test_tie_rounds():
    """Full game with multiple ties and an invalid input"""
    run = check50.run("python3 testing.py tie_rounds")

    # Round 1: tie
    run.stdin("rock")
    run.stdout("Computer chose rock.", "Round 1: computer move")
    run.stdout("It's a tie!\n", "Round 1: tie message")

    # Round 2: player win
    run.stdin("paper")
    run.stdout("Computer chose rock.", "Round 2: computer move")
    run.stdout("You win this round!\n", "Round 2: player win")

    # Round 3: invalid input (not counted)
    run.stdin("dog")
    run.stdout("Invalid choice, try again.\n", "Round 3: invalid input message")
    run.stdout("Choose rock, paper, or scissors:", "Round 3: reprompt")

    # Round 3 retry: tie (this uses the same computer move as previous round 3)
    run.stdin("paper")
    run.stdout("Computer chose paper.", "Round 3 retry: computer move")
    run.stdout("It's a tie!\n", "Round 3 retry: tie message")

    # Round 4: computer win
    run.stdin("rock")
    run.stdout("Computer chose paper.", "Round 4: computer move")
    run.stdout("You lose this round!\n", "Round 4: player loss")

    # Round 5: tie
    run.stdin("scissors")
    run.stdout("Computer chose scissors.", "Round 5: computer move")
    run.stdout("It's a tie!\n", "Round 5: tie message")

    # Round 6: player win (match ends)
    run.stdin("rock")
    run.stdout("Computer chose scissors.", "Round 6: computer move")
    run.stdout("You win this round!\n", "Round 6: player win")
    run.stdout("You won the match!", "Final match result")

    run.exit(0)




def regex(text):
    """match case-insensitively with any characters on either side"""
    return rf"(?i)^.*{escape(text)}.*$"
