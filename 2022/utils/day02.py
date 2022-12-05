def parse_left_move(s):
    if s == "A":
        return "Rock"
    elif s == "B":
        return "Paper"
    elif s == "C":
        return "Scissors"
    raise ValueError(s + " is invalid.")
    
def parse_right_move(s):
    if s == "X":
        return "Rock"
    elif s == "Y":
        return "Paper"
    elif s == "Z":
        return "Scissors"
    raise ValueError(s + " is invalid.")
    
def move_score(move):
    if move == "Rock":
        return 1
    elif move == "Paper":
        return 2
    elif move == "Scissors":
        return 3
    
    raise ValueError(move + " is invalid.")
    
def outcome_score(outcome):
    if outcome == "Lose":
        return 0
    elif outcome == "Tie":
        return 3
    elif outcome == "Win":
        return 6
    raise ValueError(outcome + " is invalid.")
    
def parse_right_outcome(s):
    if s == "X":
        return "Lose"
    elif s == "Y":
        return "Tie"
    elif s == "Z":
        return "Win"
    
    raise ValueError(f"{s} is invalid")