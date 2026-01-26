import numpy as np
import copy
import numpy as np
import copy
from tqdm import tqdm
from game import WINNING_MASKS

class Agent:
    def __init__(self):
        pass

    def play(self,x_state,o_state,state,action):
        turn_count = self.turn_count(state)
        if not self.legal(state,str(action)):
            raise ValueError(f"Invalide action ({action}) in state ({state})")

        mask = 0b1 << (8-action)

        if turn_count % 2 == 1:
            x_state |= mask
        else:
            o_state |= mask

        state = x_state | o_state
        return x_state, o_state, state

    def actions(self,state) -> list:
        state_str = format(state,'09b')
        actions = [i for i in range(len(state_str)) if state_str[i] == '0']

        return actions
    
    def turn_count(self,state) -> int:
        turn_count = bin(state).count('1')
        return turn_count
    
    def eval(self,x_state,o_state,state):

        x_win = any((x_state & mask) == mask for mask in WINNING_MASKS)
        o_win = any((o_state & mask) == mask for mask in WINNING_MASKS)
        #draw = (bin(state).count('1') == 9)

        if x_win:
            return -1
        elif o_win:
            return 1
        return 0

    def terminal(self,x_state,o_state,state):
        x_win = any((x_state & mask) == mask for mask in WINNING_MASKS)
        o_win = any((o_state & mask) == mask for mask in WINNING_MASKS)
        draw = (bin(state).count('1') == 9)

        return x_win or o_win or draw
    
    def legal(self,state,action:int) -> bool:
        state_str = format(state,'09b')
        if action.isdigit() and 0 <= int(action) <= 8:
            if state_str[int(action)] == '0':
                return True
        
        return False

