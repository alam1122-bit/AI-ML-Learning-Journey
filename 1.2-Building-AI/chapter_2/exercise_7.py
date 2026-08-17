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









