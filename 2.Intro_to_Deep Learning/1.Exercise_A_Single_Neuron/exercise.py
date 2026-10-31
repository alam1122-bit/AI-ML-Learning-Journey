import tensorflow as tf
import matplotlib.pyplot as plt

model = keras.Sequential([
    layers.Dense(1, input_shape=[1]),
])

x = tf.linspace(-1.0, 1.0, 100)
y = model.predict(x)

plt.figure(dpi=100)
plt.plot(x, y, 'k')
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.xlabel("Input: x")
plt.ylabel("Target y")
w, b = model.weights # you could also use model.get_weights() here
plt.title("Weight: {:0.2f}\nBias: {:0.2f}".format(w[0][0], b[0]))
plt.show()

'''
Input shape¶
How well can we predict a wine's perceived quality from the physiochemical measurements?

The target is 'quality', and the remaining columns are the features. How would you set the input_shape parameter for a Keras model on this task?
'''
# YOUR CODE HERE
input_shape = [11]

# Check your answer
q_1.check()

'''
2) Define a linear model
Now define a linear model appropriate for this task. Pay attention to how many inputs and outputs the model should have.
'''

from tensorflow import keras
from tensorflow.keras import layers

# YOUR CODE HERE
model = keras.Sequential([
    layers.Dense(units=1, input_shape=[11])
])

# Check your answer
q_2.check()

'''
3) Look at the weights
Internally, Keras represents the weights of a neural network with tensors. Tensors are basically TensorFlow's version of a Numpy array with a few differences that make them better suited to deep learning. One of the most important is that tensors are compatible with GPU and TPU) accelerators. TPUs, in fact, are designed specifically for tensor computations.

A model's weights are kept in its weights attribute as a list of tensors. Get the weights of the model you defined above. (If you want, you could display the weights with something like: print("Weights\n{}\n\nBias\n{}".format(w, b))).

'''

# YOUR CODE HERE
w, b = model.weights
print("Weights\n{}\n\nBias\n{}".format(w, b))
# Check your answer
q_3.check()
