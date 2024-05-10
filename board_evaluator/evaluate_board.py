from typing import List, Tuple


def check_winner(board: List[str]) -> Tuple[bool, str]:
    
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]

    for pattern in win_patterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != "":
            return (True, str(board[pattern[0]]))
    if "" not in board:
        return (True, "Draw")
    return (False, 'keep playing')