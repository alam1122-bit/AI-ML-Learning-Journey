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






