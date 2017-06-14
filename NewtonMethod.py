from sympy import sympify

def NewtonMethod(xone,repeat):
    function = str(input('What is the full funtion? Please use "**" for powers'))
    while repeat > 0:
        x=xone
        Sfunction = sympify(function)
        Dfunction = eval(str(Sfunction.diff('x')))
        
        results = (xone - ((eval(function))/(Dfunction)))
        print(results)
        xone = results
        repeat -=1
