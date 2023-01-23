from Models.Clause import Clause
from Models.KNF_Formel import Formula
from Models.Literal import Literal
import random


def WalkSAT(formula: Formula, max_flips: int, p: float) -> bool:
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

        # with probability p, flip the value of a random variable in the clause
        # otherwise, flip the value of the variable that maximizes the number of satisfied clauses
        if random.random() < p:
            random_variable = random.choice(random_clause.lst)
            current_assignment[random_variable.name] = not random_variable.value
            print(f'Flipped variable: {random_variable.name}')
        else:
            best_variable = None
            best_count = -1
            for variable in random_clause.lst:
                temp_assignment = current_assignment.copy()
                temp_assignment[variable.name] = not variable.value
                count = len(
                    [c for c in formula.lst if any(temp_assignment.get(lit.name) == lit.value for lit in c.lst)])
                if count > best_count:
                    best_variable = variable
                    best_count = count
            current_assignment[best_variable.name] = not best_variable.value
            print(f'Flipped variable: {best_variable.name}')
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

print(WalkSAT(f, 10, 0.5))
