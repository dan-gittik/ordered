# Ordered

A decorator that captures the class attributes definition order (even in Python 2!).

```python
from ordered import ordered

@ordered()
class A:
    x = 1
    y = 2
    z = 3

assert A._order == ['x', 'y', 'z']
```
