import sys
import sympy
from sympy import *
from sympy.logic import SOPform
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
        for leftspot in range(columns):
            
            for rightspot in range(row):
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


                    




if __name__ == '__main__':
    
    boolean_equation = input('What is the boolean equation?')
    print(boolean_equation)
    Variables = []
    Minterms = []
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
    for h in range(len(truthtable[0])):
        print(truthtable[h])
    print(SOPform(Variables, Minterms))
    commandin = input("What do you want to do to the boolean equation?: ")
    match commandin:
        case "1":
            print(mysop)
        case "2":
            print(mypos)
        case "3":
            print(SOPform(Variables, invmin))
        case "4":
            print(POSform(Variables, invmin))
        case "5":
    #ask for commands for what to do to boolean equation
    #print(boolean_equation)


    



   
        




