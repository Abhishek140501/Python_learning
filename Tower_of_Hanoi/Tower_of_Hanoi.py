NUMBER_OF_DISKS = 5

# Rods represented as lists
A = list(range(NUMBER_OF_DISKS, 0, -1))  # Source rod (largest disk at index 0)
B = []  # Auxiliary rod
C = []  # Target rod

def move(n, source, auxiliary, target):
    if n <= 0:
        return

    # Step 1: Move n-1 disks from source to auxiliary
    move(n - 1, source, target, auxiliary)

    # Step 2: Move the nth disk from source to target
    target.append(source.pop())

    # Step 3: Print the current state of rods
    print(f"A: {A}")
    print(f"B: {B}")
    print(f"C: {C}")
    print("---------------")

    # Step 4: Move n-1 disks from auxiliary to target
    move(n - 1, auxiliary, source, target)

# Start solving from A to C using B
move(NUMBER_OF_DISKS, A, B, C)
