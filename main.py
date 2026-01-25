from visual_renderer import visualise
from game_logic import is_game_over,is_move_legal,play_move,move_map,run
from agents.qai import QLearningAgent
import numpy as np
from agents.minimaxai import MiniMaxAI
from agents.linearai import LinearAI
from agents.randomai import RandomAI
from agents.human import Human
import copy
import random



def main():
    ai = MiniMaxAI()
    randomai = RandomAI()  
    #linear_ai = LinearAI(alpha=0.001)
    #linear_ai.learn(100)
    #weights,bias = linear_ai._weights()



    #ai = QLearningAgent(0.1,0.1)
    #ai.learn(episodes=10000)
    player_one = Human()
    player_two = Human()
    run(player_one,player_two,10)
    while input("Type q to quit: ") != "q":
        player_x = format(0,'08b')
        player_o = format(0,'08b')
        board_state = np.zeros((3,3))
        turn_count = 1
        decision = random.randint(0,1)

        while not is_game_over(board_state,turn_count):

            if turn_count % 2 == decision:
                print("Player 1's Turn (with the X's)")
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
    
if __name__ == "__main__":
    main()