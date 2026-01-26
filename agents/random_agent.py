from agents.agent import Agent
import random

class RandomAgent(Agent):
    def action(self,x_state,o_state,state):
        actions = self.actions(state)
        action = random.choice(actions)
        return action

