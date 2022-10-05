# fibonacci=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
# lucas = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843]

def fibonacci(n):
   
   
    if n < 0:
        print("please enter a positive integer")
 
    
    elif n == 0:
        return 0
 
    
    elif n == 1 or n == 2:
        return 1
 
    else:
        return fibonacci(n-1) + fibonacci(n-2)
 
def lucas (c) :
    if c < 0:
        print("please enter a positive integer")
 
    
    elif c == 0:
        return 2
 
    
    elif c == 1 :
        return 1
 
    
    return lucas(c-1) + lucas(c-2)

def sum_series(x,a=0,b=1) :
    if x ==1 :
        return b
    if x==0 :
        return a
    return sum_series(x-1,a,b)+sum_series(x-2,a,b)

    

