import random
import time
import matplotlib.pyplot as plt
import numpy as np

N = 8

def attacks(state):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if abs(i - j) == abs(state[i] - state[j]):
                count += 1
    return count

def random_state():
    return [random.randint(0, N-1) for _ in range(N)]

def get_neighbors(state):
    for row in range(N):
        old_col = state[row]
        for new_col in range(N):
            if new_col != old_col:
                new_state = state[:]
                new_state[row] = new_col
                yield new_state

def steepest_ascent_hc():
    state = random_state()
    while True:
        neighbors = list(get_neighbors(state))
        if not neighbors:
            break
        costs = [(attacks(nb), nb) for nb in neighbors]
        min_cost, best_nb = min(costs)
        if min_cost >= attacks(state):
            break
        state = best_nb
    return attacks(state)

def first_choice_hc():
    state = random_state()
    steps = 0
    max_steps = 100
    while steps < max_steps:
        current_cost = attacks(state)
        neighbor = None
        for nb in get_neighbors(state):
            if attacks(nb) < current_cost:
                neighbor = nb
                break
        if neighbor is None:
            break
        state = neighbor
        steps += 1
    return attacks(state)

def random_restart_hc(max_restarts=1000):
    for restarts in range(1, max_restarts + 1):
        cost = steepest_ascent_hc()
        if cost == 0:
            return restarts, 0
    return max_restarts, cost

def run_steepest(num_runs=100):
    successes = sum(1 for _ in range(num_runs) if steepest_ascent_hc() == 0)
    return successes / num_runs * 100

def run_first_choice(num_runs=100):
    total_time = 0
    successes = 0
    for _ in range(num_runs):
        start = time.time()
        cost = first_choice_hc()
        total_time += time.time() - start
        if cost == 0:
            successes += 1
    return successes / num_runs * 100, total_time / num_runs

def run_random_restart(num_trials=100, max_restarts=1000):
    total_restarts = 0
    successes = 0
    for _ in range(num_trials):
        restarts, cost = random_restart_hc(max_restarts)
        if cost == 0:
            successes += 1
            total_restarts += restarts
    avg_restarts = total_restarts / max(1, successes)
    return successes / num_trials * 100, avg_restarts

def plot_comparison():
    # Run experiments
    steepest_sr = run_steepest(100)
    fc_sr, fc_time = run_first_choice(100)
    rr_sr, rr_restarts = run_random_restart(100)
    
    methods = ['Steepest', 'First-Choice', 'Random-Restart']
    success_rates = [steepest_sr, fc_sr, rr_sr]
    
    x = np.arange(len(methods))
    width = 0.35
    
    fig, ax = plt.subplots()
    bars = ax.bar(x, success_rates, width, label='Success Rate (%)')
    ax.set_ylabel('Success Rate (%)')
    ax.set_title('8-Queens Hill Climbing Variants Comparison')
    ax.set_xticks(x)
    ax.set_xticklabels(methods)
    ax.legend()
    
    # Annotate
    for bar, sr in zip(bars, success_rates):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{sr:.1f}%', ha='center', va='bottom')
    
    print(f'Steepest success rate: {steepest_sr:.2f}%')
    print(f'First-choice success: {fc_sr:.2f}%, avg time: {fc_time*1000:.2f}ms')
    print(f'Random-restart success: {rr_sr:.2f}%, avg restarts: {rr_restarts:.1f}')
    plt.show()

if __name__ == '__main__':
    plot_comparison()

