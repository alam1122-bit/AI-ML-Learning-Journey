"""
Let’s work with the acceptance probability above exp(–(S_old – S_new)/T).

Suppose our our current solution has a score of S_old = 205. Our new solution would have a score of S_new = 196

Using simulated annealing, there is a possibility for us to accept this new state even though it has a lower score than the current one.

In this situation, what would the temperature T need to be in order to choose this new state with a probability of at least 0.5?
"""
# Intermediate Level
# Ans: 13

"""
Suppose the current solution has score S_old = 150 and you try a small modification to create a new solution with score S_new = 140. In the greedy solution, 
this new solution wouldn't be accepted because it would mean a decrease in the score. In simulated annealing, 
the new solution is accepted with a certain probability as explained above.

Modify the accept_prob function so that it returns the probability of accepting the new state using simulated annealing. 
The program should take the two score values (the current and the new) and the temperature value as arguments.
"""
# Advance Level
import random
import math

def accept_prob(S_old, S_new, T):
    # this is the acceptance "probability" in the greedy hill-climbing method
    # where new solutions are accepted if and only if they are better
    # than the old one.
    # change it to be the acceptance probability in simulated annealing
    if S_new > S_old:
        return 1.0
    else:
        s = S_old - S_new
        return math.exp(- s / T)


# the above function will be used as follows. this is shown just for
# your information; you don't have to change anything here
def accept(S_old, S_new, T):
    if random.random() < accept_prob(S_old, S_new, T):
        print(True)
    else:
        print(False)

accept(150,140,20)

