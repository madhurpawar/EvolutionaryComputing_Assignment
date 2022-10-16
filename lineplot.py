import numpy as np
import matplotlib.pyplot as plt
import sys, os
import regex as re

sys.path.insert(0, 'evoman') 

def plot_fitness(general_names, N_runs, gens):
    fitnesses = np.zeros((len(experiment_names), N_runs, 2, gens))
    
    for exp_id, experiment_name in enumerate(experiment_names):       
        f_mean = np.zeros(shape=[N_runs,gens+1])
        f_max = np.zeros(shape=[N_runs,gens+1])

    for i in range(N_runs):
            f_mean = np.load(f"{experiment_name}/fitness_gens_{i}.npy")
            f_max = np.load(f"{experiment_name}/fitness_max_{i}.npy")
            fitnesses[exp_id, i, :, :] = np.array((f_mean[i*(gens+1):(i+1)*(gens+1)-1], f_max[i*(gens+1):(i+1)*(gens+1)-1]))


    mean_max_fitness = []
    stdev_max_fitness = []
    mean_mean_fitness = []
    stdev_mean_fitness = []
    plt.figure()
    for i in range(gens):
        
        fitnesses[fitnesses==0] = np.nan
        mean_mean_fitness = np.append(mean_mean_fitness, np.nanmean(fitnesses[:,:,0,i]))
        stdev_mean_fitness = np.append(stdev_mean_fitness, np.nanstd(fitnesses[:,:,0,i]))
        mean_max_fitness = np.append(mean_max_fitness,np.nanmean(fitnesses[:,:,1,i]))
        stdev_max_fitness = np.append(stdev_max_fitness,np.nanstd(fitnesses[:,:,1,i]))
        
  
    plt.plot(mean_mean_fitness, '-', label='mean')
    plt.plot(mean_max_fitness, '-', label='maximum')
    plt.fill_between(np.arange(0, gens), mean_mean_fitness - stdev_mean_fitness, 
                         mean_mean_fitness + stdev_mean_fitness, alpha=0.2)
    plt.fill_between(np.arange(0, gens), mean_max_fitness - stdev_max_fitness, 
                         mean_max_fitness + stdev_max_fitness, alpha=0.2)

    plt.title("Algorithm 1: Enemy 3, 4, 7")
    plt.xlabel("generations")
    plt.ylabel("fitness")
    plt.legend(loc=4)
    plt.ylim(-9, 110)
    plt.savefig(f"Lineplots/{experiment_names[-1]}", dpi=400)
    plt.show()


if __name__ == '__main__':
    # experiment names specified
    experiment_names = ['CrossoverII_hidden10_gen15_enemy[3, 4, 7]']
    N_runs = 10

    plot_fitness(experiment_names, N_runs, gens=15)

