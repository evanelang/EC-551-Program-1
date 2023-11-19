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

def createTruthTable(booleanexpr, Vars):
    bool2 = sympify(booleanexpr)
    #bool3 = SOPform(bool2)
    mytruth = truth_table(bool2, Vars, input=False)
    newtruth = []
    x = 0
    for t in mytruth:
        if t == True:
            newtruth.append(1)
        else:
            newtruth.append(0)
        x += 1
    return newtruth




if __name__ == '__main__':
    #boolean_equation = input('What is the boolean equation?')

    runprog = 0
    NonsingleVars = []
    myoutputs = {}
    master_lut_dict = {}
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
                created_usedvars = []
                conlut = []
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
                            created_usedvars.append(otherouts+ "_LUT" + str(otherlutsize) + "_" + str(otherlutcount))
                            conlut.append(otherouts+ "_LUT" + str(otherlutsize) + "_" + str(otherlutcount))

                    for var in Variables:
                        if var in editterm:
                            if var not in usedvars:
                                created_usedvars.append(var)
                                usedvars.append(var)
                                varcount += 1
                                varsintermcount += 1
                    
                    if varsintermcount > lutsize:
                        print("Error: LUT size too small")
                        exit()
                    if varcount > lutsize:
                        myoutputs[myout]['LUTS'][myout + "_LUT" + str(lutsize) + "_" + str(lutcount)] = luteq[:-3]
                        master_lut_dict[myout + "_LUT" + str(lutsize) + "_" + str(lutcount)] = {}
                        master_lut_dict[myout + "_LUT" + str(lutsize) + "_" + str(lutcount)]["Equation"] = luteq[:-3]
                        master_lut_dict[myout + "_LUT" + str(lutsize) + "_" + str(lutcount)]["Connected_LUTS"] = conlut
                        master_lut_dict[myout + "_LUT" + str(lutsize) + "_" + str(lutcount)]["Variables"] = []
                        master_lut_dict[myout + "_LUT" + str(lutsize) + "_" + str(lutcount)]["LUT_Size"] = lutsize
                        temper = created_usedvars[:-varsintermcount]
                        for prevlut in temper:
                            master_lut_dict[myout + "_LUT" + str(lutsize) + "_" + str(lutcount)]["Variables"].append(prevlut)
                        luttruth = createTruthTable(luteq[:-3], master_lut_dict[myout + "_LUT" + str(lutsize) + "_" + str(lutcount)]["Variables"])
                        master_lut_dict[myout + "_LUT" + str(lutsize) + "_" + str(lutcount)]["LUT_LOAD"] = luttruth
                        created_usedvars = created_usedvars[-varsintermcount:]
                        created_usedvars.append(myout + "_LUT" + str(lutsize) + "_" + str(lutcount))
                        conlut = []
                        conlut.append(myout + "_LUT" + str(lutsize) + "_" + str(lutcount))
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
                    master_lut_dict[myout + "_LUT" + str(lutsize) + "_" + str(lutcount)] = {}
                    master_lut_dict[myout + "_LUT" + str(lutsize) + "_" + str(lutcount)]["Equation"] = luteq[:-3]
                    master_lut_dict[myout + "_LUT" + str(lutsize) + "_" + str(lutcount)]["Connected_LUTS"] = conlut
                    master_lut_dict[myout + "_LUT" + str(lutsize) + "_" + str(lutcount)]["Variables"] = []
                    master_lut_dict[myout + "_LUT" + str(lutsize) + "_" + str(lutcount)]["LUT_Size"] = lutsize
                    temper = created_usedvars
                    for prevlut in temper:
                        master_lut_dict[myout + "_LUT" + str(lutsize) + "_" + str(lutcount)]["Variables"].append(prevlut)
                    luttruth = createTruthTable(luteq[:-3], master_lut_dict[myout + "_LUT" + str(lutsize) + "_" + str(lutcount)]["Variables"])
                    master_lut_dict[myout + "_LUT" + str(lutsize) + "_" + str(lutcount)]["LUT_LOAD"] = luttruth
                    myoutputs[myout]['lutcount'] = lutcount
                        
            case "2":
                    with open("bitstream.json", 'w') as outfile:
                        json.dump(myoutputs, outfile)
                    with open("masterlut.json", 'w') as outfile:
                        json.dump(master_lut_dict, outfile)
                        
            case "3":
                with open("bitstream.json", 'r') as outfile:
                    myoutputs = json.load(outfile)
                with open("masterlut.json", 'r') as outfile:
                    master_lut_dict = json.load(outfile)
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
                for myout in master_lut_dict:
                    luts = myoutputs[myout]['LUTS']
                    print(luts)
                    lutsize = myoutputs[myout]['lutsize']
                    variables = myoutputs[myout]['Variables']
                    lutcount = myoutputs[myout]['lutcount']
                    conlut = myoutputs[myout]['Connected_LUTS']
                    luttruth = myoutputs[myout]['Minterms']

                    #to count the number of unique variables in each lut
                    unique_variables_per_lut[myout] = []
                    # Iterate over all LUTs
                    for lut in luts:
                        total_luts += len(luts)
                        total_lutsize += lutsize
                        total_lutsizes += lutsize
                        total_input_mem += 2 ** len(variables)
                        total_connections += len(conlut)
                        total_input_mem += len(luttruth)
                        #to count the number of unique variables in each lut
                        for var in variables:
                            if var not in unique_variables_per_lut[myout]:
                                unique_variables_per_lut[myout].append(var)
                    total_memory=total_input_mem/lutsize
                print("Total LUTs: ", total_luts)
               #print the number of total variables
                for myout in unique_variables_per_lut:
                    total_variables += len(unique_variables_per_lut[myout])
                print("Total Variables: ", total_variables)
                #print the total lut size
                print("Total LUT Size: ", total_lutsize)
                #print the total connections
                print("Total Connections: ", total_connections)
                #print the total memory
                print("Total Memory: ", total_memory)
                #print the total input memory
                print("Total Input Memory: ", total_input_mem)
                #print the total lut sizes
                print("Total LUT Sizes: ", total_lutsizes)
                #print the number of unique variables in each lut
                print("Unique Variables Per LUT: ", unique_variables_per_lut)

            case "5":
                #(Optional) A visual representation of your mapped FPGA (bonus points)
                pass
            case "6":
                print("LUT Conn Viewer: ALL LUTS IN THE FPGA")
                print(master_lut_dict.keys())
                print("Input the LUT you want to view or input 'all' to view all LUTs")
                lut_name = input("Enter the LUT name: ")
                if lut_name == "all":
                    print(master_lut_dict)
                else:
                    print(master_lut_dict[lut_name])
            case "12":
                break
    #print(myoutputs)
    print(master_lut_dict)