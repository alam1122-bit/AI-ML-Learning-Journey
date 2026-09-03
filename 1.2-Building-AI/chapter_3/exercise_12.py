"""
Exercise 12: Least squares

Level - Beginner

Suppose we have a data set of three points in the format of (x, y): (0, 5), (2, 9.6), and (3.2, 13.6). Your colleagues have built three different models to fit the data, 
all of the form y = a + b*x. They have given you the coefficients of their models, and they are as follows:

a) a=0.5, b=3.2

 b) a=0, b=1.9

c) a=7.6, b=1.9

Which of the coefficients gives the smallest squared error? You can use the "Beginner Exercise Dataset" in the above widget to help you calculate the error!

Select the correct answer : c) a=7.6, b=1.9

"""
"""
Level - Intermediate
Modify the program so it implements the calculation of the squared error. 
In other words, you should calculate the predicted prices for all the cabins in the data, 
subtract the predicted price from the actual price (which is given in the data), square the difference, and add them all up.

The program needs to work for any number of cabins and cabin features.
"""
import numpy as np

X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])
c = np.array([3000, 200 , -50, 5000, 100])    # coefficient values
 
def squared_error(X, y, c):
    sse = 0.0
    pred_y = 0.0
    for xi, yi in zip(X, y):
       pred_y = (xi @ c)
       sse += (yi - pred_y) ** 2
    print(sse)

squared_error(X, y, c)

"""
Level -  Advance

Write a program that calculates the squared error for multiple sets of coefficient values and prints out the index of the set that yields the smallest squared error: 
this is a poor man's version of the least squares method where we only consider a fixed set of alternative coefficient vectors instead of finding the global optimum.
"""

import numpy as np

# data
X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array([[3000, 200 , -50, 5000, 100], 
              [2000, -250, -100, 150, 250], 
              [3000, -100, -150, 0, 150]])   

def find_best(X, y, c):
    smallest_error = np.Inf
    best_index = -1
    for index, coeff in enumerate(c):
        sse = np.sum((y - (X @ coeff)) ** 2)
        if sse < smallest_error:
            smallest_error = sse
            best_index = index
    print("the best set is set %d" % best_index)


find_best(X, y, c)
