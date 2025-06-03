# Square Root Approximation using Bisection Method

This Python function approximates the square root of a non-negative number using the **bisection method**. It is particularly useful for cases where you want a simple, iterative numerical solution without relying on built-in math functions.

## Function Overview

```python
def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
Parameters
square_target (float or int):
The number for which to compute the square root. Must be non-negative.

tolerance (float, optional):
The acceptable error margin between the square of the estimated root and the original number. Default is 1e-7.

max_iterations (int, optional):
The maximum number of iterations allowed for the bisection algorithm. Default is 100.

Returns
An approximate square root of the input number (float).

If convergence fails within the specified iterations, it prints an error message and returns None.

Exceptions
Raises ValueError if square_target is negative.

Example Usage

N = 16
square_root_bisection(N)

Output:
The square root of 16 is approximately 4.0

How It Works
Handles edge cases for 0 and 1 directly.

Uses the bisection method to iteratively narrow the range where the square root lies.

Stops if the result is within the given tolerance or if the maximum number of iterations is reached.

Notes
This is a simple implementation for educational or small-scale use.

For more accurate or performance-sensitive applications, consider using Python’s math.sqrt() or cmath for complex numbers.

Author
Abhishek Anand