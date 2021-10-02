import math


def f(x):
    """Computes function value for given input x

    Args:
        x (float): The input value to compute value of function f at point x
    """
    op = 0.0
    # This function is taken for demonstration purposes
    op = 3*x + math.sin(x) - math.exp(x)

    return op

def bisection(x_l,x_r,counter, x_prev = 0.0, tol = 0.0001,iterations = 10):
    """This method computes the root of a non-linear equation (if exists) given the interval by halving the
       interval at each iteration to narrow down to the root

    Args:
        x_l (float): Left end of interval under consideration
        x_r (float): Right end of interval under consideration
        counter (integer): Variable that keeps track of iterations
        x_prev (float, optional): Keeps track of previous midpoint to compute error (used only after first iteration)
        tol (float, optional): Tolerance value to stop the iterations(Taken as 0.01% by default)
        iterations (integer, optional): Number of iterations to be performed
    """
    x_new = (x_l + x_r)/2
    counter += 1
    print("Iteration",counter,": x_l= ",x_l,", x_r= ",x_r,", x_new= ",x_new)
    if(f(x_new)*f(x_l)<0):
        x_r = x_new
    else:
        x_l = x_new
    
    # flag = 0  
    if((abs(x_prev - x_new)<tol) or (counter >= iterations)):
        print("The root for the given function is: ",x_new)
    else:
        bisection(x_l,x_r,counter,x_new,tol,iterations)           

    
print("Enter two integers a an b")
a,b = map(int, input().split())
# a = 0
# b = 1
counter = 0
if(f(a)*f(b)>0):
    print("No root exists in the interval (", a, ", ", b, ")")
else:
    bisection(a,b,counter,a-1,0.001,5)




