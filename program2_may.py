import sys
import sympy
from sympy import *
from sympy.logic.boolalg import to_dnf
from sympy.logic import SOPform
from sympy.logic import POSform
from sympy.logic import boolalg
from sympy.logic.boolalg import And, Or, Not, Xor, Nand, Nor, Implies, Equivalent, truth_table
import math



def processEq(booleanexpr, Vars):
    if(len(Vars) == 4):
        print("HI")
    return 0

def synthesize(boolean_expression, lut_size):
    # Step 1: Parse the boolean expression and extract the variables.
    variables = myoutputs[myout]['Variables']
    print("variables",variables)

    # Step 2: Determine the number of LUTs required based on the number of variables and the size of the LUT.
    num_functions = 2 ** (2 ** len(variables))  # Total number of boolean functions
    num_luts = int(num_functions / lut_size)  # Number of LUTs required
    print(num_luts)

    # Step 3: Generate the truth table for the boolean expression.
    tt = []
    for val in truth_table(sympify(boolean_expression), variables):
        tt.append(bool(val))

    # Step 4: Group the truth table into groups of size equal to the size of the LUT.
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
        if i < len(lut_functions):
            lut_vars = variables[:lut_size]  # Assign the first 'lut_size' variables to the LUT
            lut_func = lut_functions[i]
            lut_assignments.append((f'LUT{i}', lut_vars, lut_func))

    print(lut_assignments)

    return lut_assignments

#trying to do part d bitstream for the program
#just a template for the bitstream function
#def bitstream(lut_assignments, bitstream_file_path):
    # Initialize an empty list
    #bitstream = []
    # For each lut in lut_assignments
    #for lut in lut_assignments:
        # If the lut function is true
        #if lut[2] == True:
            # Append 1 to the bitstream
            #bitstream.append('1')
        # If the lut function is false
        #elif lut[2] == False:
            # Append 0 to the bitstream
           # bitstream.append('0')
        # If the lut function is not true or false
        #else:
            # Append 1 to the bitstream
            #bitstream.append('1')
    # Write the bitstream to a file
    #with open(bitstream_file_path, 'w') as f:
        #f.write(''.join(bitstream))

# Example usage
#lut_assignments = [...] # List of LUT assignments
#bitstream_file_path = "example.bit"
#bitstream(lut_assignments, bitstream_file_path)


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
                for details in myoutputs.keys():
                    boolean_expression =myoutputs[details]['Equation']
                    lut_assignments = synthesize(boolean_expression, lut_size)
                #print('LUT Assignments:', lut_assignments)
                    for i, (lut_name, lut_vars, lut_func) in enumerate(lut_assignments):
                        print('LUT  {} : {} = {}'.format(lut_name, lut_vars, lut_func))
                    lut_dict = {}
                    for i, lut in enumerate(lut_assignments):
                        lut_name, lut_vars, _ = lut
                        for var in lut_vars:
                            lut_dict[f'{lut_name}_{var}'] = var

                    print(lut_dict)

                    
            case "12":
                runprog = 1
    print(myoutputs)