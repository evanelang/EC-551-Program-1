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






    #trying to do part a

def synthesize(boolean_expression, lut_size):
        # Step 1: Parse the boolean expression and extract the variables and the output.

        boolean_expression = input("Enter a boolean expression: ")
        variables = sorted(set(filter(str.isalpha, boolean_expression)))

        print("Variables:", variables)

        output = boolean_expression.split('=')[0]
        
        # Step 2: Determine the number of LUTs required based on the number of variables and the size of the LUT.
        num_luts = math.ceil(len(variables) / lut_size)
        
        # Step 3: Generate the truth table for the boolean expression.
        tt = truth_table(sympify(boolean_expression), variables)
        
        # Step 4: Group the truth table into groups of size equal to the size of the LUT.
       
        groups = [tt[i:i+lut_size] for i in range(0, len(tt), lut_size)]
        
        # Step 5: For each group, determine the logic function that maps to the LUT.
        lut_functions = []
        for group in groups:
            minterms = [i for i, val in enumerate(group) if val]
            if not minterms:
                lut_functions.append('0')
            elif len(minterms) == len(group):
                lut_functions.append('1')
            else:
                expr = SOPform(variables, minterms)
                lut_functions.append(str(expr))
        
        # Step 6: Create a list that associates each LUT with its assigned logic function.
        lut_assignments = []
        for i in range(num_luts):
            lut_vars = variables[i*lut_size:(i+1)*lut_size]
            lut_func = lut_functions[i]
            lut_assignments.append((lut_vars, lut_func))
            #using formats
        print('LUT {}: {} = {}'.format(i, lut_vars, lut_func))

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
                varlen = len(Variables)
                LUTLIST = []
                #while(varlen > 0):
                #    if (varlen - 6) > 0:
                #     LUTLIST.append(myout + "_LUT6")
                #     varlen -= 6
                #    elif (varlen - 4) > 0:
                #     LUTLIST.append(myout + "_LUT6")
                #     varlen -= 4
                #    if (varlen <= 4):
                #     if varlen > 0:
                #        LUTLIST.append(myout + "_LUT4")
                #        varlen = 0
                bool2 = sympify(a[1])
                #bool3 = SOPform(bool2)
                mytruth = truth_table(bool2, Variables, input=False)
                myoutputs[myout]['LUTS'] = {}
                #myoutputs[myout]['Equation'] = bool3
                newtruth = []
                minterms = []
                x = 0
                for t in mytruth:
                    if t == True:
                        minterms.append(x)
                        newtruth.append(1)
                    else:
                        newtruth.append(0)
                    x += 1
                bool3 = SOPform(Variables, minterms)
                myoutputs[myout]['Equation'] = bool3
                myoutputs[myout]['LUT_LOAD'] = newtruth
                myoutputs[myout]['Minterms'] = minterms
                lutsize = int(input("What size should the LUTS be?"))
                myoutputs[myout]['lutsize'] = lutsize
                eqsplit = str(bool3).split(' | ')
                varcount = 0
                lutcount = 0
                luteq = ""
                usedvars = []
                for term in eqsplit:
                    varsintermcount = 0
                    editterm = term
                    for otherouts in NonsingleVars:
                        if otherouts in editterm:
                            if otherouts not in usedvars:
                                varcount += 1
                                varsintermcount += 1
                                usedvars.append(otherouts)
                            editterm = editterm.replace(otherouts, ' ')
                            otherlutcount = myoutputs[otherouts]['lutcount']
                            otherlutsize = myoutputs[otherouts]['lutsize']
                            term = term.replace(otherouts, otherouts + "_LUT" + str(otherlutsize) + "_" + str(otherlutcount))
                    for var in Variables:
                        if var in editterm:
                            if var not in usedvars:
                                usedvars.append(var)
                                varcount += 1
                                varsintermcount += 1
                    
                    if varsintermcount > lutsize:
                        print("Error: LUT size too small")
                        exit()
                    if varcount > lutsize:
                        myoutputs[myout]['LUTS'][myout + "_LUT" + str(lutsize) + "_" + str(lutcount)] = luteq[:-3]
                        luteq = myout + "_LUT" + str(lutsize) + "_" + str(lutcount) + " | "
                        varcount -= (lutsize - 1) 
                        lutcount += 1
                    if varcount < lutsize:
                        luteq += term + " | "
                    if varcount == lutsize:
                        luteq += term + " | "
                        #myoutputs[myout]['LUTS'][myout + "_LUT" + str(lutsize) + "_" + str(lutcount)] = luteq
                        #luteq = myout + "_LUT" + str(lutsize) + "_" + str(lutcount) + " | "
                        #lutcount += 1
                        #varcount = 1
               
                myoutputs[myout]['LUTS'][myout + "_LUT" + str(lutsize) + "_" + str(lutcount)] = luteq[:-3]
                myoutputs[myout]['lutcount'] = lutcount
                        



                #print(myoutputs)
            case "12":
                break
    print(myoutputs)

