# Contains main logic for the DPLL algorithm

# Helper function
from operator import is_


def simplify_clauses(clauses, assignment):
    simplified = []

    for clause in clauses:
        clause_satisfied = False
        new_clause = []

        for lit in clause:
            var = abs(lit)

            if var in assignment:
                val = assignment[var]
                lit_is_true = val if lit > 0 else (not val)
                if lit_is_true:
                    clause_satisfied = True
                    break
                # literal is false under assignment, so drop it
                continue

            # unassigned literal stays
            new_clause.append(lit)

        if clause_satisfied:
            continue

        if len(new_clause) == 0:
            return None

        simplified.append(new_clause)

    return simplified

# Unit Propogation helper function
def unit_propagate(clauses,assignment):
    # track if we have made prpgress in the last pass
    is_changed = True

    while is_changed:
        is_changed = False

        # find the unit clause
        for clause in clauses:
            if len(clause) != 1:
                continue
            # Once we found it
            # Use the only literal in the clause
            lit = clause[0]
            # Get the var
            var = abs(lit)
            # if lit is positive then the var must be positive
            is_pos = (lit>0) 

            # If var is already assigned check for conflict
            if var in assignment:
                if assignment[var] != is_pos:
                    # Conflict found
                    return None 
                continue
            
            # Else assign 
            assignment[var] = is_pos
            # Updated that we have mede changes
            is_changed = True

            


# Main method uses helpers to decide the final output
def dpll_solver(clauses, assignment):

    clauses = simplify_clauses(clauses, assignment)
    if clauses is None:
        # This clause can NEVER be satisfied.
        return "UNSAT"

    clauses, assignment = unit_propagate(clauses, assignment)
    if clauses is None:
        
        return "UNSAT"

    if len(clauses) == 0:
        return "SAT"


