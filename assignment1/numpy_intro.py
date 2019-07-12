#!/usr/bin/env python
# coding: utf-8

import numpy as np

# In Machine Learning, often you will be given the values of x_1 ... x_n,
# as well as some output value y. It will be your job to determine the values of
# a_1 ... a_n such that a_1 * x_1 + a_2 * x_2 + ... + a_n * x_n will accurately predict
# the value of y. The process of predicting the a values is called linear regression.
#
# Each a_i coefficient represents something called a "feature weight". This
# signifies how strong the impact of variable x_i (a "feature") is in determining the value
# of the output of the function.
#
# For example, if the output variable is the price of a home, the feature set could include
# the age of the home, the size of the home's interior, the property tax rate, etc.
#
# TODO: Accepts d: the size of the feature set
#        Return: a numpy array of size d.
#        Each value in this array should be generated randomly from the 
#        standard normal distribution. This array represents a random 
#        set of "true" feature weights. This is the model our linear regression
#        will later attempt to predict.
#
# HINT: This should be 1 line of code. Look at numpy's random sampling library.
def createRandomVector(d):
    pass

# Often observed data will be provided to you as a matrix. The general convention is
# that each row in the matrix is a separate observed data point and each column in the matrix
# corresponds specific the values for a specific feature. So the value at row i and column j
# is the observed value for the feature j within data point i.
#
# TODO: Accepts a_true: A numpy array of arbitrary size d representing the "true" feature weights.
#       Accepts n: the number of data points you want to generate
#       Return: a numpy array X of dimensions n x d. Each value should be randomly
#       generated from the standard normal distribution. This represents your data matrix
#       Return: a numpy array y of size n. Value y_i should be generated by finding the dot
#       product of observed data x_i and the true feature weights with a random amount of error added.
#       The error should be randomly selected from a normal distribution with a mean of 0 and standard
#       deviation of 0.5. We do this to simulate how data in the real world isn't always clean...sometimes
#       the indicators could imply one output value when another is really correct.
#       
#
# HINT: Generating the data matrix should be very similar to createRandomVector()
# HINT: Think of the task of generating y as a series of matrix operations.
# HINT: In Python you can return multiple values.
# HINT: 3 lines of code, assuming you don't reimplement matrix operations.
def createRandomFeatureData(a_true, n):
    pass


# In Machine Learning often we need to evaluate the accuracy of our model (i.e. our predicted understanding
# of the world - in this case, our predicted feature weights) . We thus use some sort of
# "cost" function that evaluates our model and returns a number such that lower values imply a more
# accurate model and higher values imply a less accurate model. One common cost function is sum of squared errors.
# With this cost function, for each data point i, we find the difference between the real y_i and 
# the predicted y_i and square it. We then sum all these resulting values.
#
# Two things to observe about this cost function. By squaring the error, our cost function is affected only
# by the magnitude, not the direction of error (i.e. the cost function treats an error of +1 and -1 the same).
# Secondly, larger errors are penalized exponentially more than smaller errors (e.g. an error of 4 contributes
# 16 to the cost function, while an error of 2 only contributes 4).
#
# Cost functions are not only used to evaluate the model, but to build the model. Different cost functions lead
# to different models being built. Luckily for us, linear regression for the least squares regression cost function
# can be solved easily with matrix operations.
#
# TODO: Accepts X: An n x d numpy array where rows are data points and columns are features.
#       Accepts y: A vector where each index i corresponds to the output for data point i.
#       Return: a numpy array that consists of the predictions for the feature weights.  
#
# HINT: Look up "least-squares regression closed-form solution." You should be able to find the solution defined
#       in terms of matrix operations.
#
# HINT: This should be 4-6 lines of code, assuming you don't reimplement matrix operations.
def linearRegression(X, y):
    pass

# TODO: Accepts X: An n x d numpy array where rows are data points and columns are features
#       Accepts y: A vector where each index i corresponds to the output for data point i.
#       Accepts a_pred: The predicted set of feature weights our algorithm built.
#       Return: the sum of squared errors between what the model predicts for data point i and what
#       data point i's actual output is.
#
# HINT: I was able to do this in 1 line of code with 3 different numpy array/matrix operations. You can also
#       reimplement it, which would take a loop and around 5 lines of code.
def leastSquaresCostFunction(X, y, a):
    pass
    
d = 100
n = 1000
a_true = createRandomVector(d)
X, y = createRandomFeatureData(a_true, n)
model = linearRegression(X, y)
# The cost of the predicted model
print(leastSquaresCostFunction(X, y, model))
# The cost of a dummy model where all feature weights are predicted 0.
print(leastSquaresCostFunction(X, y, np.zeros((d, 1))))