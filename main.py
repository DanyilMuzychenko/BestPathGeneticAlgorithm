import random
import numpy as np
import folium
import matplotlib.pyplot as plt

population_size = 450

#Warunek 1: Lokalizacje 10 klientów jako współrzędne geograficzne
customer_coordinates = [
    (52.263990, 21.054513),  # Przykładowe współrzędne dla K1
    (52.413848, 16.826326),  # Przykładowe współrzędne dla K22
    (51.124665, 16.987980),  # Przykładowe współrzędne dla K3
    (50.044952, 21.984596),  # Przykładowe współrzędne dla K4
    (50.870263, 20.612205),  # Przykładowe współrzędne dla K5
    (51.246521, 22.514655),  # Przykładowe współrzędne dla K6
    (51.406053, 21.129693),  # Przykładowe współrzędne dla K7
    (51.866529, 20.861594),  # Przykładowe współrzędne dla K8
    (52.080078, 21.024170),  # Przykładowe współrzędne dla K9
    (52.217933, 21.219304)   # Przykładowe współrzędne dla K10
]

# Zdefiniuj macierz kosztów (przykład)
cost_matrix = np.array([
    # K1, K2, ..., K10
    [0, 10, 15, 20, 25, 30, 35, 40, 45, 50],  # K1
    [10, 0, 12, 18, 30, 35, 40, 45, 50, 55],  # K2
    [15, 12, 0, 14, 22, 28, 35, 40, 45, 50],  # K3
    [20, 18, 14, 0, 10, 15, 25, 30, 35, 40],  # K4
    [25, 30, 22, 10, 0, 8, 16, 20, 25, 30],   # K5
    [30, 35, 28, 15, 8, 0, 12, 18, 22, 28],   # K6
    [35, 40, 35, 25, 16, 12, 0, 10, 15, 20],  # K7
    [40, 45, 40, 30, 20, 18, 10, 0, 8, 14],   # K8
    [45, 50, 45, 35, 25, 22, 15, 8, 0, 10],   # K9
    [50, 55, 50, 40, 30, 28, 20, 14, 10, 0]   # K10
])

# Inne założenia
#customer_coordinates = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(10)]

def calculate_total_cost(route, cost_matrix):
    total_cost = 0
    for i in range(len(route) - 1):
        from_customer = route[i] - 1
        to_customer = route[i + 1] - 1
        total_cost += cost_matrix[from_customer][to_customer]

    return total_cost

# Warunek 1 :
class Genotype:
    def __init__(self, sequence):
        self.sequence = sequence  # Sekwencja odwiedzanych klientów
        self.fitness = None  # Dodaj atrybut fitness

    def __repr__(self):
        return f"Genotype(sequence={self.sequence}, fitness={self.fitness})"

#Inicjalizacja genotypu
initial_sequence = list(range(len(customer_coordinates)))  # Inicjalna sekwencja to kolejność klientów
random.shuffle(initial_sequence)  # Losowe tasowanie sekwencji
initial_genotype = Genotype(sequence=initial_sequence)

print(initial_genotype)

# Warunek 2 :
class Population:
    def __init__(self, size, gene_length):
        self.size = size
        self.gene_length = gene_length
        self.chromosomes = self._initialize_population()

    def _initialize_population(self):
        initial_population = []
        for _ in range(self.size):
            sequence = list(range(self.gene_length))
            random.shuffle(sequence)
            genotype = Genotype(sequence)
            initial_population.append(genotype)
        return initial_population


# Przykład inicjalizacji populacji
gene_length = len(customer_coordinates)
initial_population = Population(size=population_size, gene_length=gene_length)

# Wyświetlenie pierwszych kilku chromosomów z populacji
for i in range(10):
    print(initial_population.chromosomes[i])

def evaluate_population(population, cost_matrix):
    for chromosome in population.chromosomes:
        total_cost = calculate_total_cost(chromosome.sequence, cost_matrix)
        chromosome.fitness = 1 / total_cost  # Im mniejszy koszt, tym lepsza ocena fitness

# Przykład użycia
evaluate_population(initial_population, cost_matrix)

# Wyświetlenie oceny fitness dla pierwszych kilku chromosomów z populacji
for i in range(10):
    print(f"Chromosome {i + 1}: Fitness = {initial_population.chromosomes[i].fitness}")

#w5
def tournament_selection(population, tournament_size):
    selected_chromosomes = []
    for _ in range(len(population.chromosomes)):
        tournament_candidates = random.sample(population.chromosomes, tournament_size)
        winner = max(tournament_candidates, key=lambda x: x.fitness)
        selected_chromosomes.append(winner)
    return selected_chromosomes


def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1.sequence) - 1)
    child_sequence = parent1.sequence[:crossover_point] + [gene for gene in parent2.sequence if
                                                           gene not in parent1.sequence[:crossover_point]]
    return Genotype(sequence=child_sequence)


def mutation(chromosome, mutation_rate):
    if random.uniform(0, 1) < mutation_rate:
        mutation_points = random.sample(range(len(chromosome.sequence)), 2)
        chromosome.sequence[mutation_points[0]], chromosome.sequence[mutation_points[1]] = chromosome.sequence[
            mutation_points[1]], chromosome.sequence[mutation_points[0]]

        # Sprawdzanie unikalności wszystkich genów w sekwencji
        while len(set(chromosome.sequence)) < len(chromosome.sequence):
            mutation_points = random.sample(range(len(chromosome.sequence)), 2)
            chromosome.sequence[mutation_points[0]], chromosome.sequence[mutation_points[1]] = chromosome.sequence[
                mutation_points[1]], chromosome.sequence[mutation_points[0]]

    return chromosome


def generate_next_generation(population, tournament_size, crossover_rate, mutation_rate):
    selected_chromosomes = tournament_selection(population, tournament_size)

    new_population = Population(size=population.size, gene_length=population.gene_length)

    for i in range(0, len(selected_chromosomes), 2):
        parent1 = selected_chromosomes[i]
        parent2 = selected_chromosomes[i + 1] if i + 1 < len(selected_chromosomes) else selected_chromosomes[i]

        # Krzyżowanie
        if random.uniform(0, 1) < crossover_rate:
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
        else:
            child1, child2 = parent1, parent2

        # Mutacja
        child1 = mutation(child1, mutation_rate)
        child2 = mutation(child2, mutation_rate)

        new_population.chromosomes[i] = child1
        new_population.chromosomes[i + 1] = child2

    return new_population

def evolutionary_algorithm_with_stopping_criteria(population_size, gene_length, cost_matrix, max_generations, tournament_size, crossover_rate, mutation_rate, improvement_threshold=10):
    # Inicjalizacja początkowej populacji
    population = Population(size=population_size, gene_length=gene_length)
    evaluate_population(population, cost_matrix)

    # Główna pętla ewolucji
    best_fitness_history = []  # Lista do śledzenia najlepszego fitness w kolejnych pokoleniach
    generations_without_improvement = 0

    for generation in range(max_generations):
        # Generowanie nowego pokolenia
        new_population = generate_next_generation(population, tournament_size, crossover_rate, mutation_rate)

        # Ocenianie nowego pokolenia
        evaluate_population(new_population, cost_matrix)

        # Elitaryzm: Zachowanie najlepszego chromosomu z poprzedniego pokolenia
        best_previous = max(population.chromosomes, key=lambda x: x.fitness)
        best_current = max(new_population.chromosomes, key=lambda x: x.fitness)

        if best_current.fitness > best_previous.fitness:
            new_population.chromosomes[random.randint(0, population_size - 1)] = best_previous
            generations_without_improvement = 0
        else:
            generations_without_improvement += 1

        # Zastępujemy poprzednią populację nową
        population = new_population

        # Dodaj aktualny najlepszy fitness do historii
        best_fitness_history.append(best_current.fitness)

        # Wyświetlanie najlepszego rozwiązania w danym pokoleniu
        print(f"Generation {generation + 1}: Best Fitness = {best_current.fitness}")

        # Warunek zatrzymania: Brak znaczącej poprawy przez określoną liczbę pokoleń
        if generations_without_improvement >= improvement_threshold:
            print(f"\nStopping criteria met: No improvement for {improvement_threshold} generations.")
            break

    return max(population.chromosomes, key=lambda x: x.fitness), best_fitness_history

# Parametry algorytmu genetycznego
gene_length = len(customer_coordinates)
max_generations = 10
tournament_size = 5
crossover_rate = 0.7
mutation_rate = 0.3


def plot_route_on_map(route, customer_coordinates):
    map_center = [np.mean([coord[0] for coord in customer_coordinates]),
                  np.mean([coord[1] for coord in customer_coordinates])]
    folium_map = folium.Map(location=map_center, zoom_start=10)

    # Dodawanie znaczniki dla klientów
    for i, coord in enumerate(customer_coordinates):
        folium.Marker(location=coord, popup=f'K{i + 1}').add_to(folium_map)

    # Konwersja indeksów na współrzędne dla linii trasy
    route_coordinates = [customer_coordinates[i - 1] for i in route]  # reduce by 1 as indices start from 1

    # Dodawanie linię reprezentującą trasę
    folium.PolyLine(locations=route_coordinates, color='blue').add_to(folium_map)

    # Usuwanie linię łączącą ostatniego klienta z pierwszym klientem.
    folium_map.add_child(folium.Popup(folium.Html(f'<p>Route Length: Not Calculated</p>', script=True)))

    return folium_map

#Uruchomienie algorytmu genetycznego
best_solution, fitness_history = evolutionary_algorithm_with_stopping_criteria(
    population_size, gene_length, cost_matrix, max_generations, tournament_size, crossover_rate, mutation_rate
)

# Wyświetlanie najlepszego rozwiązania
print("\nBest Solution:")
print(best_solution)


# Wizualizacja trasy na mapie
folium_map = plot_route_on_map(best_solution.sequence, customer_coordinates)
folium_map.save('optimal_route_map.html')


def plot_fitness_history(fitness_history):
    plt.plot(range(1, len(fitness_history) + 1), fitness_history, marker='o')
    plt.title('Fitness History')
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.show()

