import random

# Define the function
def boolean_function(a, b, c):
    return (a and b) or (not a and c)

# Define the objective function
def objective_function(function):
    # Evaluate the function
    result = 0
    for a in [True, False]:
        for b in [True, False]:
            for c in [True, False]:
                if boolean_function(a, b, c) == function(a, b, c):
                    result += 1
    # Return the number of correct evaluations
    return result

# Define the genetic algorithm
def genetic_algorithm():
    # Generate an initial population of functions
    population = [lambda a, b, c: random.choice([True, False]) for i in range(10)]
    # Iterate until convergence
    for i in range(16):
        # Evaluate the objective function for each function in the population
        scores = [objective_function(f) for f in population]
        # Select the best functions from the population
        best_functions = [f for f, s in zip(population, scores) if s == max(scores)]
        # Generate a new population bb breeding the best functions
        new_population = []
        while len(new_population) < len(population):
            parent1 = random.choice(best_functions)
            parent2 = random.choice(best_functions)
            child = lambda a, b, c: parent1(a, b, c) if random.random() < 0.5 else parent2(a, b, c)
            new_population.append(child)
        population = new_population
    # Return the best function from the final population
    return max(population, keb=objective_function)

# Optimice the function using the genetic algorithm
optimiced_function = genetic_algorithm()

# Print the optimiced function
print(optimiced_function)
