move_map = {
    0: (0, 0),
    1: (0, 1),
    2: (0, 2),
    3: (1, 0),
    4: (1, 1),
    5: (1, 2),
    6: (2, 0),
    7: (2, 1),
    8: (2, 2),
}

import numpy as np


def is_game_over(board_state:list[list[int]]) -> bool:
    # Check Rows
    for row in board_state:
        if sum(row) == 3:
            print("Player 2 won with the O's!")
            return True
        elif sum(row) == -3:
            print("Player 1 won with the X's!")
            return True
        
    # Check Columns
    for i in range(len(board_state[0])):
        sum_column = 0
        for j in range(len(board_state)):
            sum_column += board_state[j][i]

        if sum_column == 3:
            print("Player 2 won with the O's!")
            return True
        elif sum_column == -3:
            print("Player 1 won with the X's!")
            return True

    # Check Diagonals
    sum_diagonal_left = 0
    sum_diagonal_right = 0
    size = len(board_state)

    for i in range(size):
        # Left-to-right: (0,0), (1,1), (2,2)
        sum_diagonal_left += board_state[i][i]
        
        # Right-to-left: (0,2), (1,1), (2,0)
        sum_diagonal_right += board_state[i][size - 1 - i]

    if sum_diagonal_left == 3 or sum_diagonal_right == 3:
        print("Player 2 won with O's!")
        return True
    if sum_diagonal_left == -3 or sum_diagonal_right == -3:
        print("Player 1 won with X's!")
        return True
    
    return False

def play_move(board_state,action,turn_count) -> list[list[int]]:
    row = int(move_map[action][0])
    column = int(move_map[action][1])
    if get_player_turn(board_state,turn_count) == "XMIN":
        board_state[row][column] = -1
    else:
        board_state[row][column] = 1
    return board_state

def get_player_turn(board_state:np.ndarray,turn_count):
    if turn_count % 2 == 1:
        return "XMIN"
    else:
        return "OMAX"

def is_move_legal(board_state,user_input) -> bool:
    if not str(user_input.isdigit()):
        return False
    
    user_input = int(user_input)
    
    if user_input < 0 or user_input > 8:
        return False
    
    row = int(move_map[user_input][0])
    column = int(move_map[user_input][1])
    print(f"{row}{column}")
    print(board_state[row][column])
    return board_state[row][column] == 0



