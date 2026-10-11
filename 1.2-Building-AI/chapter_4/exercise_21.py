'''
  Level - Beginner

  Inputs                    Hidden Layer       Output

  [1.3] ------ [-0.76] -------> \
                                 \
  [-2.2] ----- [0.22] ---------> ( a1 ) ----\
                                 /         \
  [ 9.5] ----- [0.56] --------> /           \
                                             \
  [ ... ] ---------------------> ( a2 ) ------> [ O ] ---->
                                             /
  [ ... ] ---------------------> ( a3 ) ----/
                                 /
  [ ... ] ---------------------> ( a4 )

Consider the neural network in the picture above. How many input nodes does it have?
ans: 3

What about hidden nodes?
ans: 4

Let’s focus on the hidden nodes. What is the value of the linear combination in node a_1 before an activation function is applied to it?
ans: 3.848

If we choose to use the identity function as the activation function, what would be the output of this node?
ans: 3.848

If your final task would be to predict based on the height, weight, and length if a thing is a dog or a cat, 
what would you choose to be the activation function for the output layer?
ans: sigmoid, since the output will be a probability of it being one of them

If we choose to use a sigmoid activation function, what would be the output of this node?
ans: ~0.98

'''


