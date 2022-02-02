import numpy as np
import boolean_functions
import functionals
import bit_strings


def get_fourier(fun,S):
  '''Computes Fourier coefficient for fun on S based on Proposition 1.8.
  
  Args:
    fun: function on [-1,1] valued numpy.array 
    S: [-1,1] valued numpy.array S[i] = 1 iff i is in the set "S"

  Returns:
    A numpy.float64 
  '''

  n = len(S)
  basis_fun = lambda x: boolean_functions.Basis(x,S)
  return functionals.inner_prod(fun,basis_fun,n)

def get_fourier_transform(fun,n):
  '''Computes all Fourier coefficients for fun.  Note Fast Walsh–Hadamard Transform
  is a better implementation for large n.
  
  Args:
    fun: function on [-1,1] valued numpy.array 
    n: dimension of the input arrays

  Returns:
    A numpy.array of length n 
  '''

  S_pop = bit_strings.gen_bit_strings(n) #generates all possible "sets" S 
  transform = np.empty(len(S_pop))
  for index, S in enumerate(S_pop):
    transform[index] = get_fourier(fun,S)
  return transform
