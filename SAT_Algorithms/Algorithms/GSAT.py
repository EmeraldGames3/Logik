from Models.Clause import Clause
from Models.KNF_Formel import Formula
from Models.Literal import Literal
import random


def GSAT(formula: Formula, max_flips: int) -> bool:
    # base case: if the formula is empty, it's true
    if not formula.lst:
        return True
    # base case: if the formula contains an empty clause, it's false
    if Clause([]) in formula.lst:
        return False

    # initialize the current assignment with random values
    current_assignment = {lit.name: random.choice([True, False]) for clause in formula.lst for lit in clause.lst}
    print(f'Initial assignment: {current_assignment}')

    for i in range(max_flips):
        unsatisfied_clauses = [clause for clause in formula.lst if
                               not any(lit.value == current_assignment.get(lit.name) for lit in clause.lst)]
        print(f'Unsatisfied clauses: {unsatisfied_clauses}')

        # if all clauses are satisfied, return True
        if not unsatisfied_clauses:
            return True

        # pick a random unsatisfied clause
        random_clause = random.choice(unsatisfied_clauses)
        print(f'Random unsatisfied clause: {random_clause}')

        # flip the value of the variable that appears in the clause that maximizes the number of satisfied clauses
        variable_count = {lit.name: 0 for lit in random_clause.lst}
        for clause in formula.lst:
            for lit in clause.lst:
                if lit.value == current_assignment.get(lit.name):
                    variable_count[lit.name] += 1
        max_variable = max(variable_count, key=variable_count.get)
        current_assignment[max_variable] = not current_assignment[max_variable]
        print(f'Flipping {max_variable} to {current_assignment[max_variable]}')

    return False


l1 = Literal("P", True)
l2 = Literal("T", False)
l3 = Literal("X", True)
l4 = Literal("P", False)

c1 = Clause([l1, l2])
c2 = Clause([l1, l3])
c3 = Clause([l1, l4])
c4 = Clause([l1, l2, l3, l4])
c5 = Clause([l3])

f = Formula([c1, c2, c3, c4, c5])

print(GSAT(f, 10))

