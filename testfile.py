








































































































































































































































#test cases 
def test_case(test_cases):
    match (test_cases):
        case 1:
            return "case 1"
        case 2:
            return "case 2"
        case 3:
            return "case 3"
        case 4:
            return "case 4"
        case 5:
            return "case 5"
        case 6:
            return "case 6"
        case 7:
            return "case 7"
        case 8:
            return "case 8"
        case _:
            return "other cases"
        
#test the function
print(test_case(1))  #will return "case1"
print(test_case(2))
print(test_case(3))
print(test_case(4))
print(test_case(5))
print(test_case(6))
print(test_case(7))
print(test_case(8))
print(test_case(9))     #will return other cases




































def test_cases(a, b,c):
    #create a dictionary with possible input combinations and their corresponding cases
    case={
        (0,0,0): "case 1",
        (0,0,1): "case 2",
        (0,1,0): "case 3",
        (0,1,1): "case 4",
        (1,0,0): "case 5",
        (1,0,1): "case 6",
        (1,1,0): "case 7",
        (1,1,1): "case 8"}
    
    #assign a a variable/tuple from inputs to represent the possible inputs combination.
    tuples=  (a, b,c) 
    if tuples in case:
        return case[tuples]
    else:
        raise ValueError("Invalid combinations")

# Now test the functions
print(test_cases(0,0,0)) # must pring case














