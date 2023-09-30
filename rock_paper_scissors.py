import random

def is_win(player, opponent):
    # returns True if player wins
    #  r>s, s>p , p>r
    if (player == 'r' and opponent =='s') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

def play():
    user = input("What is your choice?\n'r' for rock, 'p' for paper, 's' for scissors:\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It is a tie."
    # r>s, s>p , p>r
    if is_win(user, computer):
        return f"You won!\nPlayer choice:\t\t{user}\nComputer choice:\t{computer}"

    return f"You lost!\nPlayer choice:\t\t{user}\nComputer choice:\t{computer}"

print(play())
