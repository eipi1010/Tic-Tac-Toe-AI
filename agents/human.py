from agents.agent import Agent

class Human(Agent):
    def play(self,x_state,o_state,state):
        '''
        x = int(x_state, 2)
        o = int(o_state,2)
        state = x | o
        state = format(state, '08b')
        
        
        
        '''
        turn_count = state.bit_count()

        user_input = input("Enter number (0-8): ")
        while not self.is_move_legal(state, user_input):
            user_input = input("Enter valid number (0-8): ")

        action = int(user_input)

        if turn_count % 2 == 1:
            mask = 0b1 << action
            x_state |= mask
        else:
            mask = 0b1 << action
            o_state |= mask

        state = x_state | o_state

        return x_state, o_state, state
    
    def is_move_legal(state:str,user_input:int) -> bool:
        if user_input.isdigit() and 0 <= int(user_input) <= 8:
            if state[user_input] == '0':
                return True
        
        return False


