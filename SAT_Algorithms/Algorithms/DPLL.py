from Models.Clause import Clause
from Models.KNF_Formel import Formula
from Models.Literal import Literal


def DPLL(formula: Formula) -> bool:
    if not formula.lst:
        # List is empty
        # Embrace the truth
        return True
    if Clause([]) in formula.lst:
        # Empty Clause in the Formula
        # Reject Falsity
        return False

    for c in formula.lst:
        while len(c.lst) == 1:
            temp_l = c.lst[0]

            formula.remove_clause(c)

            for c1 in formula.lst:
                for l in c1.lst:
                    if l == Literal(temp_l.name, not temp_l.value):
                        c1.remove_literal(l)

    print(formula)


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

DPLL(Formula(

))
