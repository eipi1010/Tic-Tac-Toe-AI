from agents.agent import Agent



class MiniMaxAI(Agent):
    def play(self,state):

        if self.terminal(state):
            return
        if self.player(state) == "XMIN":
            best_value = float('inf')
            best_action = self.actions(state)[0]
            for action in self.actions(state):
                value = self.Minimax(self.result(state,action))
                if value < best_value:
                    best_value = value
                    best_action = action
            return best_action

        
        if self.player(state) == "OMAX":
            best_value = float('-inf')
            best_action = self.actions(state)[0]
            for action in self.actions(state):
                value = self.Minimax(self.result(state,action))
                if value > best_value:
                    best_value = value
                    best_action = action
            return best_action


    def Minimax(self,state):
        if self.terminal(state):
            return self.value(state)
        if self.player(state) == "XMIN":
            value = float('inf')
            for action in self.actions(state):
                value = min(value, self.Minimax(self.result(state,action)))
            return value
        
        if self.player(state) == "OMAX":
            value = float('-inf')
            for action in self.actions(state):
                value = max(value, self.Minimax(self.result(state,action)))
            return value
        