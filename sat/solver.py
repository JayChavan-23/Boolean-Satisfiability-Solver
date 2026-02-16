# Contains main logic for the DPLL algorithm

# Helper function
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


