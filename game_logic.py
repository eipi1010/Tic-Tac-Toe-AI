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

import random

import numpy as np

def run(player_one,player_two,games:int):
    for _ in range(games):
        player_x = 0b000000000
        player_o = 0b000000000
        state = 0b000000000
        turn_order = random.randint(0,1)
        while not is_game_over(player_x,player_o,state):
            if turn_count % 2 == turn_order:
                print(f"Player {"1" if turn_order == 1 else "2"}\'s Turn (with the {"X" if turn_order == 1 else "O"}\'s)")
                player_one.play(player_x,player_o):
                player_

            
                visualise(board_state) 
                user_input = input("Enter number (0-8): ")
                while not is_move_legal(board_state,str(user_input)):
                    user_input = input("Enter valid number (0-8): ")
            else:
                print("Player 2's Turn (with the O's)")
                visualise(board_state) 
                user_input = input("Enter number (0-8): ")
                while not is_move_legal(board_state,str(user_input)):
                    user_input = input("Enter valid number (0-8)")
                
            board_state = play_move(board_state,int(user_input),turn_count)
            turn_count += 1

            visualise(board_state)


def is_game_over(x_state,o_state, state) -> bool:
    winning_masks = [
        0b111000000,  # top row
        0b000111000,  # middle row
        0b000000111,  # bottom row
        0b100100100,  # left column
        0b010010010,  # middle column
        0b001001001,  # right column
        0b100010001,  # diagonal \
        0b001010100,  # diagonal /
    ]

    x_win = any((x_state & mask) == mask for mask in winning_masks)
    o_win = any((o_state & mask) == mask for mask in winning_masks)
    draw = (state.bit_count() == 9)

    for mask in range(len(winning_masks)):
        if player_x & mask == mask:



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
    
    if turn_count > 9:
        print("Draw!")
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




