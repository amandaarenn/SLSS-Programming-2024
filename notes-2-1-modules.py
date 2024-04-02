# Modules
# Author: Amanda
# 11 March 2024

import random

# Dmonstrate some parts of the random module.
# ramdo,.ramdom()->(0, 1.0]

def coin_flip():
    # Return either heads, tails or other?
    # Heads -- (0 - 0.5]
    # Tails -- (0.5 - 0.999999]
    # Other -- the rest
    result = random.random()

    if result < 0.5:
        return "Heads"
    elif result < 0.999999:
        return "Tails"
    else: 
        return "Other"

def main(): 
    # Repeat the coin flip 1000 times.
    # Keep track of heads, tails, and other.
    heads = 0
    tails = 0
    other = 0

    for _ in range(1_000_000):
        result = coin_flip()
        
        if result == "Heads":
            heads = heads + 1  #
        elif result == "Tails":
            tails += 1  # Increment
        else:
            other += 1 

    # Print the results.
    print(f"Heads: {heads}")
    print(f"Tails: {tails}")
    print(f"Other: {other}")

main()