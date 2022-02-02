import numpy as np
import fourier_estimation
import boolean_functions
import bit_strings


def learning_algorithm_A(fun, S_pop, delta, epsilon):
  size = len(S_pop)
  n = len(S_pop[0])
  epsilon1 = np.sqrt(epsilon)/( 2 * np.sqrt(size))
  delta1 = delta / size    #Uses the union bound
  fourier_coeff = fourier_estimation.get_fourier_transform_est(fun,n, S_pop, delta = delta1, epsilon = epsilon1)
  g = lambda x: np.sum([fourier_coeff[i] * boolean_functions.Basis(x, S_pop[i]) for i in range(len(S_pop))])
  h = lambda x: np.sign(g(x)) if g(x) != 0 else 1 #arbitrary assignment of g(x) = 0
  return h


def low_deg_algorithm(fun, n, delta, epsilon, deg = None, is_monotone = None):
  if (deg is None) and (is_monotone == True):
    deg = int(np.ceil(2 * (np.sqrt(n * 2/np.pi) + 1/(2*np.sqrt(n)))/epsilon) )
    if deg>n:
      deg = n
    print(deg)
  S_pop = bit_strings.S_max_deg(n,deg)

  return learning_algorithm_A(fun, S_pop, delta, epsilon)

