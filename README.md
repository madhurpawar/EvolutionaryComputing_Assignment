# EvoMan: Generalist Agent Training with Evolutionary Algorithms

## 📌 Overview

This project explores the use of Evolutionary Algorithms (EAs) to train **generalist agents** capable of playing multiple video game enemies in the [EvoMan](https://github.com/karinemiras/evoman_framework) simulation framework. A generalist agent is expected to perform well against a variety of enemies with differing abilities and strategies.

Two different EAs were implemented and evaluated, using a neural network controller with a single hidden layer of 10 neurons. The project focused on optimizing the network weights for robust gameplay performance across different enemy groups.

---

## 🎯 Objective

- Implement two EAs using the **Individual Evolution** mode of EvoMan.
- Train and evaluate generalist agents on two predefined groups of enemies.
- Compare EA performance based on fitness, Gain scores, and statistical significance.
- Submit the best-performing agent based on defined competition metrics.

---

## 🧠 EA Algorithms

### EA1: Default Fitness-Based Genetic Algorithm
- Fitness Function:  
  `fitness = 0.9 * (100 - enemy_energy) + 0.1 * player_energy - log(time)`
- Key Features:
  - One-point crossover
  - Random mutation
  - Selection: Top 20% elitism
  - Population: 100
  - Generations: 15

### EA2: Time-Invariant Fitness-Based Genetic Algorithm
- Fitness Function:  
  `fitness = 0.9 * (100 - enemy_energy) + 0.1 * player_energy`
- Identical EA setup, but **without time penalty** in fitness

---

## 🕹️ Enemy Groups

- **Group 1 (EA2 performed best)**:
  - Enemy 2: Airman
  - Enemy 5: Metalman
  - Enemy 8: Quickman

- **Group 2 (Both EAs performed similarly)**:
  - Enemy 3: Woodman
  - Enemy 4: Heatman
  - Enemy 7: Bubbleman

---

## ⚙️ Experimental Setup

- Neural Network: Feedforward, 10 hidden neurons
- Generations: 15
- Population Size: 
  - EA1: 100  
  - EA2: 70 (found to perform better)
- 10 independent runs per EA per group
- Each best solution tested 5 times per enemy
- Environment:
  - Difficulty level: 2
  - Contact hurt: "player"
  - Enemy mode: "static"
  - Multiple mode: "yes"

---

## 📊 Results

### Fitness Evolution (Avg ± Std)

- EA2 showed more consistent improvement and stabilization, especially for Group 1
- EA1 performance was more variable and generally lower on Group 1

### Box Plot: Gain Scores

- Group 1 (EA2) showed significantly higher Gain scores
- Statistical Test (T-Test):

| Group      | T-Statistic | p-Value |
|------------|-------------|---------|
| Enemies [2,5,8] | -2.963      | 0.010   |
| Enemies [3,4,7] | 0.004       | 0.996   |

> ✅ EA2 significantly outperformed EA1 for Group 1  
> ❌ No significant difference for Group 2

### Best Solution (Submitted)

- Algorithm: EA2  
- Enemy Group: [2, 5, 8]

| Enemy      | Player Energy | Enemy Energy |
|------------|----------------|----------------|
| Flashman   | 0              | 80             |
| Airman     | 84             | 0              |
| Woodman    | 0              | 70             |
| Heatman    | 0              | 40             |
| Metalman   | 57.5           | 0              |
| Crashman   | 0              | 50             |
| Bubbleman  | 0              | 20             |
| Quickman   | 22.6           | 0              |

---

## 💡 Key Insights
- Removing time from the fitness function (EA2) improved generalist performance.
- EA2 achieved statistically significant results for Group 1.
- Training agents on diverse enemy behavior leads to robust generalization.

---

## 📌 Future Work
- Experiment with varying mutation rates or dynamic mutation.
- Normalize neural network inputs for potentially better learning.
- Explore Neuroevolution techniques like NEAT for topology evolution.

---

## 📚 References
- Togelius, J., Karakovskiy, S., Baumgarten, R. *The 2009 Mario AI Competition*.
- Smit, S.K., & Eiben, A.E. (2014). *Parameter Tuning of Evolutionary Algorithms: Generalist vs. Specialist*.
- Hinterding, R., Eiben, A.E., & Michalewicz, Z. (1999). *Parameter Control in Evolutionary Algorithms*.

