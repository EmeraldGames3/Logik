class Literal:
    def __init__(self, name: str, value: bool = None):
        if type(value) != bool and value is not None:
            raise AttributeError

        self.value = value
        self.name = name

    def __hash__(self):
        return hash((self.value, self.name))

    def __eq__(self, other):
        return self.name == other.name and self.value == other.value

    def __str__(self):
        return f"{self.name} with value {self.value}" if self.value is not None else self.name

    def __repr__(self):
        return f"{self.name} with value {self.value}" if self.value is not None else self.name


l1 = Literal("P", True)
l2 = Literal("T", False)
l3 = Literal("X")

assert l2 != l1
assert l1 == Literal("P", True)
assert l3 == Literal("X")

l = [l1, l2, l3]

# print(l)
