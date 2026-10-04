import random
import numpy as np

# Parameters
NUM_TASKS = 1000
NUM_SERVERS = 3
POPULATION_SIZE = 50
GENERATIONS = 100
MUTATION_RATE = 0.1

# Initializing population (random task distributions)
def initialize_population():
    return [np.random.randint(0, NUM_SERVERS, NUM_TASKS) for _ in range(POPULATION_SIZE)]

# Fitness function (minimizing the difference between the most and least loaded servers)
def fitness(individual):
    server_loads = np.bincount(individual, minlength=NUM_SERVERS)
    return -max(server_loads) + min(server_loads)  # Negative for minimization

# Selection: Tournament selection
def select_parents(population):
    tournament = random.sample(population, 5)
    return sorted(tournament, key=fitness, reverse=True)[:2]

# Crossover: Single-point crossover
def crossover(parent1, parent2):
    point = random.randint(1, NUM_TASKS - 1)
    return np.concatenate((parent1[:point], parent2[point:])), np.concatenate((parent2[:point], parent1[point:]))

# Mutation: Randomly reassign some tasks
def mutate(individual):
    if random.random() < MUTATION_RATE:
        index = random.randint(0, NUM_TASKS - 1)
        individual[index] = random.randint(0, NUM_SERVERS - 1)
    return individual

# Main genetic algorithm loop
def genetic_algorithm():
    population = initialize_population()
    for _ in range(GENERATIONS):
        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            parent1, parent2 = select_parents(population)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1), mutate(child2)])
        population = new_population

    # Best solution found
    best_solution = max(population, key=fitness)
    return best_solution

# Running the algorithm
best_allocation = genetic_algorithm()

# Computing task distribution
server_loads = np.bincount(best_allocation, minlength=NUM_SERVERS)
total_tasks = sum(server_loads)

# Printing results
for i, count in enumerate(server_loads):
    print(f"Server {chr(65 + i)}: {count} tasks ({(count / total_tasks) * 100:.2f}%)")
