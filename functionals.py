import numpy as np
import bit_strings

def apply_function(fun, bit_string_sample):
  '''Applies function to each array in a ndarray (bit_string_sample) along the first axis

  Args:
    fun: function on [-1,1] valued numpy.array (Boolean function)
    bit_string_sample: [-1,1] valued ndarray with each input given along the first
    axis.
  
  Returns:
    A numpy.array where the i-th value is given by the evaluation of the function
    on the i-th sample. 
  '''  
  return np.apply_along_axis(fun, axis = 1, arr = bit_string_sample)


def inner_prod(fun1,fun2,n):
  '''Computes the inner product of the Boolean functions fun1 and fun2 according
  to Definition 1.3.

  Args:
    fun1, fun2: function on [-1,1] valued numpy.array 
    n: dimension of input
  
  Returns:
    np.float
  '''
  
  bit_string_pop = bit_strings.gen_bit_strings(n)
  fun1_v = apply_function(fun1,bit_string_pop)
  fun2_v = apply_function(fun2,bit_string_pop)
  return 2 ** (-n) * np.dot(fun1_v, fun2_v)

def relative_hamming_dist(fun1,fun2, n):
  '''Computes the relative Hamming distance (Definition 1.10) between two functions
  using Proposition 1.9. P(f(x) != g(x)) 
  
  Args:
    fun1, fun2 : function on [-1,1] valued numpy.array 
    n: dimension of input 
    
  Returns:
    np.float
  '''  
  return (1- inner_prod(fun1,fun2,n))/2

