from Models.Clause import Clause
from Models.Literal import Literal


class Formula:
    def __init__(self, lst: list[Clause]):
        self.lst = lst
        self.remove_duplicates()

    def remove_duplicates(self):
        self.lst = list(dict.fromkeys(self.lst))

    def add_clause(self, c):
        if type(c) == Clause:
            self.lst.append(c)
        elif type(c) == list:
            self.lst += c
        else:
            raise AttributeError

        self.remove_duplicates()

    def remove_clause(self, l):
        self.lst.remove(l)

    def __eq__(self, other):
        if not isinstance(other, Formula):
            return False

        if len(self.lst) != len(other.lst):
            return False

        for i in range(len(self.lst)):
            if self.lst[i] not in other.lst:
                return False

        return True

    def __hash__(self):
        return hash(tuple(self.lst))

    def __add__(self, other):
        return Clause(self.lst + other.lst)

    def __str__(self):
        return str(list(map(lambda x: str(x), self.lst)))

    def __repr__(self):
        return str(list(map(lambda x: str(x), self.lst)))


l1 = Literal("P", True)
l2 = Literal("T", False)
l3 = Literal("X", True)

c1 = Clause([l1])
c2 = Clause([])

c1.add_literal(l1)
c1.add_literal([l2, l3])

c2.add_literal([l1, l3])

f = Formula([c1])
f.add_clause([c2])

assert f == Formula([c1, c2])
assert f == Formula([c2, c1])
assert f != 1
assert f != "3"

f.add_clause(c1)
f.add_clause([c1, c2])

assert f == Formula([c1, c2])
assert f == Formula([c2, c1])
assert f != 1
assert f != "3"
