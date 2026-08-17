"""
Beginner 
Exercise 7: Flip the coin

When flipping a coin, you have two possible outputs – heads and tails.
What is the probability of getting two consecutive tails when tossing a coin?

ans: 0.25

What is the probability of getting four consecutive heads when tossing a coin?

ans: 0.0625

"""
"""
Exercise: Flip the coin (Intermediate Level)
Write a program that counts the number of occurrences of "11" in an input sequence of zeros and ones. 
The input of the program is just the sequence and it should return a single number, which is the number of occurrences of "11".

"""

def count11(seq):
   # define this function and return the number of occurrences as a number
    x = 0
    for i in range(len(seq) - 1):
        #print(seq[i])
        if seq[i] == 1 and seq[i+1] == 1:
               x = x + 1
        else:
            pass      
    return x

print(count11([0, 0, 1, 1, 1, 0])) # this should print 2


"""
Advance level

Write a program that generates 10000 random zeros and ones where the probability of one is p1 and the probability 
of zero is 1-p1 (hint: np.random.choice([0,1], p=[1-p1, p1], size=10000)), counts the number of occurrences of 5 consecutive ones ("11111") in the sequence, 
and outputs this number as a return value. 
Check that for p1 = 2/3, the count is close to 10000 x (2/3)^5 ≈ 1316.9.
"""

import numpy as np

def generate(p1):
    seq = np.random.choice([0 ,1],p = [1 - p1, p1],size=10000)
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1

    # seq = np.empty(10000)
    return seq

def count(seq):
    x=0
    for i in range(len(seq)-4):
        if seq[i] == 1 and seq[i+1] == 1 and seq[i+2] == 1 and seq[i+3] == 1 and seq[i+4] == 1:
            x = x + 1
    return x

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))

"""
The probability of "11111" at any given position in the sequence can be calculated as (2/3)^5 ≈ 0.13169. 
The number of occurrences is close to 10000 times this: 1316.9. To be more precise, the expected number of occurrences is about 0.13169 x 9996 ≈ 1316.3, 
because there are only 9996 places for a subsequence of length five in a sequence of 10000. The actual number will usually (in fact, with over 99% probability) 
be somewhere between 1230 and 1404. We check the solution allowing for an even wider margin that covers 99.99% of the cases.
"""





