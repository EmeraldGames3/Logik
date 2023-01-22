from Models.Literal import Literal


class Clause:
    def __init__(self, lst: list[Literal]):
        self.lst = lst
        self.remove_duplicates()

    def remove_duplicates(self):
        self.lst = list(dict.fromkeys(self.lst))

    def add_literal(self, l):
        if type(l) == Literal:
            self.lst.append(l)
        elif type(l) == list:
            self.lst += l
        else:
            raise AttributeError

        self.remove_duplicates()

    def remove_literal(self, l):
        for i in range(len(self.lst)):
            if self.lst[i] == l:
                self.lst.pop(i)

    def __hash__(self):
        return hash(tuple(self.lst))

    def __eq__(self, other):
        if not isinstance(other, Clause):
            return False

        if len(self.lst) != len(other.lst):
            return False

        for i in range(len(self.lst)):
            if self.lst[i] not in other.lst:
                return False

        return True

    def __add__(self, other):
        return Clause(self.lst + other.lst)

    def __str__(self):
        return str(list(map(lambda x: str(x), self.lst)))

    def __repr__(self):
        return str(list(map(lambda x: str(x), self.lst)))


l1 = Literal("P", True)
l2 = Literal("T", False)
l3 = Literal("X", True)

c = Clause([])

c.add_literal(l1)
c.add_literal([l2, l3])

assert c == Clause([l3, l2, l1])
assert c == Clause([l1, l2, l3])
assert c != 1
assert c != "2"

c.add_literal([l1, l2, l3])

assert c == Clause([l3, l2, l1])
assert c == Clause([l1, l2, l3])
assert c != 1
assert c != "2"

# print(c)

# print(c)
