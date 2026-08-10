"""
Exercise 4: Probabilities
Recall the program that prints out the word 'dog' with 20% probability. 
Modify the program so that it prints either the word 'dog' or the word 'cat' (but never both, because either you're a dog person or a cat person, but not both, right?)

Change the probability of the word 'dog' to be 80% probability (because apparently there are more dog lovers than cat lovers in the world) so that the probability of the word 
'cat' is 20%.
"""
# Intermediate Level

import random

def main():
    prob = 0.20
    if random.random() < prob:
        print('cat')
    else:
        print('dog')

main()

"""
Write a program that prints "I love" followed by one word: the additional word should be 'dogs' with 80% probability, 'cats' with 10% probability,
and 'bats' with 10% probability.

Here's an example output:
I love bats

"""
# Advance Level

import random

def main():

    number = random.random() 

    if (number < 0.8):
        favourite = 'dogs'
    elif (number < 0.9):
        favourite = 'cats'
    else:
        favourite = 'bats'

   # favourite = name  # change this
    print("I love " + favourite) 


main()






