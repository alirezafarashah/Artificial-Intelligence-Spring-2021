import random
import re
import matplotlib.pyplot as plt


def generate_random_sequence():
    sequence = ''
    for i in range(n):
        sequence += nucleotides[random.randint(0, len(nucleotides) - 1)]
    return sequence


def calculate_fitness(sequence):
    fitness = 0
    for i in range(len(constraints)):
        fitness += constraints[i][1] * len(re.findall(constraints[i][0], sequence))
    return fitness


def select(population):
    min_fitness = 0
    for i in range(k):
        if population[i][1] < min_fitness:
            min_fitness = population[i][1]
    weights = [-min_fitness + p[1] + 1 for p in population]
    indexes = [x for x in range(k)]
    new_population = []
    for i in random.choices(indexes, weights=weights, k=k):
        new_population.append(population[i])
    return new_population


def cross_over(population):
    for j in range((k - 1) // 2):
        rand_index = random.randint(0, n - 1)
        first_child = population[2 * j][0][0:rand_index] + population[2 * j + 1][0][rand_index:]
        second_child = population[2 * j + 1][0][0:rand_index] + population[2 * j][0][rand_index:]
        population[2 * j] = (first_child, calculate_fitness(first_child))
        population[2 * j + 1] = (second_child, calculate_fitness(second_child))
    return population


def mutation(population):
    for i in range(len(population)):
        if random.uniform(0, 1) <= 0.5:
            mutation_index = random.randint(0, n - 1)
            random_char = list(set(nucleotides) - {population[i][0][mutation_index]})[random.randint(0, 2)]
            new_seq = population[i][0][0:mutation_index] + random_char + population[i][0][mutation_index + 1:]
            population[i] = (new_seq, calculate_fitness(new_seq))
    return population


def find_max_index(population):
    max_fitness_index = 0
    for i in range(k):
        if population[i][1] > population[max_fitness_index][1]:
            max_fitness_index = i
    return max_fitness_index


def genetic_algorithm():
    population = []
    plot = []
    for i in range(k):
        new_seq = generate_random_sequence()
        new_fit = calculate_fitness(new_seq)
        population.append((new_seq, new_fit))
    for i in range(iteration_limit):
        population = select(population)
        population = cross_over(population)
        population = mutation(population)
        plot.append(population[find_max_index(population)][1])
    plt.plot(plot)
    plt.show()
    max_fitness = population[find_max_index(population)][1]
    pop_max = population[find_max_index(population)][0]
    output_file.write(pop_max)
    output_file.close()
    print(max_fitness)


input_file_name = "input6.txt"
output_file_name = "B6.txt"
input_file = open(input_file_name, 'r')
output_file = open(output_file_name, 'w')
n = int(input_file.readline())
k = int(input_file.readline())
iteration_limit = int(input_file.readline())
nucleotides = input_file.readline().split()
constraints = []
for line in input_file:
    constraints.append([line.split()[0], int(line.split()[1])])
genetic_algorithm()
