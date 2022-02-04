import numpy as np
import boolean_functions

import fourier_transform
import fourier_estimation
import learning
import functionals

#Compute majority, a linear threshold function, tribes, basis


vote_1 = np.array([-1,1,1,-1,1])
outcome_1 = boolean_functions.Maj(vote_1)
outcome_2 = boolean_functions.Lin(vote_1,np.array([.8,0,-1,.6,.5]))

vote_2 = np.array([-1,-1,-1,-1,1,1])
outcome_3 = boolean_functions.Tribes(vote_2, w = 2)
outcome_4 = boolean_functions.Tribes(vote_2, w = 3)
outcome_5 = boolean_functions.Basis(vote_2, np.array([1,1,1,-1,-1,1]))

print(outcome_1) #1
print(outcome_2) #-1
print(outcome_3) #-1
print(outcome_4) #1
print(outcome_5) #-1

#compute Fourier transform and estimated Fourier transform.
ft = fourier_transform.get_fourier_transform(boolean_functions.Maj, n = 7)

fte = fourier_estimation.get_fourier_transform_est(boolean_functions.Maj, n = 7,
                                             delta = .2, epsilon = .3 )
print(ft)
print(fte)

#estimate f by h by repeated samples and the low deg algorithm
f = lambda x: boolean_functions.Lin(x,np.array([.8,0,1,.6,.5]))
h = learning.low_deg_algorithm(f, n = 5, delta = .2, epsilon = .3, is_monotone = True)

#compute the distance between the two functions
dist = functionals.relative_hamming_dist(f, h, n= 5)

print(dist) #random but should be near zero.