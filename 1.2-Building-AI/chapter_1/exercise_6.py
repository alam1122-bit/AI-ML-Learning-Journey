"""
Exercise 6 (Beginner Level)
To understand what role temperature plays, it's worthwhile to pause here for a second to think about and answer the following questions:

Question-01: What happens when we increase the temperature value to a ridiculously large number?

ans: we accept all new solutions

Question-02: What happens if we set the temperature as close as possible to 0?

ans: we only accept new solutions when they are better than the current one

"""

"""
Exercise 6: Simulated Annealing (Intermediate Level)
1D simulated annealing: modify the program below to use simulated annealing instead of plain hill climbing. 
In simulated annealing the probability of accepting a solution that lowers the score is given by prob = exp(-(S_old - S_new)/T). 
Setting the temperature T and gradually decreasing can be done in many ways, some of which lead to better outcomes than others. 
A good choice in this case is for example: T = 2*max(0, ((steps-step*1.2)/steps))**3.

Running the code produces something like the following chart, where the black box marks the starting point. 
The code below uses the plain hill-climbing strategy to only go up towards a peak. The solution is marked by a red star. 
As you can see, the hill-climbing strategy tends to get stuck in local optima.

"""
# Solution
import math, random        	# just for generating random mountains                                 	 
import numpy as np

n = 10000 # size of the problem: number of possible solutions x = 0, ..., n-1

# generate random mountains                                                                               	 
def mountains(n):
    h = [0]*n
    for i in range(50):
        c = random.randint(20, n-20) # 20 <= x <= 980 e.g. 500
        w = random.randint(3, int(math.sqrt(n/5)))**2 # e.g 3,195  100
        s = random.random() # e.g .12
        h[max(0, c-w):min(n, c+w)] = [h[i] + s*(w-abs(c-i)) for i in range(max(0, c-w), min(n, c+w))]
        # h[400:600] = h[0]+ 480 for i in range(400:600)
    # scale the height so that the lowest point is 0.0 and the highest peak is 1.0
    low = min(h)
    high = max(h)
    h = [y - low for y in h]
    h = [y / (high-low) for y in h]
    return h

h = mountains(n)

# start at a random place
x0 = random.randint(1, n-1)
x = x0

# keep climbing for 5000 steps
steps = 5000

def main(h, x):
    n = len(h)
    # the climbing starts here
    for step in range(steps):
        # this is our temperature to to be used for simulated annealing
        # it starts large and decreases with each step. you don't have to change this
        T = 2*max(0, ((steps-step*1.2)/steps))**3

        # let's try randomly moving (max. 1000 steps) left or right
        # making sure we don't fall off the edge of the world at 0 or n-1
        # the height at this point will be our candidate score, S_new
        # while the height at our current location will be S_old
        x_new = random.randint(max(0, x-1000), min(n-1, x+1000))
        if h[x_new] > h[x]:
            x = x_new           # the new position is higher, go there
        else:
            if T > 0:
                prob =  math.exp( - ( h[x] - h[x_new])/T)  
                if random.random() < prob:
                    x = x_new          
    return x

x = main(h, x0)
print("ended up at %d, highest point is %d" % (x, np.argmax(h)))

"""
Advance Level:
Let's use simulated annealing to solve a simple two-dimensional optimization problem. The following code runs 50 optimization tracks in parallel (at the same time). 
It currently only looks around the current solution and only accepts moves that go up. Modify the program so that it uses simulated annealing.
Remember that the probability of accepting a solution that lowers the score is given by prob = exp(–(S_old - S_new)/T). 
Remember to also adjust the temperature in a way that it decreases as the simulation goes on, and to handle T=0 case correctly.
Your goal is to ensure that on the average, at least 30 of the optimization tracks find the global optimum (the highest peak).
If plotting the code takes too long, use this gist to plot the code locally on your computer. It should be significantly faster.
"""

