class Literal:
    def __init__(self, name: str, value: bool):
        if type(value) != bool:
            raise AttributeError

        self.value = value
        self.name = name

    def __hash__(self):
        return hash((self.value, self.name))

    def __eq__(self, other):
        return self.name == other.name and self.value == other.value

    def __str__(self):
        return f"{self.name} with value {self.value}"

    def __repr__(self):
        return f"{self.name} with value {self.value}"


l1 = Literal("P", True)
l2 = Literal("T", False)
l3 = Literal("X", True)

assert l2 != l1
assert l1 == Literal("P", True)
assert l3 == Literal("X", True)

l = [l1, l2, l3]

# print(l)
