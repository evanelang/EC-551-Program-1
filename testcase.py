


# test case
# match case
# match case is a new feature in python 3.10
# match case is a new way to write switch case in python
# match case is more powerful than switch case
# match case is more readable than switch case
# match case is more flexible than switch case
# match case is more efficient than switch case
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
