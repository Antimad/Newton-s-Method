from sympy import sympify
"""
    Solves the problem
    Xn+1 = Xn - (F(Xn)/F'(Xn))
"""

def NewtonMethod(xone,repeat):
"""
    xone = the initial x value
    repeat = how many iterations to get near the root of the function
"""
    function = str(input('type in full function, use x as the function variable'))
    while repeat > 0:
        x=xone
        Sfunction = sympify(function) 
        Dfunction = eval(str(Sfunction.diff('x'))) # Differentiates the function
        results = (xone - ((eval(function))/(Dfunction))) 
        print(results)
        xone = results
        repeat -=1
