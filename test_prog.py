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
    boolean_equation = input('What is the boolean equation?')
    Variables = []
    myoutputs = {}
    
    a = boolean_equation.split('=')
    myout = a[0]
    for char in a[1]:
        if char not in ['(',')','+','*','!','&','|', ' ']:
            if char not in Variables:
                Variables.append(char)
    Variables = sorted(Variables)
    myoutputs[myout] = {}
    myoutputs[myout]['Variables'] = Variables
    myoutputs[myout]['Equation'] = a[1]
    bool2 = sympify(a[1])
    mytruth = truth_table(bool2, Variables, input=False)
    
    newtruth = []
    x = 0
    for t in mytruth:
        newtruth.append(t)
        x += 1
    myoutputs[myout]['TruthTable'] = newtruth
    print(myoutputs)