from game_logic import is_game_over,move_map,play_move

def get_reward(board_state:list[list[int]],turn_count,action:int) -> int:
    action = move_map[action]
    row = action[0]
    column = action[1]
    board_state = play_move(board_state,turn_count,row,column)
    return int(is_game_over(board_state))

def get_possible_actions(board_state:list[list[int]]) -> list[int]:
    possible_actions = []
    action = 1
    for row_index in range(len(board_state[0])):
        for column_index in range(len(board_state)):
            if board_state[row_index][column_index]:
                possible_actions.append(action)
            action += 1
            


