"""
There is a specific way to calculate such conditional probabilities that is particularly useful in many applications, namely the Bayes rule. 
The often-used formula for the Bayes rule is:

  P(A|B) = (P(B|A) * P(A)) / P(B)

Level - Beginner
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
"""
Level - Intermediate

Let's suppose you have a social media account on Instagram, Twitter, or some other platform (just in case you don't, it doesn't matter. 
We'll fill you in with the relevant information). 
You check your account and notice that you have a new follower – this means that another user has decided to start following you to see things that you post. 
You don't recognize the person, and their username (or "handle" as it's called) is a little strange: John37330190. You don't want to have creepy bots following you, 
so you wonder whether to block them. To decide whether you should block the new follower, you decide to use the Bayes rule!

Let's assume that 5% of your new followers are bots: this can be written as

P(bot) = 0.05.
Let's also assume that 80% of bot accounts have a username that includes an 8-digit number (like 37330190):

P(8-digits | bot) = 0.8
The last term that is required is the probability, P(8-digits), which is the probability that a new follower (either a bot or not) has an 8-digit number in their username. 
This probability would be quite hard to know or estimate directly. 
Instead, we may just know that real people who follow you usually don't have such a sequence in their username, so perhaps we have:

P(8-digits | human) = 0.01.
The nice thing is that we can now calculate P(8-digits) from the above information. 
The formula may look a little nasty at first sight, unless you're familiar with probability calculus, but it's quite friendly if you approach it with a smile:

P(8-digits) = P(8-digits | bot) x P(bot) + P(8-digits | human) x P(human)
The last term P(human) must be 0.95 since the other option (bot) has probability 0.05. Plug the number into the above formula to calculate the probability P(8-digits):

Ans: 0.0495

Lastly, calculate the probability that the new follower is a bot, P(bot | 8-digit), using the Bayes rule. 
The values of the three terms that are needed are found above. Choose the right answer (rounded up to four decimal digits):

Ans: 0.8081

"""
"""
Advanced Level

Let's suppose you have a social media account on Instagram, Twitter, or some other platform. (Just in case you don't, it doesn't matter. 
We'll fill you in with the relevant information.) You check your account and notice that you have a new follower – this means that another 
user has decided to start following you to see things that you post. You don't recognize the person, and their username 
(or "handle" as it's called) is a little strange: John37330190. You don't want to have creepy bots following you, so you wonder. 
To decide whether you should block the new follower, you decide to use the Bayes rule!

Suppose we know the probability that a new follower is a bot. You'll be writing a program that takes this value as an input. For now, 
let's just call this value P(bot). You'll also be given the probability that the username of a bot account includes an 8-digit number, 
which we'll call P(8-digits | bot), as well as the same probability for human (non-bot) accounts, P(8-digits | human).

To use the Bayes rule, we'll also need to know the probability that a new follower (can be either bot or human) has an 8-digit number in their username,
P(8-digits). The nice thing is that we can calculate P(8-digits) from the above information. The formula is as follows:

P(8-digits) = P(8-digits | bot) x P(bot) + P(8-digits | human) x P(human)
Remember that you can get P(human) simply as 1–P(bot), since these are the only options. 
(We consider business and other accounts as "human" as long as they aren't bots.)

Write a program that takes as input the probability of a follower being a bot (pbot), 
the probability of a bot having a username with 8 digits (p8_bot), and the probability of a human having a username with 8 digits (p8_human). 
The values for these inputs are free for you to choose, but they have to be probabilitites, so they have to be between 0 and 1.

Using the numbers you give the program calculate P(8-digits) and then use it and the Bayes rule to calculate and 
print out the probability of the new follower being a bot, P(bot | 8-digits):

P(bot | 8-digits) =  P(8-digits | bot) x P(bot) / P(8-digits).
"""

def bot8(pbot, p8_bot, p8_human):
    phuman = 1 - pbot
    p8_digit = (p8_bot*pbot) + (p8_human*phuman)
    pbot_8 = (p8_bot*pbot) / p8_digit
    print(pbot_8)
    
    #output 0.64

pbot = 0.1
p8_bot = 0.8
p8_human = 0.05

bot8(pbot, p8_bot, p8_human)

