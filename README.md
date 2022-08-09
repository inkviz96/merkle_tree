## Description
Merkle Tree is like binary tree but with hashes

## Example
```python
from merkle_tree import MerkleTree

mt = MerkleTree()
mt.create_tree([['some', 'values'], ['for', 'test']])
print(mt.root)
>>> ['a93a498300691c5b78773a945caf26706c5b6268176c3ad49c892d3e5219f1c6']
```

If you have not 2^n values script duplicate last value and create a pare