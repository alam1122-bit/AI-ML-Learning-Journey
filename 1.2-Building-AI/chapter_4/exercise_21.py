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
'''
Level - Intermediate

We have trained a simple neural network with a larger set of cabin price data. The network predicts the price of the cabin based on the attributes of the cabin. 
The network consists of an input layer with five nodes, a hidden layer with two nodes, a second hidden layer with two nodes, and finally an output layer with a single node. 
In addition, there is a single bias node for each hidden layer and the output layer.

The program below uses the weights of this trained network to perform what is called a forward pass of the neural network. 
The forward pass is running the input variables through the neural network to obtain output, in this case the price of a cabin of given attributes.

The program is incomplete though. The bias nodes are not used in the version below, and the activation functions for the hidden layers and 
the output layer have not been properly defined.

Modify the program to use the bias nodes, and to use the ReLU activation function for the hidden nodes, and a linear (identity) activation for the output node. 
ReLU activation function returns either the input value of the function, or zero, whichever is the largest, and linear activation just returns the input as output. 
After these are done, get a prediction for the price of a cabin which is described by the following feature vector [74, 5, 10, 2, 100].

'''
import numpy as np

w0 = np.array([[ 1.19627687e+01,  2.60163283e-01],
               [ 4.48832507e-01,  4.00666119e-01],
                              [-2.75768443e-01,  3.43724167e-01],
                   [ 2.29138536e+01,  3.91783025e-01],
                   [-1.22397711e-02, -1.03029800e+00]])

w1 = np.array([[11.5631751 , 11.87043684],
                   [-0.85735419,  0.27114237]])

w2 = np.array([[11.04122165],
                   [10.44637262]])

b0 = np.array([-4.21310294, -0.52664488])
b1 = np.array([-4.84067881, -4.53335139])
b2 = np.array([-7.52942418])

x = np.array([[111, 13, 12, 1, 161],
                 [125, 13, 66, 1, 468],
                 [46, 6, 127, 2, 961],
                 [80, 9, 80, 2, 816],
                 [33, 10, 18, 2, 297],
                 [85, 9, 111, 3, 601],
                 [24, 10, 105, 2, 1072],
                 [31, 4, 66, 1, 417],
                 [56, 3, 60, 1, 36],
                 [49, 3, 147, 2, 179]])
y = np.array([335800., 379100., 118950., 247200., 107950., 266550.,  75850.,
                93300., 170650., 149000.])


def hidden_activation(z):
    # ReLU activation. fix this!
        return np.maximum(0,z)

def output_activation(z):
    # identity (linear) activation. fix this!
        return z

x_test = [[72, 2, 25, 3, 450], [60, 3, 15, 1, 300], [74, 5, 10, 2, 100]]
for item in x_test:
    h1_in = np.dot(item, w0) + b0 # this calculates the linear combination of inputs and weights. it is missing the bias term, fix it!
    h1_out = hidden_activation(h1_in) # apply activation function
    
    h2_in = np.dot(h1_out, w1) + b1 # the output of the previous layer is the input for this layer. it is missing the bias term, fix it!
    h2_out = hidden_activation(h2_in)
    
    out_in = np.dot(h2_out, w2) + b2
    out = output_activation(out_in)
    print(out)

'''
Output
[231177.31750927]
[184784.0147384]
[233890.02420755]
'''

'''
What price does the neural network predict for the cabin in question?
ans: roughly 230,000 euros

What type of a machine learning problem is this?
ans: supervised learning

How can we make sure we are not overfitting the neural network to the data?
ans: use cross-validation

'''

'''
Level - Advanced

We have trained a simple neural network with a larger set of cabin price data. The network predicts the price of the cabin based on the attributes of the cabin. 
The network consists of an input layer with five nodes, a hidden layer with two nodes, a second hidden layer with two nodes, and finally an output layer with a single node. 
In addition, there is a single bias node for each hidden layer and the output layer.

The program below uses the weights of this trained network to perform what is called a forward pass of the neural network. The forward pass is running the 
input variables through the neural network to obtain output, in this case the price of a cabin of given attributes.

The program is incomplete though. The program only does the forward pass up to the first hidden layer and is missing the second hidden layer and the output layer.

Modify the program to do a full forward pass and print out the price prediction. To do this, write out the remaining forward pass operations and use the 
ReLU activation function for the hidden nodes, and a linear (identity) activation for the output node. ReLU activation function returns either the input value of the 
function, or zero, whichever is the largest, and linear activation just returns the input as output. After these are done, get a prediction for the price of a 
cabin which is described by the following feature vector [82, 2, 65, 3, 516].

'''

import numpy as np

w0 = np.array([[ 1.19627687e+01,  2.60163283e-01],
               [ 4.48832507e-01,  4.00666119e-01],
                   [-2.75768443e-01,  3.43724167e-01],
                   [ 2.29138536e+01,  3.91783025e-01],
                   [-1.22397711e-02, -1.03029800e+00]])

w1 = np.array([[11.5631751 , 11.87043684],
                   [-0.85735419,  0.27114237]])

w2 = np.array([[11.04122165],
                   [10.44637262]])

b0 = np.array([-4.21310294, -0.52664488])
b1 = np.array([-4.84067881, -4.53335139])
b2 = np.array([-7.52942418])

x = np.array([[111, 13, 12, 1, 161],
                 [125, 13, 66, 1, 468],
                 [46, 6, 127, 2, 961],
                 [80, 9, 80, 2, 816],
                 [33, 10, 18, 2, 297],
                 [85, 9, 111, 3, 601],
                 [24, 10, 105, 2, 1072],
                 [31, 4, 66, 1, 417],
                 [56, 3, 60, 1, 36],
                 [49, 3, 147, 2, 179]])
y = np.array([335800., 379100., 118950., 247200., 107950., 266550.,  75850.,
                93300., 170650., 149000.])


def hidden_activation(z):
    # ReLU activation. fix this!
        return np.maximum(0,z)

def output_activation(z):
    # identity (linear) activation. fix this!
        return z

x_test = [[82, 2, 65, 3, 516]]
for item in x_test:
    h1_in = np.dot(item, w0) + b0 # this calculates the linear combination of inputs and weights
    h1_out = hidden_activation(h1_in) # apply activation function
    
    # fill out the missing parts:
    # the output of the first hidden layer, h1_out, will need to go through
    # the second hidden layer with weights w1 and bias b1
    
    h2_in = np.dot(h1_out, w1) + b1
    h2_out = hidden_activation(h2_in)
    # and finally to the output layer with weights w2 and bias b2.
    
    output_in = np.dot(h2_out, w2) + b2
    out = output_activation(output_in)
    # remember correct activations: relu in the hidden layers and linear (identity) in the output
    
    print(out)

'''
Output

[257136.43628059]

'''

'''
What price does the neural network predict for a cabin described by input vector [82, 2, 65, 3, 516] ?
ans: roughly 257,100 euros

What type of machine learning is this?
ans: supervised learning

How can we make sure we are not overfitting the neural network to the data?
ans: user cross-validation

'''



  

