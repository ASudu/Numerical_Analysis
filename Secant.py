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

def swap(x_0,x_1):
    if(abs(f(x_0)) < abs(f(x_1))):
        temp = x_1
        x_1 = x_0
        x_0 = temp
    else:
        pass
    return x_0, x_1

def secant(x_0,x_1,counter, x_prev = 0.0, tol = 0.0001,iterations = 10):
    """This method computes the root of a non-linear equation (if exists) given the interval by halving the
       interval at each iteration to narrow down to the root

    Args:
        x_0 (float): First initial point of method
        x_1 (float): Second initial point of method
        counter (integer): Variable that keeps track of iterations
        x_prev (float, optional): Keeps track of previous midpoint to compute error (used only after first iteration)
        tol (float, optional): Tolerance value to stop the iterations(Taken as 0.01% by default)
        iterations (integer, optional): Number of iterations to be performed
    """
    x_0, x_1 = swap(x_0,x_1)
    x_new = (x_0*f(x_1) - x_1*f(x_0))/(f(x_1) - f(x_0))
    counter += 1
    print("Iteration",counter,": x_0= ",x_1,", x_1= ",x_1,", x_new= ",x_new)
        
    # flag = 0  
    if((abs(x_prev - x_new)<tol) or (counter > iterations)):
        print("The root for the given function is: ",x_new)
    else:
        secant(x_1,x_new,counter,x_new,tol,iterations)
                  

    
print("Enter two integers a an b")
a,b = map(int, input().split())
# a = 0
# b = 1
counter = 0
if(f(a)*f(b)>0):
    print("No root exists in the interval (", a, ", ", b, ")")
else:
    secant(a,b,counter,a-1,0.001,5)
