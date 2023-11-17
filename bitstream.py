import sys
import sympy
from sympy import *
from sympy.logic.boolalg import to_dnf
from sympy.logic import SOPform
from sympy.logic import POSform
from sympy.logic import boolalg
from sympy.logic.boolalg import And, Or, Not, Xor, Nand, Nor, Implies, Equivalent, truth_table
import math
import os
import json
import logging

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
                myoutputs[myout]['Equation'] = str(bool3)
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
                    print(term)
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
                        usedvars = usedvars[-varsintermcount:]
                        varcount = varsintermcount + 1
                        lutcount += 1
                        print("HIT")
                    if varcount < lutsize:
                        luteq += term + " | "
                    if varcount == lutsize:
                        luteq += term + " | "
                        
                        #myoutputs[myout]['LUTS'][myout + "_LUT" + str(lutsize) + "_" + str(lutcount)] = luteq
                        #luteq = myout + "_LUT" + str(lutsize) + "_" + str(lutcount) + " | "
                        #lutcount += 1
                        #varcount = 1
                    print(usedvars)
                    print(varcount)
                myoutputs[myout]['LUTS'][myout + "_LUT" + str(lutsize) + "_" + str(lutcount)] = luteq[:-3]
                myoutputs[myout]['lutcount'] = lutcount
                        
            case "2":
                    with open("bitstream.json", 'w') as outfile:
                        json.dump(myoutputs, outfile)
                        
            case "3":
                with open("bitstream.json", 'r') as outfile:
                    myoutputs = json.load(outfile)
                print(myoutputs)
                print(type(myoutputs))
            
                    
           





                #print(myoutputs)
            case "12":
                break
    print(myoutputs)