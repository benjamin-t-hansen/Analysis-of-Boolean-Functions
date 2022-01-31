import numpy as np

def Maj(ary):
  '''Majority function: Returns majority for a [-1,1] valued array.
  
  Args:
    ary: A numpy array of -1's and 1's.
  
  Returns: 
    A numpy.float64 with value from the list [-1, 0, 1]
    -1 if the majority of values are -1
    0  if half the values are -1 
    1 if the majority of values are 1
  '''
  return np.sign(sum(ary))


def Dic(ary,i):
  '''Dictator Function: Returns the value in the i-th position (0-indexed) of a
  [-1,1] valued array.  
  
  Args:
    ary: A numpy array of -1's and 1's.
    i: The 0-index of the 'Dictator' 0 <= i <= len(ary)

  Returns: 
    A numpy.float64 with value from the list [-1, 1]
    -1 if the i-th value is -1
    1  if the i-th value is 1
  '''
  return ary[i]

def Lin(ary,weights, bias = 0):
  '''Linear threshold function: Returns sign of weighted average + bias.
  (Note that Maj and Dic are special cases of this function)

  Args:
    ary: A numpy array of -1's and 1's. (x_1, x_2, ..., x_n)
    weights: A numpy array of weights. (w_1, w_2, ..., w_n)
    bias: An int or float (b)
  
  Returns: 
    A numpy.float64 with value from the list [-1, 0, 1]
    -1 if x_1 * w_1 + ... + x_n * w_n + b < 0 
    0  if x_1 * w_1 + ... + x_n * w_n + b = 0 
    1  if x_1 * w_1 + ... + x_n * w_n + b > 0 
  '''
  return np.sign(np.dot(ary,weights)+bias)


def Tribes(ary, w = 2):
  '''Tribes function: Each element of a [-1,1] valued array is assigned to a tribe. 
  Each tribe member votes within the tribe.  If every member of at least one 
  tribe votes 1, the function returns 1.  Otherwise returns -1.

  Args:
    ary: A numpy array of -1's and 1's. 
    w: int number, the number of tribes.  len(ary)/w must be an integer. 
  
  Returns:
    A numpy.float64 with value from the list [-1, 1]
  '''

  ary01  =  (ary+1)/2  #all function need 0 for false and 1 for true
  ndary = np.split(ary01,w)
  vote_outcome = np.any(np.all(ndary, axis =1)) 
  #inner all checks if all members of a tribe voted 1 
  return 2* vote_outcome - 1 #function range is {-1,1}
