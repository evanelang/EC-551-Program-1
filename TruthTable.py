import sys

def evaluate_boolean_equation(boolean_equation):
    # Implementing a stack to evaluate the boolean equation
    Variables = []
    for char in boolean_equation:
        if char not in ['(',')','+','*']:
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
        
    left = Variables[:(len(Variables)//2)]
    top = Variables[(len(Variables)//2):]
    terms = boolean_equation.split('+')
    Minterms = []
    for term in terms:
        leftspot = 0
        righspot = 0
        Minterm = 0
        for char in term:
            if char not in ['(',')','+','*']:
                if char in left:
                    leftspot += 2**(len(left) - left.index(char)-1)
                    Minterm += 2**(len(Variables) - Variables.index(char)-1)
                elif char in top:
                    righspot += 2**(len(top) - top.index(char)-1)
                    Minterm += 2**(len(Variables) - Variables.index(char)-1)
        print("Left: ", leftspot, "Right: ", righspot)
        kmap[leftspot][righspot] = 1
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
