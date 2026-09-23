'''
Exercise 16: Nearest neighbor
The program below uses the library sklearn to generate a random dataset. You don't need to be familiar with sklearn, we explain all the necessary information below. 
Each sample in the dataset has two input features X and one binary output class y. We can think of a sample as a cabin, with its size and price as its input features, 
and whether we like it (1) or not (0) as its output class.

The program's goal is to classify the cabins based on their nearest neighbor's class. 
That is, predict whether we would like a cabin based on our opinion of another cabin with the most similar input features.

The program first generates the random dataset and splits it into training and test sets. Then, for each cabin in the test set, 
it identifies its nearest neighbor from the cabins in the train set using the distance function. However, 
the program has very high standards and dislikes all the cabins y_predict[i] = 0.

Your goal is to make the program smarter by predicting the output class (y_predict) 
for each cabin in the test set based on the output class (y_train) of its nearest neighbor.
'''
# Level - Intermediate
