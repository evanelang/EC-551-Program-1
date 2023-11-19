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
    print("Welcome to the FPGA Resource Allocation Program")
    print("Please set your limits for the FPGA")
    maxluts = int(input("What is the maximum number of LUTs?"))
    maxinputs = int(input("What is the maximum number of inputs?"))
    maxoutputs = int(input("What is the maximum number of outputs?"))
    runprog = 0
    NonsingleVars = []
    myoutputs = {}
    master_lut_dict = {}
    myoutputs["totalinputs"] = []
    myoutputs["totaloutputs"] = 0
    myoutputs["totalinputsmax"] = maxinputs
    myoutputs["totaloutputsmax"] = maxoutputs
    myoutputs["totalLUTS"] = maxluts
    while(runprog != 1):
        if(myoutputs["totaloutputs"] > myoutputs["totaloutputsmax"]):
            print("Error: Not enough outputs allocated")
            break
        if(len(myoutputs["totalinputs"]) > myoutputs["totalinputsmax"]):
            print("Error: Not enough inputs allocated")
            break
        if(len(master_lut_dict) > myoutputs["totalLUTS"]):
            print("Error: Not enough LUTs allocated")
            break
        print("Please select an option")
        print("1. Enter a boolean equation")
        print("2. Save the bitstream")
        print("3. Load the bitstream")
        print("4. Calculate FPGA resource usage")
        print("5. Visual representation of FPGA")
        print("6. View LUT connections and LUT details")
        print("7. View bitstream/current FPGA state")
        print("12. Exit")
        commandin = input('What would you like to do?')
        match commandin:
            case "1":
                runprog = 0
                Variables = []
                boolean_equation = input('What is the boolean equation?') 
                a = boolean_equation.split('=')
                myoutputs["totaloutputs"] += 1
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
                            myoutputs["totalinputs"].append(char)
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
                        master_lut_dict[myout + "_LUT" + str(lutsize) + "_" + str(lutcount)]["Connected_LUTS"] = []
                        master_lut_dict[myout + "_LUT" + str(lutsize) + "_" + str(lutcount)]["Variables"] = []
                        master_lut_dict[myout + "_LUT" + str(lutsize) + "_" + str(lutcount)]["LUT_Size"] = lutsize
                        temper = created_usedvars[:-varsintermcount]
                        for prevlut in temper:
                            master_lut_dict[myout + "_LUT" + str(lutsize) + "_" + str(lutcount)]["Variables"].append(prevlut)
                        luttruth = createTruthTable(luteq[:-3], master_lut_dict[myout + "_LUT" + str(lutsize) + "_" + str(lutcount)]["Variables"])
                        master_lut_dict[myout + "_LUT" + str(lutsize) + "_" + str(lutcount)]["LUT_LOAD"] = luttruth
                        created_usedvars = created_usedvars[-varsintermcount:]
                        created_usedvars.append(myout + "_LUT" + str(lutsize) + "_" + str(lutcount))
                        for conner in conlut:
                            if conner in master_lut_dict[myout + "_LUT" + str(lutsize) + "_" + str(lutcount)]["Variables"]:
                                master_lut_dict[myout + "_LUT" + str(lutsize) + "_" + str(lutcount)]["Connected_LUTS"].append(conner)
                                conlut.remove(conner)
                        
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
                total_connections = 0

                for myout in master_lut_dict.keys():
                    #luts=master_lut_dict[myout]['LUTS']
                    
                    
                    #luts = master_lut_dict[myout]['LU']
                    lutsize = master_lut_dict[myout]["LUT_Size"]
                    print("lutsize",lutsize)
                    variables = master_lut_dict[myout]["Variables"]
                    print("variables",variables)
                    total_luts_count= len(master_lut_dict.keys())
                    print("total_luts_count",total_luts_count)
                    connections_for_luts = len(master_lut_dict[myout]["Connected_LUTS"])
                    print("connections_for_luts",connections_for_luts) # !!!debugging error starting here

                # Iterate over all LUTs
                    #for lut in master_lut_dict.keys():
                    #for var in variables:
                            #if var in master_lut_dict[lut]:
                    total_input_mem += 2 ** len(variables)
                    total_lutsizes += 2 ** lutsize
                    total_variables += len(variables)         
                    total_connections += connections_for_luts
                    print("total",total_connections)
                luts_required= total_variables/total_lutsizes
                memory_percentage=(2**total_input_mem)*total_luts_count
                #pecentage of fpga luts that are not connected...
                    
                    #if lutsize == len(variables):
                        #print(f"LUT size matches the number of variables for output {myout} and LUT {lut}")
                    #else:
                        #print(f"LUT size does not match the number of variables for output {myout} and LUT {lut}")
                # Print the total LUT size, total variables, percentage of connections, and total memory
                print(f"Total LUT size: {total_lutsizes}")
                print(f"Total variables: {total_variables}")
                print(f"Percentage of connections: {(total_connections /maxluts)}%")
                #print(f"Percentage of connections: {(total_connections /maxluts) * 100 if total_luts != 0 else 0}%")
                print(f"Total memory required: {memory_percentage}")
                print(f"Percentage of LUTs: {luts_required * 100 }%")  # Modified line
                


               

            case "5":
                #(Optional) A visual representation of your mapped FPGA (bonus points)
                
                pass
            case "6":
                print("LUT Conn Viewer: ALL LUTS IN THE FPGA")
                print(master_lut_dict.keys())
                print("Input the LUT you want to view or input 'all' to view all LUTs")
                lut_name = input("Enter the LUT name: ")
                if lut_name == "all":
                    print(json.dumps(master_lut_dict, indent=4))
                else:
                    print(lut_name + ": ")
                    print(json.dumps(master_lut_dict[lut_name], indent=4))
            case "7":
                print(json.dumps(myoutputs, indent=4))
            case "12":
                break
    #print(myoutputs)
    print(master_lut_dict)