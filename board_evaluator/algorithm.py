from typing import List, Tuple
from evaluate_board import check_winner


def minimax(board, depth, maximizing_player):
    winner, _ = check_winner(board) 
    if winner:
        if winner == 'X':
            return -10 + depth
        elif winner == 'O':
            return 10 - depth
        elif winner == 'Draw':
            return 0

    if maximizing_player:
        max_score = float('-inf')
        for i in range(9):
            if board[i] == '':
                board[i] = 'O'
                score = minimax(board[:], depth + 1, False)
                board[i] = ''
                max_score = max(score, max_score)
        return max_score
    else:
        min_score = float('inf')
        for i in range(9):
            if board[i] == '':
                board[i] = 'X'
                score = minimax(board[:], depth + 1, True)
                board[i] = ''
                min_score = min(score, min_score)
        return min_score

def get_move(board):
    num_chars = sum(1 for cell in board if cell != '') # Count non-empty cells
    if num_chars % 2 == 1:  # If the number of characters is odd
        best_score = float('-inf')
        best_move = -1
        for i in range(9):
            if board[i] == '':
                board_copy = board[:]
                board_copy[i] = 'O'
                score = minimax(board_copy, 0, False)
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move
    else:
        return -1  # No move if the number of characters is even
