# Boolean Satisfiability Solver (SAT Solver) using DPLL

This project implements a Boolean SAT solver in Python using the DPLL (Davis–Putnam–Logemann–Loveland) algorithm.

The solver reads logical formulas in DIMACS CNF format and determines whether the formula is satisfiable (SAT) or unsatisfiable (UNSAT).


## Project Flow

- Reads SAT problems from `.cnf` files in DIMACS CNF format
- Parses the file and converts it into a Python structure (list of clauses)
- Uses the DPLL backtracking algorithm to find a valid assignment
- Applies unit propagation to simplify the formula
- Returns whether the formula is SAT or UNSAT

## How it works

The project has three main components:

### 1. Parser (`parser.py`)
- Reads the `.cnf` file
- Extracts number of variables and clauses
- Converts clauses into a list of integer lists

Example:
```
1 -2 0
-1 3 0
```
becomes:
[[1,-2],[-1,3]]


### 2. Solver (`solver.py`)
Implements the DPLL algorithm:

- Simplifies clauses using current assignments
- Applies unit propagation
- Recursively tries variable assignments
- Backtracks if a contradiction is found

---

### 3. Main runner (`main.py`)
- Reads input `.cnf` files
- Calls the parser
- Calls the solver
- Prints SAT or UNSAT

## Results

A naive brute-force SAT solver checks all possible assignments, which takes `O(2^n)` time for `n` variables.

The DPLL-based solver implemented in this project still has a worst-case complexity of `O(2^n)`, but in practice it runs much faster because it reduces the search space using unit propagation, clause simplification, and early backtracking.

These optimizations allow the solver to avoid exploring most invalid assignments, significantly improving computation time compared to naive brute-force methods.


| Example      | Variables | Naive checks (2^n) | DPLL checks | Reduction |
|-------------|-----------|--------------------|-------------|-----------|
| sat1.cnf   | 3         | 8                  | ~3          | ~62%      |
| sat2.cnf   | 3         | 8                  | ~2          | ~75%      |
| unsat1.cnf | 1         | 2                  | 1           | 50%       |
| unsat2.cnf | 2         | 4                  | 1           | 75%       |


