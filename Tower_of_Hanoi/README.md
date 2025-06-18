# Tower of Hanoi

This Python script solves the Tower of Hanoi problem using recursion.

## Description

The Tower of Hanoi is a mathematical puzzle where you have to move a stack of disks from one rod to another, obeying the following rules:
1. Only one disk can be moved at a time.
2. A disk can only be placed on top of a larger disk.
3. You can use one auxiliary rod.

This script recursively moves disks between three rods and prints the state of each move.

## Code

```python
NUMBER_OF_DISKS = 5
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

def move(n, source, auxiliary, target):
    if n <= 0:
        return
    move(n - 1, source, target, auxiliary)
    target.append(source.pop())
    print(A, B, C, '\n')
    move(n - 1, auxiliary, source, target)

move(NUMBER_OF_DISKS, A, B, C)


Author
Abhishek Anand 
```
