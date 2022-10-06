# fibonacci=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
# lucas = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843]
# branch
def fibonacci(n):
    """
    this fucntion returns the sum of the previous 2 indices 
    starting from 0 as the first index and 1 as the second
    """
   
   
    if n < 0:
        print("please enter a positive integer")
 
    
    elif n == 0:
        return 0
 
    
    elif n == 1 or n == 2:
        return 1
 
    else:
        return fibonacci(n-1) + fibonacci(n-2)
 
def lucas (c) :
    """
    this fucntion returns the sum of the previous 2 indices
    starting from 2 as the first index and 1 as the second
    """
    if c < 0:
        print("please enter a positive integer")
 
    
    elif c == 0:
        return 2
 
    
    elif c == 1 :
        return 1
 
    
    return lucas(c-1) + lucas(c-2)

def sum_series(x,a=0,b=1) :
    """
    this fucntion returns the sum of the previous 2 indices
    but with custom starting indices 
    calling this function with no optional parameters will produce numbers from the fibonacci series.
    calling it with the optional arguments 2 and 1 will produce values from the lucas numbers.
    calling it with any other arguments it will be another series 
    """
    if x ==1 :
        return b
    if x==0 :
        return a
    return sum_series(x-1,a,b)+sum_series(x-2,a,b)

    

