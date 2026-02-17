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
                    return None, assignment
                # Already satisfied; simplify to remove this clause and continue propagation
                clauses = simplify_clauses(clauses, assignment)
                if clauses is None:
                    return None, assignment
                is_changed = True
                break

            # Else assign and simplify
            assignment[var] = is_pos
            is_changed = True
            clauses = simplify_clauses(clauses, assignment)
            if clauses is None:
                return None, assignment
            break
    return clauses, assignment


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

    # Pick an unassigned variable (first one appearing in clauses)
    branch_var = None
    for clause in clauses:
        for lit in clause:
            v = abs(lit)
            if v not in assignment:
                branch_var = v
                break
        if branch_var is not None:
            break

    if branch_var is None:
        return "UNSAT"

    # Branch: try True, then False (each branch gets a copy of assignment)
    assignment_true = assignment.copy()
    assignment_true[branch_var] = True
    if dpll_solver(clauses, assignment_true) == "SAT":
        return "SAT"

    assignment_false = assignment.copy()
    assignment_false[branch_var] = False
    return dpll_solver(clauses, assignment_false)

