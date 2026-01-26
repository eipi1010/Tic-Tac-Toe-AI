import numpy as np
import random
import copy
from tqdm import tqdm

class QLearningAgent():
    def __init__(self,gamma:float,alpha:float):
        self.gamma = gamma
        self.alpha = alpha
 
        self.qtable = {}
        self.board_state = np.zeros((3,3))
        self.turn_count = 1
    def __str__(self):
        return(str(self.qtable))
    

    def get_best_action(self,board_state,turn_count) -> str:
        possible_actions = self.get_possible_actions(board_state) or []
        action_taken = random.choice(possible_actions)
        best_reward = self.qtable_expected(board_state,action_taken)
        for action in possible_actions:
            reward = self.qtable_expected(board_state,action)
            if turn_count % 2 == 1:
                if best_reward < reward:
                    best_reward = reward
                    action_taken = action
            else:
                if best_reward > reward:
                    best_reward = reward
                    action_taken = action
            
        return action_taken

    
    def learn(self,episodes=1000):
        for epsilon in tqdm(range(episodes)):
            self.board_state = np.zeros((3,3))
            self.turn_count = 1
            while abs(self.is_game_over(self.board_state)) == 0 and self.turn_count <= 9:
                possible_actions = self.get_possible_actions(self.board_state) or []
                if random.randint(0,int(epsilon)) == 0:
                    action_taken = random.choice(possible_actions)
                else:
                    action_taken = self.get_best_action(self.board_state,self.turn_count)
                q_observed = self.getqvalue(self.board_state,action_taken,self.turn_count)
                q_expected = self.qtable_expected(self.board_state,action_taken)
                td_error = q_observed - q_expected
                game_state = self.get_state_key(self.board_state,self.turn_count%2)
                self.qtable[game_state][action_taken] = q_expected + self.alpha * td_error
                self.board_state = play_move(self.board_state,self.turn_count,action_taken)
                self.turn_count += 1
            

    def get_state_key(self,board_state,turn_count):
        board_state = board_state.ravel().tolist()
        board_state.append(turn_count % 2)
        return tuple(board_state)
                
    def qtable_expected(self,board_state,action) -> float:
        qrewards = np.zeros(9)
        game_state = self.get_state_key(board_state,self.turn_count)
        if game_state not in self.qtable:
            self.qtable[game_state] = qrewards

        return self.qtable[game_state][action]
        

    def getqvalue(self,board_state,action:int,turn_count):
        qvalue = self.get_reward(board_state,action,turn_count) + self.gamma * self.get_expected_bestqvalue(board_state,action,turn_count)
        return qvalue
    
    def get_expected_bestqvalue(self,board_state,action:int,turn_count):
        temp_board_state = copy.deepcopy(board_state)
        temp_board_state = play_move(temp_board_state,turn_count,action)
        
        actions = self.get_possible_actions(temp_board_state)
        best_q = self.qtable_expected(temp_board_state,action)

        if turn_count % 1 == 0:
            for action in actions:
                q_expected = self.qtable_expected(temp_board_state,action)
                best_q = min(best_q,q_expected)
        else:
            for action in actions:
                q_expected = self.qtable_expected(temp_board_state,action)
                best_q = max(best_q,q_expected)            
        
        return best_q

    def get_reward(self, board_state,action:int,turn_count) -> int:
        temp_board_state = play_move(board_state,turn_count,action)
        if abs(self.is_game_over(temp_board_state)) == 1:
            return self.is_game_over(temp_board_state)
        else:
            return 0

    def get_possible_actions(self,board_state:list[list[int]]) -> list[int]:
        possible_actions = []
        action = 0
        for row_index in range(len(board_state[0])):
            for column_index in range(len(board_state)):
                if board_state[row_index][column_index] == 0:
                    possible_actions.append(action)
                action += 1

        return possible_actions

    def is_game_over(self,board_state:list[list[int]]) -> int:
        # Check Rows
        for row in board_state:
            if sum(row) == 3:
                return 1
            elif sum(row) == -3:
                return -1
            
        # Check Columns
        for i in range(len(board_state[0])):
            sum_column = 0
            for j in range(len(board_state)):
                sum_column += board_state[j][i]

            if sum_column == 3:
                return 1
            elif sum_column == -3:
                return -1

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
            return 1
        if sum_diagonal_left == -3 or sum_diagonal_right == -3:
            return -1
        
        return 0

            



