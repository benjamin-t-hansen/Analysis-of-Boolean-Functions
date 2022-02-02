import numpy as np
import boolean_functions
import functionals
import bit_strings

def get_chernoff_sample_size(delta, epsilon):
  '''Calculates the number of samples needed to estimate Fourier coefficents to
  an accuracy of epsilon with a probability at least delta. 
  Based on the multiplicative Chernoff bound:
   (basis*f+1)/2 is a Bernoulli random variable.  For example use 
   Theorem 3.1. from
   https://math.uchicago.edu/~may/REU2019/REUPapers/Rajani.pdf 


   Args:
    delta: float in the interval (0, 1)
    epsilon: float in the interval (0, inf)

  Returns:
    A numpy.float64 
  '''

  if not (0<delta <1) or not (0 <epsilon):
    ValueError("delta or epsilon incorrectly specified.")
  n_samples = int(np.ceil(3/4 * np.log(2/delta)/(epsilon ** 2)))
  prob = "{:.4f}".format(1-delta)
  print(str(n_samples) +''' samples are need to obtain an accuracy of epsilon 
  for each Fourier coefficient with a probability at least ''' + prob + '.')
  return n_samples

def get_fourier_transform_est(fun,n, S_pop = None, n_samples = None, delta = None, epsilon = None):
  ''' Computes the estimated Fourier coefficent for for all Basis functions associated 
  to an element of S_pop.  If n_samples is not specified, delta and epsilon must
  be specified to estimate the Fourier coefficents to an accuracy of epsilon with 
  a probability at least delta.  The value of the fuction fun is caculated only 
  once per sample.
  
  Computational bottleneck.  Goal to implement Walsh–Hadamard Transform.

   Args:
    fun: function on [-1,1] valued numpy.array 
    n: dimension of the input 
    S_pop: a [-1,1] valued numpy.ndarray with dimesion of axis 1 equal to n
          if specified.
    n_samples: int, the number of samples 
    delta: float in the interval (0, 1) if specified
    epsilon: float in the interval (0, inf)  if specified

  Returns:
    A numpy.array  of length n
  '''
  
  if S_pop is None:
    S_pop = bit_strings.gen_bit_strings(n)
  if n_samples is None:
    n_samples = get_chernoff_sample_size(delta, epsilon)
    if n_samples> 2**n:
      print("Should just sample every possible input if possible")
  transform = np.empty(len(S_pop))
  bit_string_sample = np.random.choice(np.array([-1,1]), size = (n_samples, n))
  fun_values = functionals.apply_function(fun,bit_string_sample)
  for index, S in enumerate(S_pop):
    basis_fun = lambda x: boolean_functions.Basis(x,S)
    basis_values = functionals.apply_function(basis_fun, bit_string_sample)
    transform[index] = np.dot(fun_values, basis_values)/n_samples
  return transform
  
