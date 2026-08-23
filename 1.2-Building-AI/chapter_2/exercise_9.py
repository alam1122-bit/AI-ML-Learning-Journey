"""
Exercise 9: Block or not
Let's suppose you have a social media account on Instagram, Twitter, or some other platform (just in case you don't, 
it doesn't matter. We'll fill you in with the relevant information). 
You check your account and notice that you have a new follower – this means that another user has decided to start following you to see things that you post. 
You don't recognize the person, and their username (or "handle" as it's called) is a little strange: John37330190. You don't want to have creepy bots following you, 
so you wonder whether to block them. To decide whether you should block the new follower, you decide to use the Bayes rule!
Let's assume that 5% of your new followers are bots: this can be written as
P(bot) = 0.05.
Let's also assume that 80% of bot accounts have a username that includes an 8-digit number (like 37330190):
P(8-digits | bot) = 0.8
The last term that is required is the probability that a new follower (either a bot or not) has an 8-digit number in their username. Assume this to be:
P(8-digits) = 0.041.
Calculate the probability that the new follower is a bot, P(bot | 8-digit), using the Bayes rule: P(A | B) = P(B | A)P(A)/P(B). 
The values of the three terms that are needed are found above. Choose the right answer (rounded up to one decimal digit):

Ans: 97.6%

"""
