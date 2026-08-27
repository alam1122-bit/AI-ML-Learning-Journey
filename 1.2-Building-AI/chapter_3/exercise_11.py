"""
Level - Beginner

# input values for one mökkis: size, size of sauna, distance to water, number of indoor bathrooms, 
# proximity of neighbours
"""
x = [66, 5, 15, 2, 500]
c = [3000, 200 , -50, 5000, 100]     # coefficient values

prediction = c[0]*x[0] + c[1]*x[1] + c[2]*x[2] + c[3]*x[3] + c[4]*x[4]

print(prediction)
"""
You can use the above piece of code to calculate these, or use pen and paper.

What would the predicted price of a cabin be with the following details? Size: 85 m2, size of the sauna: 10m2, 
distance to a lake: 15m, number of indoor toilets: 1, distance to next door neighbor: 100m

Your answer is correct: 271250 eur 
What would the predicted price of a cabin be with the following details? Size: 155m2, size of the sauna: 15m2, distance to a lake: 5m, 
number of indoor toilets: 1, distance to next door neighbor: 200m.

Your answer is correct: 492450 euro
"""
# Level - Intermediate
# Edit the code so that it prints out the prices of multiple cabins in one go.

# input values for three mökkis: 
#  - size [m^2], 
#  - size of the sauna [m^2], 
#  - distance to water [m], 
#  - number of indoor bathrooms, 
#  - proximity of neighbors [m]
X = [[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]]

# coefficient values
c = [3000, 200 , -50, 5000, 100]

def predict(X, c):
    # write a loop that goes over the cabin data and for each cabin prints out 
    # the predicted price of the cabin you can assume that the number of inputs
    # and the number of coefficients are the same
    
    for i in range(len(X)):
        price = 0
        for j in range(len(c)):
            price += c[j] * X[i][j]
        print(price)

predict(X, c)



