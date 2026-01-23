
def visualise(board_state: list[list[int]]):
    # ANSI Color codes
    BLUE = "\033[94m"
    RED = "\033[91m"
    RESET = "\033[0m"
    
    board_state_visual = [["0","1","2"],["3","4","5"],["6","7","8"]]
    
    for row_index in range(len(board_state)):
        for column_index in range(len(board_state[row_index])):
            if board_state[row_index][column_index] == -1:
                # Wrap X in Blue
                board_state_visual[row_index][column_index] = f"{BLUE}X{RESET}"
            elif board_state[row_index][column_index] == 1:
                # Wrap O in Red
                board_state_visual[row_index][column_index] = f"{RED}O{RESET}"
    
    print("\n" + "-"*13) # Top border for style
    for row in board_state_visual:
        # Joining with " | " makes it look like a real grid
        print(f"| {' | '.join(row)} |")
        print("-"*13)
        





