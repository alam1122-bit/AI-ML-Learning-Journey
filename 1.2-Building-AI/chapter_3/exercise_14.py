'''
Exercise 14: Training data vs test data

Level: Intermediate

The program estimates the coefficients of a linear regression model (array c) from the following data:

size	size of the sauna	distance to water	number of indoor bathrooms	proximity of neighbors	actual price
cabin 1	25	2	50	1	500	127,900
cabin 2	39	3	10	1	1000	222,100
cabin 3	13	2	13	1	1000	143,750
cabin 4	82	5	20	2	120	268,000
cabin 5	130	6	10	2	600	460,700
cabin 6	115	6	10	1	550	407,000
Use the predicted coefficients to obtain price estimates for the following two cabins:

size	size of the sauna	distance to water	number of indoor bathrooms	proximity of neighbors	actual price
cabin 7	36	3	15	1	850	196000
cabin 8	75	5	18	2	540	290000
Note that the predicted prices will not be the same as the actual prices (which are given in the above table just for comparison – you won't need them in the exercise).
'''
import numpy as np

def main():
    np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
    x_train = np.array(
        [
            [25, 2, 50, 1, 500], 
            [39, 3, 10, 1, 1000], 
            [13, 2, 13, 1, 1000], 
            [82, 5, 20, 2, 120], 
            [130, 6, 10, 2, 600],
            [115, 6, 10, 1, 550 ]
        ]
    )   
    
    y_train = np.array([127900, 222100, 143750, 268000, 460700, 407000])

    # add the feature data for the two new cabins here. note: don't include the price data
    x_test = np.array(
        [
            [36, 3,	15,	1,	850],
            [75, 5, 18, 2, 540]
        ]
    )

    c = np.linalg.lstsq(x_train, y_train, rcond=-1)[0]

    # this will print the predicted prices for the six cabins in the training data
    # change this so that it predicts the prices of the two new cabins that are not
    # included in the training set

    print(x_test @ c)

main()

'''
Level: Advanced
Write a program that reads data about one set of cabins (training data), estimates linear regression coefficients based on it, then reads data about another set of cabins (test data), and predicts the prices in it. Note that both data sets contain the actual prices, but the program should ignore the prices in the second set. They are given only for comparison.


The contents of the sets are as follows.

training data
size	size of the sauna	distance to water	number of indoor bathrooms	proximity of neighbors	actual price
25	        2	                    50	                    1	                        500	            127900
39	        3	                    10	                    1	                        1000	        222100
13	        2	                    13	                    1	                        1000	        143750
82	        5	                    20	                    2	                        120	            268000
130	        6	                    10	                    2	                        600	            460700
115	        6	                    10	                    1	                        550	            407000

test data
size	size of the sauna	distance to water	number of indoor bathrooms	proximity of neighbors	actual price
36	            3	                15	                    1	                    850	                196000
75	            5	                18	                    2	                    540	                290000
You can read the data into the program the same way as in the previous exercise.

You should then separate the feature and price data that you have just read from the file into two separate arrays names x_train and y_train, so that you can use them as argument to np.linalg.lstsq.

The program should work even if the number of features used to describe the cabins differs from five (as long as the same number of features are given in each file).

The output should be the set of coefficients for the linear regression and the predicted prices for the second set of cabins.

'''

import numpy as np
from io import StringIO


train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''

def main():
    np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
    
    # Please write your code inside this function
    train_data = np.loadtxt(StringIO(train_string))
    test_data = np.loadtxt(StringIO(test_string))
    
    # read in the training data and separate it to x_train and y_train
    x_train = train_data[:, :-1]
    y_train = train_data[:, -1]
    
    # fit a linear regression model to the data and get the coefficients
    c = np.linalg.lstsq(x_train , y_train, rcond=None)[0]
    
    # read in the test data and separate x_test from it
    x_test = test_data[:, :-1]
    
    # print out the linear regression coefficients
    print(c)
    
    # this will print out the predicted prics for the two new cabins in the test data set
    print(x_test @ c)


main()
