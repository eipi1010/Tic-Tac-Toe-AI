from agents.agent import Agent
from agents.random_agent import RandomAI
from agents.minmax_agent import MiniMaxAI
import numpy as np
from game_logic import is_game_over,is_move_legal,play_move
import copy
import random
from tqdm import tqdm


class LinearAI(Agent):
    def __init__(self,alpha):
        self.alpha = alpha
        self.weights = np.zeros((9,18))
        self.bias = np.zeros((9,1))

    def play(self,state):
        input = self.get_input(state)
        y_hat = self.weights @ input + self.bias
        action = self.actions(state)
        best_action = action[0]
        best_y_hat = float('-inf')
        for a in action:
            if y_hat[a] > best_y_hat:
                best_action = a
                best_y_hat = y_hat[a]
        return best_action

        
    def get_input(self,state:np.ndarray) -> np.ndarray:
        state = state.flatten()
        input = np.zeros((18,1))
        #X's are the first 9 input spots and O's are the last 9 input spots
        for i in range(len(state)):
            if state[i] == 0:
                continue
            elif state[i] == -1:
                input[i] = 1
            else:
                input[i+9] = 1

        return input
    
    def learn(self,episodes = 100):
        random_ai = RandomAI()
        minimax_ai = MiniMaxAI()


        for _ in tqdm(range(episodes), desc="Training"):
            state = np.zeros((3,3))
            input = self.get_input(state)
            turn_count = 1
            decision = random.randint(0,1)

            if decision == 0:
                print("Player 1 is LinearAI")
            else:
                print("Player 2 is LinearAI")

            while not is_game_over(state,turn_count):
                input = self.get_input(state)



                if turn_count % 2 == decision:
                    user_input = random_ai.play(state)
                else:
                    y = np.zeros((9,1))
                    y[minimax_ai.play(state)] = 1
                    y_hat = self.weights @ input + self.bias
                    y_hat = self.relu(y_hat)
                    self.get_weights(input, y)
                    user_input = self.play(state, self.weights,self.bias)
                    

                state = play_move(state,int(user_input),turn_count)
                turn_count += 1
            
        
    def relu(self,y_hat):
        for i in range(len(y_hat)):
            if y_hat[i][0] < 0:
                y_hat[i][0] = 0
        
        return y_hat

    def get_weights(self,input,y):
        y_hat = self.weights @ input + self.bias
        error = y_hat - y                    # (9, 1)

        dW = 2 * error @ input.T             # (9, 18)
        db = 2 * error                       # (9, 1)

        self.weights -= self.alpha * dW
        self.bias    -= self.alpha * db

    


