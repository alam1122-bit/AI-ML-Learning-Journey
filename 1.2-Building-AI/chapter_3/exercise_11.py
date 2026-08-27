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
