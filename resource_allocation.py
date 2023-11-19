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



            case "4":
                
                total_luts = 0
                total_variables = 0
                total_lutsize = 0
                total_connections = 0
                total_memory = 0
                total_input_mem=0
                total_lutsizes=0
                #to count the number of unique variables in each lut
                unique_variables_per_lut = {}
                # Iterate over all outputs
                #put luts withing myout
                for myout in myoutputs:
                    luts = myoutputs[myout]['LUTS']
                    lutsize = myoutputs[myout]['lutsize']
                    variables = myoutputs[myout]['Variables']
                    #print(f"Variables for output {myout}: {variables}")  # Debugging line

                # Iterate over all LUTs
                #count how many unique variables are in each lut
                #for subber in NonsingleVars:
                    #if subber in varmaker:
                        #Variables.append(subber)
                        #varmaker = varmaker.replace(subber, ' ')
                #for char in varmaker:
                    #if char not in ['(',')','+','*','!','&','|', ' ', '~']:
                        #if char not in Variables:
                            #Variables.append(char)
                #Variables = sorted(Variables)
                #variables is l...
#I create a lut that goes into the equation: we should add that to some list, and then in the same way
# we check for the variables, we should check if that lut is in the string, and if it is, we should not add it. so it gets rid of all these
#weird like oh if for example lut name is abc_lut4. now abc is a variable, so we should not add it to the list of luts. if abc is present,
# take them out and count them as list of variables or inputs. so create a master list of all luts in the equation
#and then check if the lut name is in the equation, and if it is, dont add it to the list of luts.
                    for lut in luts:
                        if lut not in unique_variables_per_lut:
                            unique_variables_per_lut[lut] = set()

                        for var in variables:
                            if var in luts[lut]:
                                total_input_mem += 2 ** len(variables)
                                print('total_input_mem', total_input_mem)
                                total_lutsizes += 2 ** lutsize
                                


                                
                                total_luts += len(luts)
                                total_variables += len(variables)
                                #total_lutsize += lutsize * len(luts)
                                total_connections += len(luts) 
                                #mem_per_lut= len(luts)*(2 ** lutsize)
                                #total_memory += mem_per_lut
                                luts_required= total_variables/total_lutsizes
                    memory_percentage=(total_input_mem/total_lutsizes)
                
                            
                    #if lutsize == len(variables):
                        #print(f"LUT size matches the number of variables for output {myout} and LUT {lut}")
                    #else:
                        #print(f"LUT size does not match the number of variables for output {myout} and LUT {lut}")

                #mem_per_lut= 2** lutsize #poss combinations
                #function_s= 2** mem_per_lut

                #total_luts += len(luts)
                #total_variables += len(variables)           # 8 inputs can be represe.. with 3 total luts
                #total_lutsize += lutsize * len(luts)  
                #total_connections += len(luts)  
                #do for all the luts individually
                #total_memory += len(luts) * (2 ** lutsize)  # Memory per LUT is 2^lutsize

                # Print the total LUT size, total variables, percentage of connections, and total memory
                print(f"Total LUT size: {total_lutsizes}")
                print(f"Total variables: {total_variables}")
                print(f"Percentage of connections: {total_connections / total_luts * 100 if total_luts != 0 else 0}%")
                print(f"Total memory required: {memory_percentage}")
                print(f"Percentage of LUTs: {luts_required * 100 if total_luts != 0 else 0}%")  # Modified line
                for lut, unique_variables in unique_variables_per_lut.items():
                    print(f"Number of unique variables for LUT {lut}: {len(unique_variables)}")
                
                           


               

            case "5":
                #(Optional) A visual representation of your mapped FPGA (bonus points)
                pass

                #print(myoutputs)
            case "12":
                break
    print(myoutputs)