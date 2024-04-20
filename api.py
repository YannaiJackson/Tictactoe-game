from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class BoardList(BaseModel):
    board: List[str]

@app.post("/check_for_winner/")
async def process_items(cells_list: BoardList):
    board = cells_list.board
    # Process the cells here
    winner = check_winner(board)
    if winner == None:
        return {"message": "no winner yet, keep playing", "board": board}
    return {"message": f'the winner is {winner}', "board": board}


def check_winner(board: List[str]):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for pattern in win_patterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != " ":
            return board[pattern[0]]
    if " " not in board:
        return "Draw"
    return None
