from agents.agent import Agent
from agents.random_agent import RandomAgent

from tictactoe.backend.game import WINNING_MASKS
from tqdm import tqdm

class QLearningAgent(Agent):
    def __init__(self):
        self.random_agent = RandomAgent()
        self.q_table = {(0b000000000,0b000000000): 0,}

    def __str__(self):
        return str(self.q_table)

    def action(self,x,o,state):
        turn_count = self.turn_count(state)
        actions = self.actions(state)
        if turn_count % 2 == 1:
            min_eval = float('inf')
            best_action = action[0]
            for action in actions:
                eval = self.q(x,o,state,action)
                if min_eval > eval:
                    min_eval = eval
                    best_action = action
        
        else:
            max_eval = float('-inf')
            best_action = action[0]
            for action in actions:
                eval = self.q(x,o,state,action)
                if max_eval < eval:
                    max_eval = eval
                    best_action = action
        return best_action

    def q(self,x,o,state,action) -> float:
        x,o,state = self.play(x,o,state,action)
        game_state = (x,o)
        if game_state not in self.q_table:
            self.q_table[game_state] = self.eval(x,o,state)
        return self.q_table[game_state]
    
    def reward(self,x,o,state,action) -> int:
        return self.eval(x,o,state)

    def learn(self):
        for _ in tqdm(range(1000000),desc="QLearning"):
            x = 0b000000000
            o = 0b000000000
            state = 0b000000000

            while not self.terminal(x,o,state):
                actions = self.actions(state)
                turn_count = self.turn_count(state)

                #X is the minimizing player
                if turn_count % 2 == 1:
                    min_eval = float('inf')
                    best_action = actions[0]
                    for action in actions:
                        eval = self.q(x,o,state,action)
                        if min_eval > eval:
                            min_eval = eval
                            best_action = action
                
                else:
                    max_eval = float('-inf')
                    best_action = actions[0]
                    for action in actions:
                        eval = self.q(x,o,state,action)
                        if max_eval < eval:
                            max_eval = eval
                            best_action = action

                self.update(x,o,state,action)

                x,o,state = self.play(x,o,state,best_action)
    
    def update(self,x,o,state,action):
        current_q = self.q(x,o,state,action)
        prev_x,prev_o = x,o
        x,o,state = self.play(x,o,state,action)

        if not self.terminal(x,o,state):
            action = self.random_agent.action(x,o,state)
            x,o,state = self.play(x,o,state,action)

        turn_count = self.turn_count(state)

        if not self.terminal(x,o,state):
            actions = self.actions(state)

            if turn_count % 2 == 1:
                min_q = float('inf')
                best_action = actions[0]
                for action in actions:
                    q = self.q(x,o,state,action)
                    if min_q > q:
                        min_q = q
                        best_action = action
                
                reward = self.reward(x,o,state,best_action)
                gamma,alpha = 0.5,0.5
                new_q = reward + (gamma * min_q)
                self.q_table[(prev_x,prev_o)] = current_q + alpha * (new_q - current_q)
            
            else:
                max_q = float('-inf')
                best_action = actions[0]
                for action in actions:
                    q = self.q(x,o,state,action)
                    if max_q < q:
                        max_q = q
                        best_action = action

                reward = self.reward(x,o,state,best_action)
                gamma,alpha = 0.5,0.001
                new_q = reward + (gamma * max_q)
                self.q_table[(prev_x,prev_o)] = current_q + alpha * (new_q - current_q)
        
        

        
        











    



    
