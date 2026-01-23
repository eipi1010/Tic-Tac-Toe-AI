from visual_renderer import visualise
from game_logic import is_game_over,is_move_legal,play_move,move_map
from qai import QLearningAgent
import numpy as np
from miniai import MiniMaxAI
import copy


def main():
    board_state = np.zeros((3,3))
    turn_count = 1
    ai = MiniMaxAI()


    #ai = QLearningAgent(0.1,0.1)
    #ai.learn(episodes=10000)

    while (not is_game_over(board_state)) and turn_count <= 9:
        if turn_count % 2 == 1:
            print("Player 1's Turn (with the X's)")
        else:
            print("Player 2's Turn (with the O's)")

        visualise(board_state)
        print(board_state)   

        if turn_count % 2 == 1:
            user_input = input("Enter number (0-8): ")
        else:
            state = copy.deepcopy(board_state)
            user_input = str(ai.play(state))
        
        while not is_move_legal(board_state,user_input):
            user_input = input("Enter valid number (0-8): ")
            
        board_state = play_move(board_state,int(user_input),turn_count)
        turn_count += 1
    
    visualise(board_state)
    if turn_count > 9: 
        print("Draw!")
    
if __name__ == "__main__":
    main()