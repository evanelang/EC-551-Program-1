import sys

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
            if char not in ['(',')','+','*','!']:
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
                    
                    if max(yes, default=0) >= max(no, default=0):
                        onegreater = 2*max(yes, default=0)
                        goodnum = yes.pop(0)
                        
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
                    elif max(yes, default=0) < max(no, default=0):
                        onegreater = 2*max(no, default=0)
                        goodnum = no.pop(0)
                        while(spotval >= onegreater):
                            for x in range(len(Variables)):
                                if spotval >= 2**(len(Variables)-x-1):
                                    spotval = spotval - 2**(len(Variables)-x-1)
                        
                        if goodnum in yes:
                            
                            notracker = 1
                        if spotval-goodnum >= 0:
                            
                            spotval = spotval-goodnum
                            notracker = 1
                        curval += 1
                    

                if yestracker == 1 and notracker == 0:
                    print("term: ", term)
                    print("Hit: ", (leftspot*columns) + rightspot)
      
                    kmap[leftspot][rightspot] = 1
            cyclecount += 1
        Minterms.append(Minterm)
    print(Minterms)
    for h in range(row):
        print(kmap[h])
    return Minterms


                    




if __name__ == '__main__':
    
    boolean_equation = input('What is the boolean equation?')
    print(boolean_equation)
    evaluate_boolean_equation(boolean_equation)
    #ask for commands for what to do to boolean equation
    #print(boolean_equation)
