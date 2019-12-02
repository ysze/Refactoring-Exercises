class HashTable:
    def __init__(self):
        self.table = [[] for _ in range(10000)]

    def store(self, s: str) -> None:
        self.table[self._hash(s)].append(s)

    def lookup(self, s: str) -> int:
        return self._hash(s) if s in self.table[self._hash(s)] else -1

    @staticmethod
    def _hash(s: str) -> int:
        return 100 * ord(s[0]) + ord(s[1])
