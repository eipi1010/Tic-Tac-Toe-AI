from backend.agents.agent import Agent
from tictactoe.backend.game import WINNING_MASKS
import random



class MinMaxAgent(Agent):

    def action(self,x_state,o_state,state):

        if self.terminal(x_state,o_state,state):
            return
        
        turn_count = bin(state).count('1') + 1

        #If odd turn count then player is X
        if turn_count % 2 == 1:
            min_eval = float('inf')
            actions = []
            for action in self.actions(state):
                eval = self.Minimax(*self.play(x_state,o_state,state,action),float('-inf'),float('inf'), False)
                if eval < min_eval:
                    min_eval = eval
                    actions.clear()
                    actions.append(action)
                elif eval == min_eval:
                    actions.append(action)

            return random.choice(actions)

        
        #If even the player is O trying to maximise
        else:
            max_eval = float('-inf')
            actions = []
            for action in self.actions(state):
                eval = self.Minimax(*self.play(x_state,o_state,state,action),float('-inf'),float('inf'),True)
                if eval > max_eval:
                    max_eval = eval
                    actions.clear()
                    actions.append(action)
                elif eval == max_eval:
                    actions.append(action)
            return random.choice(actions)


    def Minimax(self,x_state,o_state,state,alpha,beta,minimizing_player):

        if self.terminal(x_state,o_state,state):
            return self.eval(x_state,o_state,state)

        if minimizing_player:
            min_eval = float('inf')
            for action in self.actions(state):
                min_eval = min(min_eval, self.Minimax(*self.play(x_state,o_state,state,action),alpha,beta,False))
                beta = min(min_eval,beta)
                if beta <= alpha:
                    break
            return min_eval
        
        else:
            max_eval = float('-inf')
            for action in self.actions(state):
                max_eval = max(max_eval, self.Minimax(*self.play(x_state,o_state,state,action),alpha,beta,True))
                alpha = max(max_eval,alpha)
                if beta <= alpha:
                    break
            return max_eval
        

        