from Models.Clause import Clause
from Models.KNF_Formel import Formula
from Models.Literal import Literal


def DPLL(formula: Formula) -> bool:
    # base case: if the formula is empty, it's true
    if not formula.lst:
        return True
    # base case: if the formula contains an empty clause, it's false
    if Clause([]) in formula.lst:
        return False

    if any(len(c.lst) == 1 for c in formula.lst):
        for clause in formula.lst:
            # if the clause is a unit clause, assign its literal
            if len(clause.lst) == 1:
                temp_lit = clause.lst[0]
                formula.remove_clause(clause)
                for c in formula.lst:
                    for lit in c.lst:
                        if lit == Literal(temp_lit.name, not temp_lit.value):
                            c.remove_literal(lit)

        return DPLL(formula)
    else:
        # This happens if there are no unit-clauses
        def assign_literal(fa, name, value):
            for cl in fa.lst:
                for l in cl.lst:
                    if l.name == name:
                        if l.value == value:
                            fa.remove_clause(cl)
                        else:
                            cl.remove_literal(l)
            return fa

        # if there are no unit clauses, pick a variable that appears in the most clauses
        variable_count = {}
        for c in formula.lst:
            for lit in c.lst:
                variable_count[lit.name] = variable_count.get(lit.name, 0) + 1

        most_common_variable = max(variable_count, key=variable_count.get)

        # Assign the most common variable to be true
        formula_1 = assign_literal(formula, most_common_variable, True)
        # Assign the most common variable to be false
        formula_2 = assign_literal(formula, most_common_variable, False)

        # Return the logical OR of the results
        return DPLL(formula_1) or DPLL(formula_2)


assert not DPLL(Formula([Clause([])]))
assert DPLL(Formula([]))

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

# print(Clause([Literal(f.lst[0].lst[0].name, True)]), Clause([Literal(f.lst[0].lst[0].name, False)]))

print(DPLL(f))

false_formula = Formula([Clause([]), Clause([Literal("A", True), Literal("B", True)]), Clause([Literal("C", False)])])

print(DPLL(false_formula))
