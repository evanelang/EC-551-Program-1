import sys
import sympy
from sympy import *
from sympy.logic.boolalg import to_dnf
from sympy.logic import SOPform
from sympy.logic import POSform



# takes boolean equation as input and returns a truth table for that equation, a list of variables, and the minterms
#WILL ALWAYS RUN
def evaluate_boolean_equation(boolean_equation):
    # Implementing a stack to evaluate the boolean equation
    Variables = []
    for char in boolean_equation:
        if char not in ['(',')','+','*','!']:
            if char not in Variables:
                Variables.append(char)
    Variables = sorted(Variables)
    terms = []
    row =  (2**(len(Variables)//2))
    #print("row: ", row)
    
    columns = (2**((len(Variables)//2) + (len(Variables)%2)))
    #print("columns: ", columns)
    #Load Kmaps with zeros
    kmap = [[0 for x in range(columns)] for y in range(row)]
    for i in range(row):
        for j in range(columns):
            kmap[i][j] = 0
        

    terms = boolean_equation.split('+')
    Minterms = []
    for term in terms:
        yes = []
        no = []
        Minterm = 0
        for char in term:
            if char not in ['(',')','+','*','!', ' ']:
                termval = 2**(len(Variables) - Variables.index(char)-1)
                if term[(term.index(char)-1)] != '!':    
                    yes.append(termval)
                    Minterm += termval
                elif term[(term.index(char)-1)] == '!':
                    no.append(termval)
        cyclecount = 0
        listlengths = len(yes)+len(no)
        
        
        yessave = yes[:]
        nosave = no[:]
        for leftspot in range(row):
            
            for rightspot in range(columns):
                yes = yessave[:]
                no = nosave[:]
                yestracker = 1
                notracker = 0
                spotval = (leftspot*columns) + rightspot
                for curval in range(listlengths):
                    
                    #Picking the highest term out of both lists to check first
                    #YES list
                    if max(yes, default=0) >= max(no, default=0):
                        onegreater = 2*max(yes, default=0)
                        goodnum = yes.pop(0)
                        #Cleans out the effects of other variables on potential result
                        while(spotval >= onegreater):
                            
                            for x in range(len(Variables)):
                                
                                if spotval >= 2**(len(Variables)-x-1):
                                    if(spotval >= onegreater):
                                        spotval = spotval - 2**(len(Variables)-x-1)
                            
                                    
                        
                        
                        if goodnum in no:
                            notracker = 1
                            
                        if spotval-goodnum >= 0:
                            spotval = spotval-goodnum
                        else:
                            
                            yestracker = 0
                        curval += 1
                    #NOT LIST
                    elif max(yes, default=0) < max(no, default=0):
                        onegreater = 2*max(no, default=0)
                        goodnum = no.pop(0)
                        while(spotval >= onegreater):
                            for x in range(len(Variables)):
                                if spotval >= 2**(len(Variables)-x-1):
                                    if(spotval >= onegreater):
                                        spotval = spotval - 2**(len(Variables)-x-1)
                        
                        if goodnum in yes:
                            
                            notracker = 1
                        if spotval-goodnum >= 0:
                            
                            spotval = spotval-goodnum
                            notracker = 1
                        curval += 1
                    

                if yestracker == 1 and notracker == 0:
                    if(Variables[-1] in term):
                        
                        finnum = (leftspot*columns) + rightspot
                        if finnum % 2 != 0:
                            #print("term: ", term)
                            #print("Hit: ", (leftspot*columns) + rightspot)
                            if finnum not in Minterms:
                                Minterms.append(finnum)
                            kmap[leftspot][rightspot] = 1
                    else:
                        finnum = (leftspot*columns) + rightspot
                        #print("term: ", term)
                        #print("Hit: ", (leftspot*columns) + rightspot)
                        if finnum not in Minterms:
                            Minterms.append(finnum)
                        kmap[leftspot][rightspot] = 1
                    
            cyclecount += 1
        #Minterms.append(Minterm)
    print("Truth Table: ")
    for h in range(row):
        print(kmap[h])
    return kmap, Minterms, Variables

#takes the minterms and variables of a boolean equation and returns the SOP in canonical form
#USED
def SOP(Variables, Minterms):
    newterms = []
    for mymin in Minterms:
        curterm = []
        for myvar in Variables:
            if mymin >= 2**(len(Variables) - Variables.index(myvar)-1):
                curterm.append(myvar)
                mymin = mymin - 2**(len(Variables) - Variables.index(myvar)-1)
            else:
                curterm.append('!' + myvar)
        if curterm not in newterms:
            newterms.append(curterm)
    return newterms



#NOT USED#######################################################################################
#report the number of prime Implicants
#the function prime implicant takes two argument: variables and minterms
    #initalizes an empty list to be updates
    #start a loop that interates over each element in the MInterms list, and assign 
    #each element to the variable myin, so myin is the single minterm from the minterm list
    #The curterm list is used to keep track of the 
    # variables for each implicant as the function iterates over the minterms.
    #The implicants list is used to store all the implicants generated from the given minterms, 
    # which are then used to find the prime implicants.

    #run sop
    # into [AB, CD] into ['A', 'B', 'C', 'D']
def prime_implicants(Variables, Minterms):
   
    implicants = []
    for mymin in Minterms:
        curterm = []
        for myvar in Variables:
            if mymin >= 2**(len(Variables) - Variables.index(myvar)-1):
                curterm.append(myvar)
                mymin = mymin - 2**(len(Variables) - Variables.index(myvar)-1)
            else:
                curterm.append('!' + myvar)
            
        implicants.append(curterm)
        #returns a list of minterms covered by each prime implicant.
    prime_implicants = []
    minterms_covered = []
    for implicant in implicants:
        if implicant not in prime_implicants:
            prime_implicants.append(implicant)
            count = 0
            minterms = []
            for mymin in Minterms:
                if all(literal in implicant or ('!' + literal) in implicant for literal in [str(literal) for literal in SOP(Variables, [mymin])]):
                    count += 1
                    minterms.append(mymin)
            minterms_covered.append(minterms)         



    #reduce if one character difference, delete both of them in the list
    # the goal is to reduce the reduce the list if prime implicants were printed out.
    ##([['A', 'B', '!C', '!D'], ['A', 'B', '!C', 'D'] to [A,B,D]
    #creating a nested loop to compare each implicant with every other implicant in the list
       
    for i in range(len(prime_implicants)):
        for j in range(i+1, len(prime_implicants)):
            diff_ch_count = 0
            diff_index = -1
            for v in range(len(prime_implicants[i])):
                if prime_implicants[i][v] != prime_implicants[j][v]:
                    diff_ch_count += 1
                    diff_index = v
            if diff_ch_count == 1:
                r_implicant = prime_implicants[i].copy()
                r_implicant[diff_index] = prime_implicants[i][diff_index][0] if prime_implicants[i][diff_index][0] == '!' else '!' + prime_implicants[i][diff_index]
                if r_implicant not in prime_implicants:
                    prime_implicants.append(r_implicant)
                    minterms_covered.append(list(set(minterms_covered[i] + minterms_covered[j])))
    #convert to list of variables to reduced list
    reduced_list = []
    for implicant in prime_implicants:
        combined_literal = ''
        for literal in implicant:
            if isinstance(literal, list): # check if the literal is a list
                combined_literal += ''.join(literal) # convert the list to a string before concatenating
            else:
                combined_literal += str(literal)
        combined_literal = combined_literal.replace('!!', '!') # replace double '!!' with a single '!'
        if combined_literal[-1]=="!":                           #remove ! at the end of the last string
            combined_literal = combined_literal[:-1]
        if combined_literal not in reduced_list:
            reduced_list.append(combined_literal)

    return reduced_list
############################################################################################

#FINDS THE NEXT ORDER OF PRIME IMPLICANTS - USED
def essential_implicants2(mysop):
    newterms = []
    implist = []
    diff = 0
    nomatch = 0
    match1 = 0
    matchlist = []
    for term in mysop:
        nomatch = 0
        for term2 in mysop:
            newterms = []
            diff = 0
            match1 = 0
            if abs(len(term)-len(term2)) <= 1:
                for char in term:
                    if char in term2:
                        newterms.append(char)
                        match1 += 1
                    else:
                        match abs(len(term)-len(term2)):
                            case 0:
                                testcharlow = '!'+char
                                testcharhigh = char[1:]
                                if testcharlow in term2:
                                    diff += 1
                                elif testcharhigh in term2:
                                    diff += 1
                                else:
                                    diff += 2
                                    #print("testchar: ", char)
                                    #print("term2: ", term2)
                                    #print("term: ", term)
                            case 1:
                                diff += 1
                if match1 == len(term)-1:
                    if abs(len(term)-len(term2)) == 0:
                        if diff == 1:
                            if newterms not in implist:
                                implist.append(newterms)
                                matchlist.append(term)
                                matchlist.append(term2)
                            nomatch = 1
                    elif abs(len(term)-len(term2)) == 1:
                        if diff == 1:
                            if newterms not in implist:
                                implist.append(newterms)
                                matchlist.append(term)
                                matchlist.append(term2)
                            nomatch = 1
        if nomatch == 0:
            if term not in matchlist:
                if term not in implist:
                    #print("nomatchterm: ", term)
                    implist.append(term)
    #print("matchlist: ", implist)
    return implist        
#Counts literals in a boolean equation              
def literal_count(equation):
    Variables = []
    for char in equation:
        if char not in ['(',')','+','*','!',' ', '_', '|', '^', '&', '~', '>', '<', '=', ' ']:
            Variables.append(char)
    return len(Variables)



# NOT USED essential prime implicants ##############################################################################################################
def essential_prime_implicants(Variables, Minterms, Dontcares):
    implicants = []
    for mymin in Minterms:
        curterm = []
        for myvar in Variables:
            if mymin >= 2**(len(Variables) - Variables.index(myvar)-1):
                curterm.append(myvar)
                mymin = mymin - 2**(len(Variables) - Variables.index(myvar)-1)
            else:
                curterm.append('!' + myvar)
        implicants.append(curterm)
    for mymin in Dontcares:
        curterm = []
        for myvar in Variables:
            if mymin >= 2**(len(Variables) - Variables.index(myvar)-1):
                curterm.append(myvar)
                mymin = mymin - 2**(len(Variables) - Variables.index(myvar)-1)
            else:
                curterm.append('!' + myvar)
        implicants.append(curterm)
    prime_implicants = []
    for implicant in implicants:
        if implicant not in prime_implicants:
            prime_implicants.append(implicant)
    essential_prime_implicants = []
    covered_minterms = []
    for implicant in prime_implicants:
        count = 0
        for mymin in Minterms:
            if all(literal in implicant for literal in SOP(Variables, [mymin])):
                count += 1
                if mymin not in covered_minterms:
                    covered_minterms.append(mymin)
        if count == 1:
            essential_prime_implicants.append(implicant)
        
    uncovered_minterms = set(Minterms + Dontcares) - set(covered_minterms)
    essential_prime_implicants += uncovered_minterms

    # Check if there is at least one single 1 that cannot be covered any other way
    single_ones = [mymin for mymin in uncovered_minterms if bin(mymin).count('1') == 1]
    if single_ones:
        essential_prime_implicants.append(single_ones[0])

    # modify the return statement to print the implicants in the same format as prime_implicants
    return [" ".join([var if var[0] != '!' else var[1]+'\''
                     for var in str(term)]) for term in essential_prime_implicants]

####################################################################################################################################################

# report the number off on set minterms
def ON_Set(Variables, Minterms):
    prime_implicants, minterms_covered = prime_implicants(Variables, Minterms)
    ON_Set_minterms = []
    for i in range(len(prime_implicants)):
        for j in range(i+1, len(prime_implicants)):
            common_minterms = set(minterms_covered[i]).intersection(set(minterms_covered[j]))
            for minterm in common_minterms:
                if minterm not in ON_Set_minterms:
                    ON_Set_minterms.append(minterm)
    return len(ON_Set_minterms)
#report the number of on set maxterms
def ON_Set_Max(Variables, Minterms):
    ON_Set_maxterms = []
    for i in range((2**len(Variables))-1):
        if i not in Minterms:
            ON_Set_maxterms.append(i)

    return(ON_Set_maxterms)
#builds a nice looking SOP boolean equation from a list of terms for printing
def build_canon_sop(canonsop):
    finstring = ""
    for term in canonsop:
        termstring = "("
        for literal in term:
            termstring += literal
            termstring += "*"
        finstring += termstring[:-1]
        finstring += ")+"
    finstring = finstring[:-1]
    return(finstring)
#builds a nice looking POS boolean equation from a list of terms for printing
def build_canon_pos(canonsop):
    finstring = ""
    for term in canonsop:
        termstring = "("
        for literal in term:
            termstring += literal
            termstring += "+"
        finstring += termstring[:-1]
        finstring += ")*"
    finstring = finstring[:-1]
    return(finstring)





if __name__ == '__main__':
    
    boolean_equation = input('What is the boolean equation?')
    print(boolean_equation)
    Variables = []
    Minterms = []
    '''
    adding dont care here
    '''
    Dontcares = []
    truthtable, Minterms, Variables = evaluate_boolean_equation(boolean_equation)
    mysop = SOPform(Variables, Minterms, Dontcares)
    #invert minterms
    invmin = []
    biggestnum = (2**(len(Variables))) - 1
    for i in range(biggestnum):
        if i not in Minterms:
            invmin.append(i)
        else:
            invmin.append(0)

    mypos = POSform(Variables, Minterms)

    myexit = 0
    #The following is the menu for the program
    print("Command 1 returns the canonical SOP")
    print("Command 2 returns the canonical POS")
    print("Command 3 returns the canonical inverse SOP")
    print("Command 4 returns the canonical inverse POS")
    print("Command 5 returns the minimized number of literals representation in SOP")
    print("Command 6 returns the minimized number of literals representation in POS")
    print("Command 7 returns the prime implicants")
    print("Command 8 returns the essential prime implicants")
    print("Command 9 returns the number of ON-Set minterms")
    print("Command 10 returns the number of ON-Set Maxterms")
    print("Command 11 returns all variables in entry")
    print("Command 12 exits program")
    #The main loops, waiting for more commands until the user exits
    commandin = input("What do you want to do to the boolean equation?: ")
    while myexit != 1:
        match commandin:
            case "1":
                canonsop = SOP(Variables, Minterms)
                a = build_canon_sop(canonsop)
                print("Canon SOP: ", build_canon_sop(canonsop))

                #print(to_anf(mysop, mypos))
            case "2":
                canonsop = SOP(Variables, invmin)
                print("Canon POS: ", build_canon_pos(canonsop))
            case "3":
                canonsop = SOP(Variables, invmin)
                print("Canon Inverse SOP: ", build_canon_sop(canonsop))
            case "4":
                canonsop = SOP(Variables, Minterms)
                print("Canon Inverse POS: ", build_canon_pos(canonsop))
            case "5":
                simp = simplify_logic(mysop)
                canonsop = SOP(Variables, Minterms)
                neweq = build_canon_sop(canonsop)
                simpcount = literal_count(str(simp))
                cancount = literal_count(neweq)
                numsave = cancount-simpcount
                print(" minimized number of literals representation in SOP: ",simplify_logic(mysop))
                print("number of literals saved: ", numsave)
            case "6":
                simp = simplify_logic(mypos)
                canonpos = SOP(Variables, invmin)
                neweq = build_canon_pos(canonpos)
                simpcount = literal_count(str(simp))
                cancount = literal_count(neweq)
                numsave = cancount-simpcount
                print(" minimized number of literals representation in POS",simplify_logic(mypos))
                print("number of literals saved: ", numsave)
            case "7":
                #Compiles all first second and third order prime implicants
                canonsop = SOP(Variables, Minterms)
                p_implicant_first_order = (essential_implicants2(canonsop))
                p_implicant_second_order = (essential_implicants2(p_implicant_first_order))
                p_implicant_third_order = (essential_implicants2(p_implicant_second_order))
                for term2 in p_implicant_second_order:
                    if term2 not in p_implicant_first_order:
                        p_implicant_first_order.append(term2)
                for term3 in p_implicant_third_order:
                    if term3 not in p_implicant_second_order:
                        p_implicant_second_order.append(term3)
                count_lit= len(p_implicant_first_order)
                print("Prime implicants: ", p_implicant_first_order)
                print("Number of prime implicants: ", count_lit)
                


            case "8":
                #reports only the essential prime implicants
                canonsop = SOP(Variables, Minterms)
                p_implicant_first_order = (essential_implicants2(canonsop))
                p_implicant_second_order = (essential_implicants2(p_implicant_first_order))
                p_implicant_third_order = (essential_implicants2(p_implicant_second_order))
                print("Prime implicants: ", p_implicant_third_order)
                print("Number of essential prime implicants: ",len(p_implicant_third_order))
            case "9":

                print("Number of ON-Set minterms:", len(Minterms))
            case "10":
                print("Number of ON-Set Maxterms:", len(ON_Set_Max(Variables, Minterms)))
            case "11":
                print("All variables in entry: ", Variables)
            case "12":
                print("Exiting program...")
                break
                
        if(commandin != 12):
            commandin = input("What do you want to do to the boolean equation?: ")
    print("Program exited")
