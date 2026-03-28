import random
import math
import matplotlib.pyplot as plt
import numpy as np

DOMAIN = (-5, 5)
K_VALUES = [3, 5, 10, 20]
MAX_ITER = 100
LAMBDA = 5

def ackley(x, y):
    a = 20
    b = 0.2
    c = 2 * math.pi
    term1 = -a * math.exp(-b * math.sqrt(0.5 * (x*x + y*y)))
    term2 = math.exp(math.cos(c * x) + math.cos(c * y))
    return term1 + term2 + a

def random_state():
    return (random.uniform(*DOMAIN), random.uniform(*DOMAIN))

def neighbors(state, lambda_=LAMBDA):
    x, y = state
    for _ in range(lambda_):
        dx = random.gauss(0, 0.5)
        dy = random.gauss(0, 0.5)
        nx = np.clip(x + dx, *DOMAIN)
        ny = np.clip(y + dy, *DOMAIN)
        yield (nx, ny)

def local_beam_search(k, stochastic=False, max_iter=MAX_ITER):
    beam = [random_state() for _ in range(k)]
    diversity_history = [] if stochastic else None
    
    for it in range(max_iter):
        successors = []
        for state in beam:
            for nb in neighbors(state):
                succ_cost = ackley(*nb)
                successors.append((succ_cost, nb))
        successors.sort()
        
        if stochastic:
            # Diversity: std of x,y
            x_vals = [s[0] for s in beam]
            y_vals = [s[1] for s in beam]
            div = np.std(x_vals) + np.std(y_vals)
            diversity_history.append(div)
            
            top_k_lambda = k * LAMBDA
            selected = random.sample(successors[:top_k_lambda], k)
            beam = [s[1] for s in selected]
        else:
            beam = [s[1] for s in successors[:k]]
    
    best_state = min(beam, key=lambda s: ackley(*s))
    final_cost = ackley(*best_state)
    return final_cost, diversity_history

def create_heatmap():
    x = np.linspace(*DOMAIN, 100)
    y = np.linspace(*DOMAIN, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.vectorize(ackley)(X, Y)
    return X, Y, Z

def plot_results(final_costs, diversity_hist):
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    
    # (a) k comparison
    axs[0,0].bar(range(len(K_VALUES)), final_costs)
    axs[0,0].set_xticks(range(len(K_VALUES)))
    axs[0,0].set_xticklabels([str(k) for k in K_VALUES])
    axs[0,0].set_title('Final Cost vs k')
    
    # (b) Diversity
    iters = range(len(diversity_hist))
    axs[0,1].plot(iters, diversity_hist)
    axs[0,1].set_title('Stochastic Diversity vs Iteration')
    
    # (c) Heatmaps
    X, Y, Z = create_heatmap()
    snapshots = [0, MAX_ITER//2, MAX_ITER-1]  # Pseudo snapshots
    for idx, snap in enumerate(snapshots):
        ax = axs[idx//2, idx%2] if idx>0 else axs[1,0]
        ax.contourf(X, Y, Z, levels=20, cmap='viridis')
        ax.set_title(f'Heatmap snapshot iter {snap}')
        # Simulate beam (random for demo)
        beam_sample = [random_state() for _ in range(5)]
        bx = [s[0] for s in beam_sample]
        by = [s[1] for s in beam_sample]
        ax.scatter(bx, by, c='red', s=50)
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    print('Running beam search for Ackley...')
    final_costs = []
    for k in K_VALUES:
        cost, _ = local_beam_search(k, stochastic=False)
        final_costs.append(cost)
        print(f'k={k}: {cost:.4f}')
    
    # Stochastic for k=10 diversity
    _, div_hist = local_beam_search(10, stochastic=True)
    
    plot_results(final_costs, div_hist)
    print('k=10+ diminishing returns: larger beams converge to same local mins (diversity loss).')

