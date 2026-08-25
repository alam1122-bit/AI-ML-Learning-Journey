"""
We have two dice in our desk drawer. One is a normal, plain dice with six sides. Each of the sides comes up with an equal 1/6 probability. 
The other one is a loaded dice that also has six sides, but that however gives the outcome six on every second try on average. 
That means the probability that you get a six is 16.7% with the first dice but 50% with the second dice.

Suppose that we pick one of the dice at random so that both have the same chances of being picked, then start rolling the same dice again and again. 
If the outcome is six on the first roll, you wouldn't be very sure it's the loaded dice. 
If the outcome is also six on the second roll, you'd start thinking it probably is. After the third six, you'd start to be quite convinced.

If the outcome keeps being six, how many rolls would it take altogether (counting from the start) until the odds are at least 100:1 in favor of the loaded dice?

Tip: use the likelihood ratio (r) discussed above. In this case, r = P(6 | loaded) / P(6 | normal).

Select the correct answer
ans: 5
"""
