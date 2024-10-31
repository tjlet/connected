from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Initialize the game board
board = [[0 for _ in range(7)] for _ in range(6)]
current_player = 1

def check_winner():
    # Check horizontal, vertical, and diagonal for a winner
    for r in range(6):
        for c in range(7):
            if board[r][c] == 0:
                continue
            if c + 3 < 7 and all(board[r][c+i] == board[r][c] for i in range(4)):
                return board[r][c]
            if r + 3 < 6 and all(board[r+i][c] == board[r][c] for i in range(4)):
                return board[r][c]
            if r + 3 < 6 and c + 3 < 7 and all(board[r+i][c+i] == board[r][c] for i in range(4)):
                return board[r][c]
            if r + 3 < 6 and c - 3 >= 0 and all(board[r+i][c-i] == board[r][c] for i in range(4)):
                return board[r][c]
    return 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move/<int:column>', methods=['POST'])
def move(column):
    global current_player
    for r in reversed(range(6)):
        if board[r][column] == 0:
            board[r][column] = current_player
            winner = check_winner()
            current_player = 3 - current_player  # Switch player
            return jsonify({'winner': winner, 'board': board})
    return jsonify({'error': 'Column full'})

@app.route('/reset', methods=['POST'])
def reset():
    global board, current_player
    board = [[0 for _ in range(7)] for _ in range(6)]
    current_player = 1
    return jsonify({'board': board})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
