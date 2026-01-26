import random
from visual_renderer import visualise
import numpy as np

WINNING_MASKS = [
    0b111000000,  # top row
    0b000111000,  # middle row
    0b000000111,  # bottom row
    0b100100100,  # left column
    0b010010010,  # middle column
    0b001001001,  # right column
    0b100010001,  # diagonal \
    0b001010100,  # diagonal /
]

class TicTacToe:
    def __init__(self, player_one, player_two, verbose=False):
        self.player_one = player_one
        self.player_two = player_two

        self.win_count_one = 0
        self.win_count_two = 0
        self.draw_count = 0
        self.verbose = verbose
        self.turn_order = 0

    def run(self, games):
        for _ in range(games):
            if self.verbose:
                print("-------- New Game ------------------")
            x = 0b000000000
            o = 0b000000000
            state = 0b000000000
            self.turn_order = random.randint(0, 1)
            
            # Determine who is X and who is O
            if self.turn_order == 0:
                x_player = self.player_one
                o_player = self.player_two
            else:
                x_player = self.player_two
                o_player = self.player_one
            
            if self.verbose:
                print(f"{x_player} plays X, {o_player} plays O")
                if self.turn_order == 0:
                    print(f"{x_player} goes first")
                else:
                    print(f"{o_player} goes first")
            
            while not self.is_game_over(x, o, state):
                visualise(x, o)
                x, o, state = self.turn(x, o, state)

            visualise(x, o)

        print(f"\nResults after {games} games:")
        print(f"{self.player_one} wins: {self.win_count_one} ({self.win_count_one/games*100:.1f}%)")
        print(f"{self.player_two} wins: {self.win_count_two} ({self.win_count_two/games*100:.1f}%)")
        print(f"Draws: {self.draw_count} ({self.draw_count/games*100:.1f}%)")

    def turn(self, x, o, state):
        turn_count = bin(state).count('1')
        if turn_count % 2 == self.turn_order:
            # Player 1's turn
            if self.verbose: 
                if self.turn_order == 0:
                    print(f"{self.player_one}'s Turn (X)")
                else:
                    print(f"{self.player_one}'s Turn (O)")
            action = self.player_one.action(x, o, state)
            x, o, state = self.player_one.play(x, o, state, action)
        else:
            # Player 2's turn
            if self.verbose:
                if self.turn_order == 0:
                    print(f"{self.player_two}'s Turn (O)")
                else:
                    print(f"{self.player_two}'s Turn (X)")
            action = self.player_two.action(x, o, state)
            x, o, state = self.player_two.play(x, o, state, action)
        
        return x, o, state

    def is_game_over(self, x_state, o_state, state) -> bool:
        x_win = any((x_state & mask) == mask for mask in WINNING_MASKS)
        o_win = any((o_state & mask) == mask for mask in WINNING_MASKS)
        draw = (bin(state).count('1') == 9)

        if x_win:
            # X won - figure out which player was X
            if self.turn_order == 0:
                # Player 1 was X
                if self.verbose: print(f"{self.player_one} (X) wins!")
                self.win_count_one += 1
            else:
                # Player 2 was X
                if self.verbose: print(f"{self.player_two} (X) wins!")
                self.win_count_two += 1
            return True
        elif o_win:
            # O won - figure out which player was O
            if self.turn_order == 1:
                # Player 1 was O
                if self.verbose: print(f"{self.player_one} (O) wins!")
                self.win_count_one += 1
            else:
                # Player 2 was O
                if self.verbose: print(f"{self.player_two} (O) wins!")
                self.win_count_two += 1
            return True
        elif draw:
            if self.verbose: print("Draw!")
            self.draw_count += 1
            return True
        
        return False




