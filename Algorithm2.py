import sys, os
import random
from numpy.lib.shape_base import _expand_dims_dispatcher
import pickle   
import numpy as np

sys.path.insert(0, 'evoman') 
from evoman.environment import Environment
from player_controllers import player_controller
from types import MethodType

#Disabling visuals for faster runs
headless = True
if headless:
    os.environ["SDL_VIDEODRIVER"] = "dummy"
            
#Setting parameters     
pop_size = 100
gen = 15
n_hidden = 10
n_runs = 10
enemy = [3,4,7]
crossover = 0.2

#Creating file for saving experiment in folder
exp_name = f"CrossoverII_ES2_hidden10_gen{gen}_enemy{enemy}"
if not os.path.exists(exp_name):
    os.makedirs(exp_name)

def New_fit(self):
    return 0.9*(100 - self.get_enemylife()) + 0.1*self.get_playerlife() +1 #+1 so fitness can't be 0

env = Environment(experiment_name=exp_name,
                  playermode="ai",
                  player_controller=player_controller(n_hidden),
                  enemies=[3,4,7],
                  randomini="yes",
                  multiplemode="yes",
                  enemymode="static")

env.fitness_single = MethodType(New_fit, env)

#Generating population for every generation
def offspring_calc(solutions, old):
    population, fitness = solutions
    new_population = np.zeros((len(pop),len(pop[0])))
    
    old_parents = int(len(population) * old)
    new_children = len(population) - old_parents
    
    #Adding parents with highest fitness (20% of new population)
    top_index = sorted(range(len(fitness)), key=lambda i: fitness[i])[-old_parents:]
    for p, i in enumerate(top_index):
         new_population[p] = population[i]
    
    #Calculating weights according to relative fitness
    if (min(fitness) < 0):
        positive = [x + min(fitness) for x in fitness]
        pop_weights = [x/sum(positive) for x in positive]
    else:
        pop_weights = [x/sum(fitness) for x in fitness]
        
    #Making new population with uniform crossover
    for count in range(0, new_children):
        count += old_parents
        
        #Choosing random parents with weights calculated above
        parents = random.choices(population, weights=pop_weights, k=2)
        
        #Picking random gene of parents
        parent_length = len(parents[0])
        child = np.zeros(parent_length)
        for j in range(parent_length):
            gene = random.choice([parents[0][j], parents[1][j]])
            child[j] = gene
        new_population[count] = child

    return new_population

#Calculating fitness for every generation
def fitness_calc(population, i):
    population_fitness = []
    for individual in population:
        fitness = env.play(pcont=individual)[0]
        population_fitness.append(fitness)
    
    #Adding mean and max fitness to lists and saving in numpy files
    fitness_generation.append(np.mean(population_fitness))
    np.save(f"{exp_name}/fitness_gens_{i}", fitness_generation)
    fitness_max.append(np.max(population_fitness))
    np.save(f"{exp_name}/fitness_max_{i}", fitness_max)
     
    return population_fitness

fitness_max = []
fitness_generation = []

#Number of weights for multilayering with hidden neurons
n_vars = (env.get_num_sensors()+1)*n_hidden + (n_hidden+1)*5

for r in range(n_runs):

    #Creating initial population and adding to environment
    pop = np.random.uniform(-1, 1, (pop_size, n_vars))
    population_fitness = fitness_calc(pop, r)
    
    best_fitness_generation = [np.max(population_fitness)]
    best = pop[np.argmax(population_fitness)]
    mean_fitness_generation = [np.mean(population_fitness)]
    standard_fitness_generation = [np.std(population_fitness)]
    
    print("\n------------------------------------------------------------------")
    print(f"Generation 0. Mean {mean_fitness_generation[-1]}, best {best_fitness_generation[-1]}")
    print("------------------------------------------------------------------")
    
    solutions = [pop, population_fitness]
    env.update_solutions(solutions)
    
    for i in range(gen):
        pop = offspring_calc(solutions, crossover)
        population_fitness = fitness_calc(pop, r)
        
        new_best = np.max(population_fitness)
        if new_best > best_fitness_generation[-1]:
            best = pop[np.argmax(population_fitness)]
        best_fitness_generation.append(new_best)
        
        mean_fitness_generation.append(np.mean(population_fitness))
        standard_fitness_generation.append(np.std(population_fitness))
         
        print("\n------------------------------------------------------------------")
        print(f"Generation {i+1}. Mean {mean_fitness_generation[-1]}, best {best_fitness_generation[-1]}")
        print("------------------------------------------------------------------")
        
        solutions = [pop, population_fitness]
        env.update_solutions(solutions)
    
    #Saving the file
    with open(f"{exp_name}/winner_{r}.pkl", "wb") as f:
        pickle.dump(best, f)
        f.close()