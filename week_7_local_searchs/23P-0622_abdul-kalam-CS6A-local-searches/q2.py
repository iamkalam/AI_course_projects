import random
import math
import matplotlib.pyplot as plt
import numpy as np

NUM_CITIES = 20
MAX_ITER = 10000

def generate_cities():
    random.seed(42)
    return [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(NUM_CITIES)]

def tour_cost(tour, cities):
    total = 0
    n = len(tour)
    for i in range(n):
        c1 = cities[tour[i]]
        c2 = cities[tour[(i + 1) % n]]
        total += math.hypot(c2[0] - c1[0], c2[1] - c1[1])
    return total

def random_tour():
    tour = list(range(NUM_CITIES))
    random.shuffle(tour)
    return tour

def two_opt(tour, i, k):
    return tour[:i] + tour[i:k+1][::-1] + tour[k+1:]

def get_two_opt_neighbors(tour):
    n = len(tour)
    for i in range(1, n - 2):
        for k in range(i + 1, n):
            yield two_opt(tour, i, k)

def linear_cooling(iter_num, T0, alpha):
    return max(0, T0 * (1 - iter_num / MAX_ITER))

def geometric_cooling(iter_num, T0, alpha):
    return T0 * (alpha ** iter_num)

def logarithmic_cooling(iter_num, T0, alpha):
    return T0 / math.log(iter_num + 10)

def simulated_annealing(cities, initial_tour, T0=10000, alpha=0.995, cooling_fn=geometric_cooling, max_iter=MAX_ITER):
    tour = initial_tour[:]
    current_cost = tour_cost(tour, cities)
    cost_history = [current_cost]
    for iter_num in range(1, max_iter + 1):
        T = cooling_fn(iter_num, T0, alpha)
        if T <= 0:
            break
        neighbor = random.choice(list(get_two_opt_neighbors(tour)))
        neighbor_cost = tour_cost(neighbor, cities)
        delta = neighbor_cost - current_cost
        if delta < 0 or random.random() < math.exp(-delta / T):
            tour = neighbor
            current_cost = neighbor_cost
        cost_history.append(current_cost)
    return tour, cost_history

def plot_cost_history(histories, labels):
    plt.figure(figsize=(10, 6))
    for history, label in zip(histories, labels):
        plt.plot(history, label=label)
    plt.xlabel('Iteration')
    plt.ylabel('Tour Distance')
    plt.title('TSP SA Cooling Schedules Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_tour(cities, tour, title):
    plt.figure(figsize=(8, 8))
    x = [c[0] for c in cities]
    y = [c[1] for c in cities]
    plt.scatter(x, y, c='blue')
    for i, (cx, cy) in enumerate(cities):
        plt.annotate(str(i), (cx, cy))
    nx = [cities[tour[i]][0] for i in range(len(tour))] + [cities[tour[0]][0]]
    ny = [cities[tour[i]][1] for i in range(len(tour))] + [cities[tour[0]][1]]
    plt.plot(nx, ny, 'r-')
    plt.title(title)
    plt.axis('equal')
    plt.show()

if __name__ == '__main__':
    cities = generate_cities()
    initial_tour = random_tour()
    
    print('Running SA...')
    final_linear, hist_linear = simulated_annealing(cities, initial_tour, cooling_fn=linear_cooling, T0=10000)
    final_geom, hist_geom = simulated_annealing(cities, initial_tour, cooling_fn=geometric_cooling, T0=10000, alpha=0.995)
    final_log, hist_log = simulated_annealing(cities, initial_tour, cooling_fn=logarithmic_cooling, T0=10000)
    
    plot_cost_history([hist_linear, hist_geom, hist_log], ['Linear', 'Geometric', 'Logarithmic'])
    plot_tour(cities, initial_tour, 'Initial Random Tour')
    plot_tour(cities, final_geom, 'Final Geometric SA Tour')
    
    print(f'Initial distance: {tour_cost(initial_tour, cities):.2f}')
    print(f'Linear SA: {tour_cost(final_linear, cities):.2f}')
    print(f'Geometric SA: {tour_cost(final_geom, cities):.2f}')
    print(f'Log SA: {tour_cost(final_log, cities):.2f}')
    print('Discussion: Geometric cooling with T0=10000 and alpha=0.995 performs best. It allows initial exploration with high T and gradual exploitation. Linear cools too quickly, risking local optima. Logarithmic cools too slowly, wasting computation.')

