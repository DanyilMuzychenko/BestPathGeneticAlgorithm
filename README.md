Optimization-of-delivery-route-using-genetic-algorithm

A system for finding the most optimal route between ten cities using a genetic algorithm.

<p align="center"> <img src="https://img.shields.io/badge/Engine-PyCharm%2023-B7F352" alt="Engine"> </p>
About

The goal of this project is to apply a genetic algorithm to optimize delivery routes for a courier company that serves a set of clients with specific locations and packages to deliver. The main objective is to find the optimal route that minimizes the total cost or delivery time. The genetic algorithm is used to efficiently explore the space of possible routes, considering delivery constraints and preferences, in order to provide the courier company with an optimal logistics solution.
</br>

Documentation
Libraries

numpy, random, matplotlib, folium

Data definition

Distance matrices between cities, fuel costs, and fuel consumption data are prepared.

Genotype generation

Generates a random route, e.g. {5, 2, 6, 4, 1, 3, 7, 9, 10, 8}.

Population initialization

Creates an initial population of size defined by SELF_SIZE.

Fitness evaluation

Calculates route efficiency based on distance, cost, and fuel consumption.

Population evolution

Implements the genetic algorithm including selection, crossover, mutation, and fitness evaluation of each individual.

Optimization

Runs for several generations, applying GA settings such as number of generations, tournament size, crossover probability, and mutation probability.

Results visualization

Uses Folium to generate an interactive map showing the cities and the optimal route.

Developers

Danyil Muzychenko (https://github.com/DanyilMuzychenko
)
