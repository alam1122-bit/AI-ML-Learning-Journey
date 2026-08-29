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
    for xi, yi in zip(X, y):
        # add your code here: calculate the predicted price,
        # subtract it from the actual price yi, 
        # square the difference using (yi - prediction)**2, 
        # and add up all the differences in variable sse
        pass

    print(sse)

squared_error(X, y, c)

