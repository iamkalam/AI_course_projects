# 🤖 AI Algorithms Lab

> A comprehensive collection of search algorithms implementations for FAST NUCES AI Lab

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Active-green)

This repository contains implementations and exercises covering fundamental and advanced search algorithms used in Artificial Intelligence. It progresses from basic graph traversal to heuristic-based optimization.

---

## 📚 Table of Contents

1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Algorithms Covered](#algorithms-covered)
4. [Week-by-Week Breakdown](#week-by-week-breakdown)
5. [How to Run](#how-to-run)
6. [Key Concepts](#key-concepts)
7. [Future Work](#future-work)
8. [References](#references)

---

## Overview

This repository is part of the AI Lab coursework at FAST NUCES, covering essential search algorithms used in problem-solving, pathfinding, and optimization. The content progresses from basic uninformed search (BFS, DFS) to advanced informed search algorithms (A*, UCS).

### Learning Journey

```
Week 1-2: Basic Concepts
        ↓
Week 3: Graph Traversal (BFS, DFS)
        ↓
Week 4: Advanced Search (UCS, A*)
        ↓
Future:  Reinforcement Learning, Game Theory, etc.
```

---

## Project Structure

```
AI_LAb/
├── test.ipynb                    # Quick testing notebook
├── week_3/
│   ├── bfs_dfs_task.ipynb        # BFS & DFS practice tasks
│   ├── task1.ipynb               # Additional practice
│   └── test.py                   # Python test file
├── week_4/
│   ├── question1.ipynb           # Campus Navigation (BFS, UCS)
│   ├── question2.ipynb           # Ride-Sharing Optimization (A*)
│   ├── question3.ipynb           # 8-Puzzle Solver (A* vs BFS)
│   └── README.md                 # Week 4 detailed documentation
└── README.md                     # This file
```

---

## Algorithms Covered

### Uninformed Search (No Heuristic)
| Algorithm | Description | Time Complexity | Use Case |
|-----------|-------------|-----------------|----------|
| **BFS** | Breadth-First Search - explores level by level | O(V + E) | Shortest path in unweighted graphs |
| **DFS** | Depth-First Search - explores depth-first | O(V + E) | Path finding, cycle detection |
| **UCS** | Uniform Cost Search - explores by accumulated cost | O(E + V log V) | Weighted shortest path |

### Informed Search (Uses Heuristic)
| Algorithm | Description | Use Case |
|-----------|-------------|----------|
| **Greedy Best-First** | Uses only heuristic h(n) | Fast but not optimal |
| **A* Search** | Combines g(n) + h(n) | Optimal with admissible heuristic |

### Heuristics Used
- **Manhattan Distance**: |x₁ - x₂| + |y₁ - y₂| (grid-based problems)
- **Euclidean Distance**: √((x₁-x₂)² + (y₁-y₂)²) (straight-line distance)
- **Minimum Distance**: Nearest neighbor heuristic

---

## Week-by-Week Breakdown

### 📅 Week 3: BFS & DFS Fundamentals

**Location**: `week_3/`

**Topics Covered:**
- Graph representation (adjacency list)
- Queue-based BFS implementation
- Stack-based DFS implementation
- Path finding with BFS and DFS
- Comparing BFS (shortest path) vs DFS (any path)

**Key Tasks:**
- Trace BFS/DFS on sample graphs
- Find shortest path from A to F
- Understand queue and stack behaviors

**Files:**
- `bfs_dfs_task.ipynb` - Complete BFS/DFS implementations
- `task1.ipynb` - Practice exercises

---

### 📅 Week 4: Uninformed & Informed Search

**Location**: `week_4/`

**Question 1: Campus Navigation System**
- Problem: Find shortest path between FAST campus buildings
- Algorithms: BFS (minimum hops) vs UCS (minimum cost)
- Graph: Weighted campus map with walking times
- **Result**: Both find same path but UCS provides cost optimization

**Question 2: Ride-Sharing Route Optimization**
- Problem: Optimize pickup order for 3 passengers
- Algorithm: A* Search with minimum distance heuristic
- State Space: (driver_location, set_of_picked_passengers)
- **Result**: Optimal pickup order using heuristic guidance

**Question 3: 8-Puzzle Solver**
- Problem: Solve sliding tile puzzle
- Algorithms: A* (Manhattan distance) vs BFS
- Heuristic: Sum of Manhattan distances to goal positions
- **Result**: A* explores significantly fewer nodes than BFS

---

## How to Run

### Using Jupyter Notebook
```bash
# Open in Jupyter
jupyter notebook

# Or use VS Code
code .
```

### Running Python Files
```bash
# Run test file
python week_3/test.py
```

### Example Outputs

**BFS Path Finding:**
```
✓ Path found!
  Path: Peshawar → Islamabad → Lahore → Multan → Karachi
  Steps: 4
```

**8-Puzzle Solver:**
```
A* Solution Depth: [number]
A* Nodes Explored: [number]
BFS Solution Depth: [number]
BFS Nodes Explored: [number]
```

---

## Key Concepts

### When to Use Which Algorithm?

```
┌─────────────────────────────────────────────────────────────┐
│                    Algorithm Selection                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Need shortest path in UNWEIGHTED graph?  →  BFS           │
│                                                              │
│  Need shortest path in WEIGHTED graph?    →  UCS           │
│                                                              │
│  Need optimal path with HEURISTIC?        →  A*            │
│                                                              │
│  Need ANY path quickly?                   →  DFS          │
│                                                              │
│  Search space is HUGE but heuristic good? →  Greedy Best-First│
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Heuristic Properties

| Property | Description | Required for A*? |
|----------|-------------|------------------|
| **Admissible** | Never overestimates true cost | Yes (for optimality) |
| **Consistent** | Satisfies triangle inequality | No (but helps) |
| **Dominance** | h₁ ≥ h₂ explores fewer nodes | No (but better) |

---

## Future Work

This repository will be expanded with more AI algorithms and projects:

### 🔮 Planned Topics

- [ ] **Week 5: Local Search Algorithms**
  - Hill Climbing
  - Simulated Annealing
  - Genetic Algorithms

- [ ] **Week 6: Game Theory**
  - Minimax Algorithm
  - Alpha-Beta Pruning
  - Game Trees

- [ ] **Week 7: Constraint Satisfaction Problems**
  - Backtracking Search
  - AC-3 Algorithm
  - Sudoku Solver

- [ ] **Week 8: Reinforcement Learning**
  - Q-Learning
  - Value Iteration
  - Policy Gradient

### 🎯 Project Ideas

- Maze Solver with multiple algorithms
- Route Planning App (like Google Maps)
- AI Game Player (Chess, Checkers, Tic-Tac-Toe)
- Sudoku Solver
- N-Puzzle Solver optimization
- Robotics Path Planning

---

## References

### Books
- 📖 Russell, S. & Norvig, P. - *Artificial Intelligence: A Modern Approach* (4th Edition)

### Online Resources
- [A* Search Algorithm - Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm)
- [8-Puzzle Problem](https://en.wikipedia.org/wiki/15_puzzle)
- [BFS vs DFS](https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/)

### Additional Learning
- [CS188 UC Berkeley - Artificial Intelligence](https://inst.eecs.berkeley.edu/~cs188/)
- [AI Playlist by Abdul Bari](https://www.youtube.com/)

---

## Contributing

This is a learning repository. Feel free to:
1. Fork the repository
2. Add improvements
3. Fix bugs
4. Add new algorithms

---

## License

This project is for educational purposes as part of FAST NUCES AI Lab.

---

## Author

**FAST NUCES AI Lab**
- Course: Artificial Intelligence
- Semester: [Current]

*Last Updated: 2024*

---

<div align="center">

⭐ Star this repository if you find it helpful!

</div>

