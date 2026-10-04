'''
Exercise 19: Looking out for overfitting

Level - Beginner

Let’s for a moment imagine you have a data set on 1000 email messages labeled as either spam or not. Out of the 1000 messages, 990 are legitimate emails, and 10 are spam.

Then you split your data into training and test sets in such a way that both labels are present in both sets in equal ratios, and then train a classifier on the data.

What would you set as the baseline accuracy that your model has to outperform in order to be considered worthwhile?

Select the correct answer

ans: 99% accuracy

'''
'''
Level - Intermediate

The program below uses the so called k-nearest neighbors algorithm. The idea is to not only look at the single nearest training data point (neighbor) but for 
example the five nearest points, if k=5. The normal nearest neighbor classifier amounts to using k=1.

The program does the classification for some value of k and outputs an image that shows how the different things are classified. 
Modify the program so that the program prints out the training and testing accuracy and make it possible to use different values for k.

Hint: You can get the model accuracy using function knn.score. For example: knn.score(x_train, y_train) returns the training set accuracy after you 
have first created the classifier by calling knn.fit(x_train, y_train).

Try different values of k to answer the questions below.
'''
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import numpy as np

# create fake data
x, y = make_moons(
    n_samples=500,  # the number of observations
    random_state=42,
    noise=0.3
)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

# Create a classifier and fit it to our data
knn = KNeighborsClassifier(n_neighbors=133)
knn.fit(x_train, y_train)
train_acc = knn.score(x_train, y_train)

print("training accuracy: %f" % train_acc)
test_acc = knn.score(x_test, y_test)
print("testing accuracy: %f" % test_acc)

