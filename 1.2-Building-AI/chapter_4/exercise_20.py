'''
Level - Beginner
Here we have a (fictional) graph of data about hours spent learning Python vs the chance of getting a raise within a year. 
If your friend has spent 70 hours learning Python, what are her chances of getting a raise within a year?

**1. Axes Description:**
* Y-Axis (Vertical): Probability of getting a raise (0% to 100%)
* X-Axis (Horizontal): Hours studied Python (10 to 100 hours)

**2. Visual ASCII / Dot Representation of the Sigmoid Curve:**

100% |                                     . . . . . . . . . . (Top Data Points at 100%)
     |                                  . .
 80% |                               . . 
     |                              . . 
 60% |                             . . 
     |                           . .  
 40% |                          . . 
     |                         . . 
 20% |                       . . 
     |                     . . 
   0%| . . . . . . . . . .                                                (Bottom Data Points at 0%)
     +-----------------------------------------------------------------------------------------
    10     20    30    40    50    60   70    80    90   100
                                Hours studied Python

  ans: at least 80%

'''

'''
Level - Intermediate 

Which of these implement a sigmoid function correctly? Select all of the correct implementations from below (more than one may apply).

Option A
def sigmoid(x):
	return 1 / 1+math.exp(-x)

Option B
def sigmoid(x):
	return 1 / (1 + math.exp(x))

Option C
def sigmoid(x):
	return 1 / (1 + math.exp(-x))

Option D
def sigmoid(x):
	x2 = -1.0*x
	a = math.exp(x2)
	nominator = 1
	denominator = 1 + a
	return nominator / denominator

Option E
def sigmoid(x):
	return 1 / (1 + 2.71**(-x))

ans: Option C anf Option D

'''
'''
Level - Advanced

You are given a set of three input values and you also have multiple alternative sets of three coefficients. 
Calculate the predicted output value using the linear formula combined with the logistic activation function.

Do this with all the alternative sets of coefficients. Which of the coefficient sets yields the highest sigmoid output?
'''

import math
import numpy as np

x = np.array([4, 3, 0])
c1 = np.array([-.5, .1, .08])
c2 = np.array([-.2, .2, .31])
c3 = np.array([.5, -.1, 2.53])

def sigmoid(z):
    # add your implementation of the sigmoid function here
    return 1/(1 + math.exp(-z))

z1 = np.dot(x,c1)
z2 = np.dot(x,c2)
z3 = np.dot(x,c3)
# calculate the output of the sigmoid for x with all three coefficients
s1 = sigmoid(z1)
s2 = sigmoid(z2)
s3 = sigmoid(z3)

print(f"c1 sigmoid: {s1}")
print(f"c2 sigmoid: {s2}")
print(f"c3 sigmoid: {s3}")

'''
Output
c1 sigmoid: 0.15446526508353473
c2 sigmoid: 0.45016600268752216
c3 sigmoid: 0.8455347349164652
'''

'''
Select the correct answer

ans: C3
'''
