import sys
import sympy
from sympy import *
from sympy.logic.boolalg import to_dnf
from sympy.logic import SOPform
from sympy.logic import POSform
from sympy.logic import boolalg
from sympy.logic.boolalg import And, Or, Not, Xor, Nand, Nor, Implies, Equivalent, truth_table

def processEq(booleanexpr, Vars):
    if(len(Vars) == 4):
        print("HI")
    return 0



if __name__ == '__main__':
    #boolean_equation = input('What is the boolean equation?')

    runprog = 0
    NonsingleVars = []
    myoutputs = {}
    while(runprog != 1):
        commandin = input('What would you like to do?')
        match commandin:
            case "1":
                runprog = 0
                Variables = []
                boolean_equation = input('What is the boolean equation?') 
                a = boolean_equation.split('=')
                myout = a[0]
                varmaker = a[1]
                NonsingleVars.append(myout)
                for subber in NonsingleVars:
                    if subber in varmaker:
                        Variables.append(subber)
                        varmaker = varmaker.replace(subber, ' ')
                for char in varmaker:
                    if char not in ['(',')','+','*','!','&','|', ' ', '~']:
                        if char not in Variables:
                            Variables.append(char)
                Variables = sorted(Variables)
                myoutputs[myout] = {}
                myoutputs[myout]['Variables'] = Variables
                myoutputs[myout]['RAWEquation'] = a[1]
                bool2 = sympify(a[1])
                bool3 = simplify_logic(bool2)
                mytruth = truth_table(bool3, Variables, input=False)
                myoutputs[myout]['Equation'] = bool3
                newtruth = []
                x = 0
                for t in mytruth:
                    newtruth.append(t)
                    x += 1
                myoutputs[myout]['TruthTable'] = newtruth
                #print(myoutputs)
            case "12":
                break
    print(myoutputs)