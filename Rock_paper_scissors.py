import random

def play():
    user=input("Whats Your Choice? 'r' for Rock, 'p' for Paper, 's' for Scissors\n: ")
    computer=random.choice(['r', 'p', 's'])

    if user == computer:
        return 'Its a Tie!'

    # r>s, s>p, p>r
    if is_win(user, computer):
        return 'You Won!'
     
    return 'You lost!'

def is_win(player, opponent): #return true if player wins
    if (player ==  'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True 
        
print(play())