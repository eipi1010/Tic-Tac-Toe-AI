import numpy as np

def visualise(x,o):
    # ANSI Color codes
    BLUE = "\033[94m"
    RED = "\033[91m"
    RESET = "\033[0m"
    
    visual_state = ["0","1","2","3","4","5","6","7","8"]
    x_string = format(x,'09b')
    o_string = format(o,'09b')
    
    for i in range(len(visual_state)):
        if x_string[i] == '1':
            # Wrap X in Blue
            visual_state[i] = f"{BLUE}X{RESET}"
        elif o_string[i] == '1':
            # Wrap O in Red
            visual_state[i] = f"{RED}O{RESET}"
    
    print("\n" + "-"*13)
    for row_start in range(0, 9, 3):
        row = visual_state[row_start:row_start+3]
        print(f"| {' | '.join(row)} |")
        print("-"*13)







