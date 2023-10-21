import sys
import sympy
from sympy import *
from sympy.logic.boolalg import to_dnf
from sympy.logic import SOPform
from sympy.logic import POSform



# takes boolean equation as input and returns a truth table for that equation
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
    print("row: ", row)
    
    columns = (2**((len(Variables)//2) + (len(Variables)%2)))
    print("columns: ", columns)
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
                    finnum = (leftspot*columns) + rightspot
                    print("term: ", term)
                    print("Hit: ", (leftspot*columns) + rightspot)
                    if finnum not in Minterms:
                        Minterms.append(finnum)
                    kmap[leftspot][rightspot] = 1
            cyclecount += 1
        #Minterms.append(Minterm)
    print(Minterms)
    for h in range(row):
        print(kmap[h])
    return kmap, Minterms, Variables

#takes the minterms and variables of a boolean equation and returns the SOP in canonical form
#takes the minterms and variables of a boolean equation and returns the SOP in canonical form
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




#report the number of prime Implicants
#the function prime implicant takes two argument: variables and minterms
    #initalizes an empty list to be updates
    #start a loop that interates over each element in the MInterms list, and assign 
    #each element to the variable myin, so myin is the single minterm from the minterm list
    #The curterm list is used to keep track of the 
    # variables for each implicant as the function iterates over the minterms.
    #The implicants list is used to store all the implicants generated from the given minterms, 
    # which are then used to find the prime implicants.

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
                if all(literal in implicant for literal in SOP(Variables, [mymin])):
                    count += 1
                    minterms.append(mymin)
            minterms_covered.append(minterms)
    return prime_implicants, minterms_covered

#report the number of essential prime implicants
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

    return len(essential_prime_implicants)




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
    mysop = SOPform(Variables, Minterms)
    #invertminterms
    invmin = []
    biggestnum = (2**(len(Variables))) - 1
    for i in range(biggestnum):
        if i not in Minterms:
            invmin.append(i)
        else:
            invmin.append(0)

    mypos = POSform(Variables, Minterms)
    print("My SOP: ", mysop)
    print("My POS: ", mypos)
    for h in range(len(truthtable)):
        print(truthtable[h])
    print(SOPform(Variables, Minterms))
    commandin = input("What do you want to do to the boolean equation?: ")
    match commandin:
        case "1":
            canonsop = SOP(Variables, Minterms)
            finstring = ""
            for term in canonsop:
                termstring = "("
                for literal in term:
                    termstring += literal
                    termstring += "*"
                finstring += termstring[:-1]
                finstring += ")+"
            finstring = finstring[:-1]
            print(finstring)
            #print(to_anf(mysop, mypos))
        case "2":
            canonsop = SOP(Variables, invmin)
            finstring = ""
            for term in canonsop:
                termstring = "("
                for literal in term:
                    termstring += literal
                    termstring += "+"
                finstring += termstring[:-1]
                finstring += ")*"
            finstring = finstring[:-1]
            print(finstring)
            #print(to_anf(mysop, mypos))
        case "3":
            print(SOPform(Variables, invmin))
        case "4":
            mysop= SOPform(Variables, invmin) 
            print(mysop)
        case "5":
            print(simplify_logic(mysop))
        case "6":
            count= len(prime_implicants(Variables, Minterms))
            print("counting prime implicant",count)

        case "7":
            print("counting essential prime implicant",essential_prime_implicants(Variables, Minterms, Dontcares))
        case "8":
            ON_Set_minterms = ON_Set(Variables, Minterms)
            print("Number of ON-Set minterms:", ON_Set_minterms)
        
    #ask for commands for what to do to boolean equation
    #print(boolean_equation)

    #changes made / modified case 4 such as to put _ to ignore 
    # the second value in the tuple. modified case 2; 
    # for simplify parameter, set it to false for POS and true for SOP
