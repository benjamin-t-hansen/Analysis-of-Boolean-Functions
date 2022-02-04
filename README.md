# Analysis of Boolean Functions
 This repository is designed to implement some aspects of the book [Analysis of Boolean Functions](https://arxiv.org/abs/2105.10386) by Ryan O’Donnell.  The current focus of this repo is aimed at providing a collection of some Boolean functions and implement some of the learning algorithms from Chapter 3; the former is ready to be used by students and the latter is not a production implementation (over sampling and slow evaluation). 

# What are Boolean Functions
We consider the collection of functions from {-1,1}^n to {-1,1} to be the possible Boolean functions.  For each n, there are 2^(n+1) such functions. These functions can be studied by examining their Fourier expansion.  Many of the functions we encounter are relatively simple and so can be approximated or learned by studying a relatively small number of the Fourier coefficients.  One of the main themes of O’Donnell's book is turning computational problems into analytical problems.

# Things in this repo

The [examples file](examples.py) is a great place to start after the README.  There are some examples of Boolean functions and one example of the low degree algorithm.  The majority function (Maj) returns the mode of the -1 and +1 votes:
Maj(-1,1,1,-1,1) = 1.

The current collection of [Boolean Functions](boolean_functions.py).

Explicitly calculating the [Fourier expansion](fourier_transform.py).

Estimating the [Fourier expansion](fourier_estimation.py).

A [general learning algorithm](learning.py) and one flavor of it (low degree algorithm).

