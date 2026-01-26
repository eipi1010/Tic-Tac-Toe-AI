from agents.agent import Agent

class HumanAgent(Agent):
    def action(self,x_state,o_state,state):

        user_input = input("Enter number (0-8): ")
        while not self.legal(state, user_input):
            user_input = input("Enter valid number (0-8): ")

        action = int(user_input)

        return action
    

    
    


