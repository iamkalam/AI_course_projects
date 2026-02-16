# Week 4: Uninformed & Informed Search Algorithms

This week covers essential search algorithms used in AI for problem-solving, ranging from simple graph traversal to heuristic-based optimization.

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Question 1: Campus Navigation System](#question-1-campus-navigation-system)
3. [Question 2: Ride-Sharing Route Optimization](#question-2-ride-sharing-route-optimization)
4. [Question 3: 8-Puzzle Solver](#question-3-8-puzzle-solver)
5. [Key Concepts](#key-concepts)
6. [Algorithm Comparison](#algorithm-comparison)

---

## Overview

This week explores three fundamental search problems:

| Question | Problem | Algorithms Used |
|----------|---------|------------------|
| Q1 | Campus Navigation | BFS, UCS |
| Q2 | Ride-Sharing Pickup | A* Search |
| Q3 | 8-Puzzle Solver | A*, BFS |

---

## Question 1: Campus Navigation System

### Problem Statement
Design a navigation system for FAST Peshawar campus that helps students find the shortest path between buildings.

### Campus Graph Structure

```
        S
        |
        |2
        C1--------------C2
        |               |     
        |2              |2  
        |    1      1   |     3
        C3------M1------C4----------A
        |               |           |    
        |2              |1          |2
        |        2      |      1    |
        P---------------C5----------H
```

### Building Codes
- **S**: Main Gate (Start)
- **C1, C2, C3, C4, C5**: Academic Blocks
- **M1**: Mosque
- **A**: Admin Block
- **P**: Parking
- **H**: Hostel

### Algorithms Implemented

#### 1. Breadth-First Search (BFS)
- **Purpose**: Find path with fewest buildings (minimum hops)
- **Property**: Guarantees shortest path in unweighted graphs
- **Time Complexity**: O(V + E)

#### 2. Uniform Cost Search (UCS)
- **Purpose**: Find fastest walking path (minimum cost)
- **Property**: Works with weighted edges, explores lower-cost paths first
- **Time Complexity**: O(E + V log V)

### Results Comparison

| Metric | BFS | UCS |
|--------|-----|-----|
| Path | S → C1 → C3 → M1 → C4 → C5 → H | S → C1 → C3 → M1 → C4 → C5 → H |
| Hops | 6 | 6 |
| Total Cost | N/A | 8 |

**Conclusion**: While both algorithms find the same path in this case, UCS provides additional cost optimization for weighted graphs.

---

## Question 2: Ride-Sharing Route Optimization

### Problem Statement
A ride-sharing app needs to pick up 3 passengers. Design an algorithm to find the best pickup order.

### State Space Design
- **State**: (driver_location, set_of_picked_passengers)
- **Actions**: Travel to any unpicked passenger's location

### Algorithm: A* Search

#### The A* Formula
```
f(n) = g(n) + h(n)
```

Where:
- **g(n)**: Actual cost from start to node n
- **h(n)**: Heuristic estimate from node n to goal
- **f(n)**: Total estimated cost

### Heuristic Used
- **Minimum distance to nearest unpicked passenger**
- **Admissible**: Yes - never overestimates the true cost

### Example
```
Start Location: (0, 0)
Passengers:
  - P1: (2, 3)
  - P2: (5, 1)
  - P3: (6, 4)
```

### Key Insights

| Property | Description |
|----------|-------------|
| Admissibility | h(n) ≤ true cost (never overestimates) |
| Optimality | A* finds optimal solution with admissible heuristic |
| Completeness | Always finds a solution if one exists |

---

## Question 3: 8-Puzzle Solver

### Problem Statement
The 8-puzzle is a sliding tile puzzle. Implement an AI to solve it using A* with Manhattan distance heuristic.

### Initial State
```
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
| 4 |   | 5 |
+---+---+---+
| 7 | 8 | 6 |
+---+---+---+
```

### Goal State
```
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 7 | 8 |   |
+---+---+---+
```

### Algorithms Compared

#### 1. A* Search with Manhattan Distance
- **Heuristic**: Sum of Manhattan distances of all tiles from goal positions
- **Formula**: `|x1 - x2| + |y1 - y2|` for each tile

#### 2. Breadth-First Search (BFS)
- **Property**: Explores all nodes at depth d before depth d+1
- **Guarantee**: Finds optimal solution

### Performance Comparison

| Metric | A* | BFS |
|--------|-----|-----|
| Solution Depth | ✓ | ✓ |
| Nodes Explored | Significantly fewer | More |
| Efficiency | Higher with good heuristic | Lower |

**Key Finding**: A* with Manhattan distance dramatically reduces nodes explored compared to BFS, making it much more efficient for the 8-puzzle problem.

---

## Key Concepts

### Uninformed Search Algorithms
| Algorithm | Description | Use Case |
|-----------|-------------|----------|
| BFS | Explores level by level | Unweighted shortest path |
| DFS | Explores depth-first | Path finding, puzzle solving |
| UCS | Explores by cost | Weighted graphs |

### Informed Search Algorithms
| Algorithm | Description | Use Case |
|-----------|-------------|----------|
| Greedy Best-First | Uses only heuristic | Fast but not optimal |
| A* | Combines g(n) + h(n) | Optimal with admissible heuristic |

### Heuristic Properties
- **Admissible**: Never overestimates (always optimistic)
- **Consistent**: Satisfies triangle inequality
- **Dominance**: h1 ≥ h2 means h1 explores fewer nodes

---

## Algorithm Comparison

```
Search Algorithm Efficiency (General):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
A* (with good heuristic)  ████████████ 100%
A* (with poor heuristic) █████░░░░░░  50%
UCS                      ██████░░░░░░  60%
BFS                      ████░░░░░░░░  40%
DFS                      ██░░░░░░░░░░  20%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Running the Code

### Question 1
```python
# Run BFS
python question1.ipynb  # Contains BFS and UCS implementations

# Output:
# BFS Path: ['S', 'C1', 'C3', 'M1', 'C4', 'C5', 'H']
# UCS Path: ['S', 'C1', 'C3', 'M1', 'C4', 'C5', 'H']
# UCS Cost: 8
```

### Question 2
```python
# Run A* for pickup optimization
python question2.ipynb

# Output:
# Best pickup order: ['P1', 'P2', 'P3']
# Total distance: [calculated]
```

### Question 3
```python
# Run both A* and BFS
python question3.ipynb

# Output:
# A* Solution Depth: [number]
# A* Nodes Explored: [number]
# BFS Solution Depth: [number]
# BFS Nodes Explored: [number]
```

---

## Learning Outcomes

By completing this week's exercises, you should understand:

1. ✅ How to represent problems as graphs
2. ✅ The difference between informed and uninformed search
3. ✅ How to design and implement heuristics
4. ✅ The importance of admissibility in A*
5. ✅ When to use BFS, UCS, or A* based on problem characteristics
6. ✅ How heuristics affect search efficiency

---

## References

- Russell, S. & Norvig, P. - Artificial Intelligence: A Modern Approach
- A* Search Algorithm: https://en.wikipedia.org/wiki/A*_search_algorithm
- 8-Puzzle Problem: https://en.wikipedia.org/wiki/15_puzzle

---

*Generated for FAST NUCES AI Lab - Week 4*

