from agents.agent import Agent
import random


class RandomAI(Agent):
    def play(self,state):
        actions = self.actions(state)
        best_action = random.choice(actions)
        return best_action
