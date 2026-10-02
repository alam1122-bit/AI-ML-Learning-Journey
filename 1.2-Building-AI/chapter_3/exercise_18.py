# Term Frequency Inverse Document Frequency (tf-idf)

'''
Exercise 18: TF-IDF

Level - Beginner

Let’s use Humpty Dumpty as our corpus:

Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall.
All the king's horses and all the king's men
Couldn't put Humpty together again.
(Remember, you can type the tf-idf equation into a search engine on your browser to do the calculation)

What is the term frequency for the word “Humpty” in line 1 of Humpty Dumpty?

ans: 1/6

What is the term frequency for the word “all” in line 3?

ans: 2/9


What is the document frequency for the word “Humpty”?

ans: 3/4

What is the tf-idf score for word “Humpty” in line 4 of Humpty Dumpty?

ans: ~0.02
'''

'''
Level - Intermediate 

Modify the following program to print out the tf-idf values for each document and each word. The following code calculates the tf and df values, 
so you'll just need to combine them according to the correct formula. There are three documents (sentences) and a total of eight terms (unique words), 
so the output should be three lists of eight tf-idf values each.

Hint: Exercise 17. Bag of Words as well as the other tiers of this exercise explain many relevant concepts in detail. 
If you're stuck, we would highly recommend you to check them out.
'''

# DATA BLOCK

text = '''he really really loves coffee
my sister dislikes coffee
my sister loves tea'''

import math

def main(text):
    # split the text first into lines and then into lists of words
    docs = [line.split() for line in text.splitlines()]
    # text.spitlines = [],[],[]
    # line.split = [..,...,..,],[...],[...]

    N = len(docs)

    # create the vocabulary: the list of words that appear at least once
    vocabulary = list(set(text.split()))


    df = {}
    tf = {}
    for word in vocabulary:
        # tf: number of occurrences of word w in document divided by document length
        # note: tf[word] will be a list containing the tf of each word for each document
        # for example tf['he'][0] contains the term frequence of the word 'he' in the first
        # document
        tf[word] = [doc.count(word)/len(doc) for doc in docs]
        # doc.count(word) count word appear in doc
        # "he" is appear one time
        # len of doc 5
        # so 1/5 = 0.2 in first iteration
        # now "he" for second doc then 3rd doc then comes second word and so on...

        # df: number of documents containing word w
        df[word] = sum([word in doc for doc in docs])/N
        # print(f"df[{word}] = {df[word]}")
    # loop through documents to calculate the tf-idf values
    for doc_index, doc in enumerate(docs):
        tfidf = []
        for word in vocabulary:
            # ADD THE CORRECT FORMULA HERE. Remember to use the base 10 logarithm: math.log(x, 10)
            tfidf_value = tf[word][doc_index] * math.log(1/df[word],10)
            
            tfidf.append(tfidf_value) 

        print(tfidf)

main(text)


'''
Level - Advanced

Let's combine two tasks: finding the most similar pair of lines and the tf-idf representation.

Write a program that uses the tf-idf vectors to find the most similar pair of lines in a given data set. You can test your solution with the example text below. 
Note, however, that your solution will be tested on other data sets too, so make sure you don't make use of any special properties of the 
example data (like there being four lines of text).

This exercise requires a bit more work than average but you should be able to benefit from what you have done in the previous exercises.

Hint: Exercise 17. Bag of Words as well as the other tiers of this exercise explain many relevant concepts in detail. If you're stuck, 
we would highly recommend you to check them out. When specifying dtype for np.empty, use float instead of np.float.
'''

