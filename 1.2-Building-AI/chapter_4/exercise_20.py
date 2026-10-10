'''
Level - Beginner
Here we have a (fictional) graph of data about hours spent learning Python vs the chance of getting a raise within a year. 
If your friend has spent 70 hours learning Python, what are her chances of getting a raise within a year?

**1. Axes Description:**
* Y-Axis (Vertical): Probability of getting a raise (0% to 100%)
* X-Axis (Horizontal): Hours studied Python (10 to 100 hours)

**2. Visual ASCII / Dot Representation of the Sigmoid Curve:**

100% |                                               . . . . . . . (Top Data Points at 100%)
     |                                           . .
 80% |                                       . . 
     |                                   . . 
 60% |                               . . 
     |                           . .  (50% Probability Threshold around ~60-65 hours)
 40% |                       . . 
     |                   . . 
 20% |               . . 
     |           . . 
   0%| . . . . .                                                     (Bottom Data Points at 0%)
     +-----------------------------------------------------------------------------------------
    10      20      30      40      50      60      70      80      90     100
                                Hours studied Python

  ans: at least 80%

'''
