import sys
import sympy
from sympy import *
from sympy.logic.boolalg import to_dnf
from sympy.logic import SOPform
from sympy.logic import POSform
from sympy.logic import boolalg
from sympy.logic.boolalg import And, Or, Not, Xor, Nand, Nor, Implies, Equivalent, truth_table
import math





def synthesize(boolean_expression, lut_size):
    # Step 1: Parse the boolean expression and extract the variables and the output.
    variables = sorted(set(filter(str.isalpha, boolean_expression)))

    output = boolean_expression.split('=')[0]

    # Step 2: Determine the number of LUTs required based on the number of variables and the size of the LUT.
    num_functions = 2 ** (2 ** len(variables))  # Total number of boolean functions
    num_functions_per_lut = 2 ** (2 ** lut_size)  # Number of functions each LUT can represent
    num_luts = num_functions // num_functions_per_lut  # Number of LUTs required

    # Step 3: Generate the truth table for the boolean expression.
    tt = []
    for val in truth_table(sympify(boolean_expression), variables):
        tt.append(bool(val))

    # Step 4: Group the truth table into groups of size equal to the size of the LUT.
    #group the truth table based on number of input combinations each LUT can handle.
    groups = []
    for i in range(0, len(tt), 2 ** lut_size):
        groups.append(tt[i:i + 2 ** lut_size])


  
    # Step 5: For each group, determine the logic function that maps to the LUT.
    lut_functions = []
    for group in groups:
        # If the group contains all 1s or all 0s, then the logic function is trivial.
        if all(group):
            lut_functions.append(True)
        elif not any(group):
            lut_functions.append(False)
        else:
            # Otherwise, determine the logic function that maps to the LUT.
            minterms = []
            for i, val in enumerate(group):
                if val:
                    minterms.append(i)
            logic_function = SOPform(variables, minterms)
            lut_functions.append(logic_function)

    # Step 6: Create a list that associates each LUT with its assigned logic function.
    lut_assignments = []
    for i in range(num_luts):
        lut_vars = variables[i*num_functions_per_lut:(i+1)*num_functions_per_lut]
        lut_func = lut_functions[i]
        lut_assignments.append((output,lut_vars, lut_func))
        print(lut_assignments)

    #return lut_assignments

if __name__ == '__main__':
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
            case "2":
                lut_size = int(input('Enter the size of the LUT: '))
                for output, details in myoutputs.items():
                    boolean_expression = output + '=' + str(details['Equation'])
                    lut_assignments = synthesize(boolean_expression, lut_size)
                    for i, (lut_vars, lut_func) in enumerate(lut_assignments):
                        print('LUT {}: {} = {}'.format(i, lut_vars, lut_func))
            case "12":
                runprog = 1
    print(myoutputs)