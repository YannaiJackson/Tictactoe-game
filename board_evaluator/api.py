# THIS MODULE IS TO BE USED ONLY IF THE COMMUNICATING MODULE IS IN JAVASCRIPT

from fastapi import FastAPI, HTTPException
from typing import List, Tuple
from pydantic import BaseModel
from evaluate_board import check_winner
from algorithm import get_move
from fastapi.middleware.cors import CORSMiddleware

class Board(BaseModel):
    board: List[str]

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this according to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/check_winner", response_model=Tuple[bool, str])
async def check_winner_endpoint(board: Board):
    result = check_winner(board.board)
    return result

@app.post("/get-move", response_model=int)
async def get_move_endpoint(board: Board):
    result = get_move(board.board)
    return result


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
