import numpy as np

# Test with your exact board state
board_state = np.array([[0., 0., 0.],
                        [0., 0., 0.],
                        [0., 0., -1.]])

move_map = {
    0: (0, 0), 1: (0, 1), 2: (0, 2),
    3: (1, 0), 4: (1, 1), 5: (1, 2),
    6: (2, 0), 7: (2, 1), 8: (2, 2),
}

# Test move 0
row, col = move_map[0]
print(f"Move 0 -> ({row}, {col})")
print(f"board_state[{row}][{col}] = {board_state[row][col]}")
print(f"board_state[{row}, {col}] = {board_state[row, col]}")

# Both should print 0.0, not -1.0