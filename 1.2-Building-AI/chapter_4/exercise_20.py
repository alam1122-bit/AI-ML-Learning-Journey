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
