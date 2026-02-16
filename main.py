# This file reads path from the commands line and calls 2 main functions:
from sat.parser import convert_file
from sat.solver import dpll_solver
files = [
    "examples/sat1.cnf",
    "examples/sat2.cnf",
    "examples/unSat1.cnf",
    "examples/unSat2.cnf",
]
# Go through all the present files
for one_file in files:
    # Save the return in vars and print it
    num_vars, clauses = convert_file(one_file)
    # print(num_vars,clauses)
    # Giving the dpll clauses and the current partial True/False values
    print(dpll_solver(clauses,{}))
    
    

# 1. parseDimacs()
# 2. dpllSover()  -> Calls the Solve method which has the dpll logic


