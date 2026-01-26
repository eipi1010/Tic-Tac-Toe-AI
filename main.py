
from game_logic import TicTacToe
from qai import QLearningAgent
import numpy as np
from agents.minmax_agent import MinMaxAgent
#from agents.linearai import LinearAI
from agents.random_agent import RandomAgent
from agents.human_agent import HumanAgent
from agents.Qlearning_agent import QLearningAgent
import copy
import random



def main():
    #randomai = RandomAI()  
    #linear_ai = LinearAI(alpha=0.001)
    #linear_ai.learn(100)
    #weights,bias = linear_ai._weights()
    #ai = QLearningAgent(0.1,0.1)
    #ai.learn(episodes=10000)
    human = HumanAgent()
    minimax_ai = MinMaxAgent()
    random_ai = RandomAgent()
    q_ai = QLearningAgent()
    q_ai.learn()
    print(q_ai)
    game = TicTacToe(minimax_ai,human,verbose=True)
    game.run(10)
    
    
if __name__ == "__main__":
    main()