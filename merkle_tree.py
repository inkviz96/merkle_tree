import hashlib


class MerkleTree:
    def __init__(self):
        self.leaves: list = list()
        self.levels: list = list()
        self.root: list

    def create_leave(self, values: list) -> None:
        hash = hashlib.sha256()
        hash.update(values[0].encode('UTF-8') + values[1].encode('UTF-8'))
        self.leaves.append(hash.hexdigest())

    def create_level(self, values: list) -> None:
       self.levels.append([values[x:2+x] for x in range(0, len(values), 2)])

    def reset_leaves(self):
        self.leaves = list()

    def create_tree(self, values: list) -> None:
        [self.create_leave(x) for x in values]
        self.create_level(self.leaves)
        if len(self.levels[0][-1]) == 1 and len(self.levels[-1]) != 1:
            self.levels[0][-1].append(self.leaves[-1])
        if len(self.levels[-1][0]) == 1:
            self.root = self.levels[-1][0]
            return
        else:
            new_leaves = self.levels[-1]
            self.reset_leaves()
            self.create_tree(new_leaves)

    def get_deep(self) -> int:
        assert self.levels == 0, "Before create tree"
        return len(self.levels)
