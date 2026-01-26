from flask import Flask, request, jsonify,send_from_directory
from agents.random_agent import RandomAgent
import os
from game import WINNING_MASKS

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "..", "frontend") # ../frontend from backend/


@app.route("/", methods=["GET"])
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/<path:filename>", methods=["GET"])
def serve_files(filename):
    return send_from_directory(FRONTEND_DIR, filename)



@app.route("/move", methods=["POST"])
def move():
    data = request.json
    x = data.get("x", 0)
    o = data.get("o", 0)
    state = data.get("state", 0)
    action = data.get("action")  # the clicked cell

    # Apply human move
    if action is not None:
        mask = 1 << action
        if (state & mask) == 0:  # empty
            # decide which bitboard to update: X or O
            x |= mask  # if human is always X
            state |= mask

    # Determine winner (optional)
    winner = None
    for mask in WINNING_MASKS:
        if (x & mask) == mask:
            winner = "X"
        elif (o & mask) == mask:
            winner = "O"
    if bin(state).count("1") == 9 and winner is None:
        winner = "Draw"

    return jsonify({"x": x, "o": o, "state": state, "winner": winner})
if __name__ == "__main__":
    app.run(debug=True)