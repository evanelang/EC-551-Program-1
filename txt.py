
#report the number of prime Implicants
def count_prime_implicants(Variables, minterms):
    # Convert the boolean equation to its canonical sum-of-products form.
    #using the function SOP above, i could of have used the one in sympy
    mysop = SOP(Variables, minterms)
    
    # Generate all possible prime implicants
    num_variables = len(Variables)
    prime_implicants = []
    for i in range(2**num_variables):
        binary = bin(i)[2:].zfill(num_variables)
        minterm = [int(x) for x in binary]
        if evaluate_boolean_equation(boolean_equation,minterm):
            prime_implicants.append(minterm)
    
    # Remove redundant prime implicants
    essential_prime_implicants = []
    remaining_minterms = minterms.copy()
    while remaining_minterms:
        covered_minterms = set()
        for implicant in prime_implicants:
            if set(implicant).issubset(remaining_minterms):
                essential_prime_implicants.append(implicant)
                covered_minterms.update(implicant)
        remaining_minterms = remaining_minterms - covered_minterms
        prime_implicants = [implicant for implicant in prime_implicants if set(implicant).isdisjoint(covered_minterms)]
    
    # Count the number of prime implicants
    num_prime_implicants = len(essential_prime_implicants)
    
    # Return the result
    return mysop, num_prime_implicants


#report the number of essential prime implicants
def report_num_essential_prime_implicants(boolean_equation):
    # Get the variables and the inverse minterms of the boolean equation
    Variables, invmin = evaluate_boolean_equation(boolean_equation)

    # Generate all possible prime implicants
    num_variables = len(Variables)
    prime_implicants = []
    for i in range(2**num_variables):
        binary = bin(i)[2:].zfill(num_variables)
        implicant = [int(x) for x in binary]
        if evaluate_boolean_equation(boolean_equation, implicant):
            prime_implicants.append(implicant)

    # Remove redundant prime implicants
    essential_prime_implicants = []
    remaining_minterms = invmin.copy()
    while remaining_minterms:
        covered_minterms = set()
        for implicant in prime_implicants:
            if set(implicant).issubset(remaining_minterms):
                essential_prime_implicants.append(implicant)
                covered_minterms.update(implicant)
        remaining_minterms = remaining_minterms - covered_minterms
        prime_implicants = [implicant for implicant in prime_implicants if set(implicant).isdisjoint(covered_minterms)]

    # Count the number of essential prime implicants
    num_essential_prime_implicants = len(essential_prime_implicants)

    # Return the result
    return num_essential_prime_implicants

