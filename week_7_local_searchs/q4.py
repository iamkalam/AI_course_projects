import random
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np

NUM_JOBS = 5
NUM_OPS = 3
NUM_MACHINES = 3

PROCESSING_TIMES = [
    [(0,3), (1,2), (2,4)], 
    [(1,5), (2,1), (0,6)], 
    [(2,4), (0,3), (1,2)], 
    [(0,2), (2,5), (1,4)], 
    [(1,3), (0,4), (2,3)]
]

def initial_sequence():
    seq = [(j, o) for j in range(NUM_JOBS) for o in range(NUM_OPS)]
    random.shuffle(seq)
    return seq

def makespan(sequence):
    machine_free = [0.0] * NUM_MACHINES
    job_end = [0.0] * NUM_JOBS
    op_end = {}
    
    for (job, op) in sequence:
        machine, ptime = PROCESSING_TIMES[job][op]
        prev_end = op_end.get((job, op-1), 0) if op > 0 else 0
        start = max(machine_free[machine], job_end[job], prev_end)
        end = start + ptime
        machine_free[machine] = end
        job_end[job] = end
        op_end[(job, op)] = end
    
    return max(machine_free)

def get_neighbors(sequence):
    n = len(sequence)
    for i in range(n - 1):
        new_seq = sequence[:]
        new_seq[i], new_seq[i+1] = new_seq[i+1], new_seq[i]
        yield new_seq, (i, i+1)

def tabu_search(initial_seq, tenure, max_iter=1000):
    current = initial_seq[:]
    best = current[:]
    tabu_list = set()
    trigger_count = 0
    
    for it in range(max_iter):
        neighbors_list = list(get_neighbors(current))
        best_nb_cost = makespan(best)
        best_nb = None
        best_swap = None
        tabu_swap = False
        
        for nb_seq, swap in neighbors_list:
            swap_id = frozenset(swap)
            is_tabu = swap_id in tabu_list
            nb_cost = makespan(nb_seq)
            
            if (nb_cost < makespan(current) or not is_tabu or nb_cost < best_nb_cost):
                if best_nb is None or nb_cost < makespan(best_nb):
                    best_nb = nb_seq
                    best_swap = swap_id
                    tabu_swap = is_tabu
        
        if best_nb is None:
            break
        
        current = best_nb
        tabu_list.add(best_swap)
        if len(tabu_list) > tenure:
            # Simple FIFO
            tabu_list = set(list(tabu_list)[1:])
        
        if tabu_swap and makespan(current) < best_nb_cost:
            trigger_count += 1
        
        if makespan(current) < makespan(best):
            best = current[:]
    
    return makespan(best), trigger_count > 0, best

def random_search(initial_seq, max_iter=1000):
    current = initial_seq[:]
    best = current[:]
    for _ in range(max_iter):
        nb_seq, _ = random.choice(list(get_neighbors(current)))
        if makespan(nb_seq) < makespan(best):
            best = nb_seq[:]
        current = nb_seq
    return makespan(best), best

def plot_gantt(sequence, title):
    # Compute schedule details
    machine_free = [0.0] * NUM_MACHINES
    job_end = [0.0] * NUM_JOBS
    op_end = {}
    schedules = [[] for _ in range(NUM_MACHINES)]
    
    for (job, op) in sequence:
        machine, ptime = PROCESSING_TIMES[job][op]
        prev_end = op_end.get((job, op-1), 0) if op > 0 else 0
        start = max(machine_free[machine], job_end[job], prev_end)
        end = start + ptime
        schedules[machine].append((job, op, start, end))
        machine_free[machine] = end
        job_end[job] = end
        op_end[(job, op)] = end
    
    fig, ax = plt.subplots(figsize=(12, 6))
    colors = plt.cm.Set3(np.linspace(0, 1, NUM_JOBS))
    
    for m in range(NUM_MACHINES):
        for job, op, start, end in schedules[m]:
            ax.barh(m, end - start, left=start, height=0.8, color=colors[job], edgecolor='black')
            ax.text((start + end)/2, m, f'J{job}-O{op}', ha='center', va='center', color='white')
    
    ax.set_xlabel('Time')
    ax.set_ylabel('Machine')
    ax.set_title(title)
    ax.grid(True, axis='x')
    plt.show()

TENURES = [3, 7, 15]

if __name__ == '__main__':
    random.seed(42)
    initial = initial_sequence()
    print('JSSP Tabu Search Results:')
    print('Tenure | Makespan | Aspiration')
    
    best_overall = initial
    min_makespan = makespan(initial)
    
    for tenure in TENURES:
        cost, triggered, best = tabu_search(initial, tenure)
        print(f'{tenure:5} | {cost:7.1f} | {triggered}')
        if cost < min_makespan:
            min_makespan = cost
            best_overall = best
    
    # Baseline
    rand_cost, rand_best = random_search(initial)
    print(f'Random: {rand_cost:.1f}')
    
    print('Best schedule Gantt:')
    plot_gantt(best_overall, f'Best Schedule (Makespan {min_makespan:.1f})')
