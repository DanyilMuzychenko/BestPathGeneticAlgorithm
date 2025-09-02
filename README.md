# Optimization of Delivery Route Using Genetic Algorithm
A system for finding the most optimal route between ten cities using a genetic algorithm.

<p align="center">
   <img src="https://img.shields.io/badge/Engine-PyCharm%2023-B7F352" alt="Engine">
</p>

## 📌 About

The purpose of this project is to apply a **genetic algorithm** to optimize delivery routes for a courier company that serves a set of clients with specific locations and packages to deliver.  
The main objective is to find an **optimal route** that minimizes the total cost or delivery time.  
The genetic algorithm efficiently explores the space of possible routes, considering delivery constraints and preferences, to provide the courier company with an **optimal logistics solution**.

---

## 📖 Documentation

### 🔧 Libraries
- `numpy`
- `random`
- `matplotlib`
- `folium`

### 🗂 Data Definition
- Prepared distance matrices between cities, fuel costs, and fuel consumption.

### 🧬 Genotype Generation
- Creates a random route in the form of, for example:  
  `{5, 2, 6, 4, 1, 3, 7, 9, 10, 8}`

### 🌱 Population Initialization
- Generates an initial population with size defined by `SELF_SIZE`.

### 📊 Fitness Evaluation
- Calculates route efficiency based on **distance, cost, and fuel consumption**.

### 🔄 Population Evolution
- Implements a genetic algorithm including:
  - Selection
  - Crossover
  - Mutation
  - Fitness evaluation of each individual

### 🚀 Optimization
- Runs through several generations with GA settings such as:
  - Number of generations
  - Tournament size
  - Crossover probability
  - Mutation probability

### 🗺 Visualization of Results
- Uses **Folium** to create an interactive map showing cities and the optimal route.

---

## 👨‍💻 Developers
- [Danyil Muzychenko](https://github.com/DanyilMuzychenko)
