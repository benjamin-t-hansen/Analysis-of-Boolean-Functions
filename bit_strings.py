import numpy as np


class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]


@Memoize
def gen_bit_strings(n):
  '''Generates numpy ndarray containing all possible [-1,1] valued arrays with 
  each array given along the first axis. 

  Args:
    n: int number, the length of the arrays. 
  
  Returns:
    A numpy.ndarray with shape (2 ** n, n)  and values from the list [-1, 1]
     containing all possible [-1,1] valued arrays with each array given along 
     the first axis.
  '''
  if n == 1:
    result = np.array([[-1],[1]])
  else:
    sub_bit_strings = gen_bit_strings(n-1)
    bit_strings_neg = np.insert(sub_bit_strings,0,-1, axis = 1)
    bit_strings_pos = np.insert(sub_bit_strings,0,1, axis = 1)
    result = np.concatenate((bit_strings_neg, bit_strings_pos), axis =0)
  return result



def S_deg(n,deg):
  '''Generates numpy ndarray containing all possible [-1,1] valued arrays with 
  exactly deg ones. Each array is given along the first axis. 

  Args:
    n: int number, the length of the arrays. 
    deg: int number, the number of 1s in each array (deg <= n)
  
  Returns:
    A numpy.ndarray with shape (n choose deg, n) and values from the list [-1, 1].
    The  ndarray contains all possible [-1,1] valued arrays with 
    exactly deg ones. Each array is given along the first axis. 
  '''
  
  if (n== 1) & (deg ==1): 
    result = np.array([[1]])
  elif (deg == 0): 
    result = -1 * np.ones((1,n))
  else:
    sub_bit_strings_sub = S_deg(n-1,deg-1)
    bit_strings_pos = np.insert(sub_bit_strings_sub,0,1, axis = 1)
    result = bit_strings_pos
    if deg < n:
      sub_bit_strings_equal = S_deg(n-1,deg)
      bit_strings_neg = np.insert(sub_bit_strings_equal,0,-1, axis = 1)
      result = np.concatenate((bit_strings_neg, bit_strings_pos), axis =0)
  return result

def S_max_deg(n, deg):
  '''Generates numpy ndarray containing all possible [-1,1] valued arrays with 
  at most deg ones. Each array is given along the first axis. 

  Args:
    n: int number, the length of the arrays. 
    deg: int number, the max number of 1s in each array (deg <= n)
  
  Returns:
    A numpy.ndarray with  values from the list [-1, 1].
    The  ndarray contains all possible [-1,1] valued arrays with 
    at most deg ones. Each array is given along the first axis. 
  '''

  S_deg_range = [S_deg(n,k) for k in range(0, deg+1)]
  S_deg_range = np.concatenate(S_deg_range)
  return  S_deg_range



