import numpy as np
import copy
import numpy as np
from game_logic import play_move
import copy
from tqdm import tqdm

class Agent:
    def __init__(self):
        pass

    def play(self,state):
        pass
        
    def turncount(self,state):
        return 10 - len(self.actions(state))


    def actions(self,state:np.ndarray) -> list:
        possible_actions = []
        action = 0
        for row_index in range(len(state[0])):
            for column_index in range(len(state)):
                if state[row_index][column_index] == 0:
                    possible_actions.append(action)
                action += 1

        return possible_actions
    

    def player(self,state:np.ndarray):
        turn_count = self.turncount(state)
        if turn_count % 2 == 1:
            return "XMIN"
        else:
            return "OMAX"
    
    def result(self,state:np.ndarray,action:int) -> np.ndarray:
        state = copy.deepcopy(state)
        turn_count = self.turncount(state)
        state = play_move(state, action, turn_count)
        return state


    def terminal(self,state:"np.ndarray"):
        # Check Rows
        for row in state:
            if sum(row) == 3:
                return True
            elif sum(row) == -3:
                return True
            
        # Check Columns
        for i in range(len(state[0])):
            sum_column = 0
            for j in range(len(state)):
                sum_column += state[j][i]

            if sum_column == 3:
                return True
            elif sum_column == -3:
                return True

        # Check Diagonals
        sum_diagonal_left = 0
        sum_diagonal_right = 0
        size = len(state)

        for i in range(size):
            # Left-to-right: (0,0), (1,1), (2,2)
            sum_diagonal_left += state[i][i]
            
            # Right-to-left: (0,2), (1,1), (2,0)
            sum_diagonal_right += state[i][size - 1 - i]

        if sum_diagonal_left == 3 or sum_diagonal_right == 3:
            return True
        if sum_diagonal_left == -3 or sum_diagonal_right == -3:
            return True
        
        if len(self.actions(state)) == 0:
            return True

        return False

    def value(self,state:list[list[int]]) -> int:
        # Check Rows
        for row in state:
            if sum(row) == 3:
                return 1
            elif sum(row) == -3:
                return -1
            
        # Check Columns
        for i in range(len(state[0])):
            sum_column = 0
            for j in range(len(state)):
                sum_column += state[j][i]

            if sum_column == 3:
                return 1
            elif sum_column == -3:
                return -1

        # Check Diagonals
        sum_diagonal_left = 0
        sum_diagonal_right = 0
        size = len(state)

        for i in range(size):
            # Left-to-right: (0,0), (1,1), (2,2)
            sum_diagonal_left += state[i][i]
            
            # Right-to-left: (0,2), (1,1), (2,0)
            sum_diagonal_right += state[i][size - 1 - i]

        if sum_diagonal_left == 3 or sum_diagonal_right == 3:
            return 1
        if sum_diagonal_left == -3 or sum_diagonal_right == -3:
            return -1
        
        return 0