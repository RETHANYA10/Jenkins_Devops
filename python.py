#!/usr/bin/env python3
"""
LCM Calculator - Calculates the Least Common Multiple of two integers.
Handles zero and negative numbers safely.
"""

import sys
import math

def gcd(a: int, b: int) -> int:
    """Compute the Greatest Common Divisor using Euclidean algorithm."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

def lcm(a: int, b: int) -> int:
    """Compute the Least Common Multiple."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

def main():
    # Ensure correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: python lcm.py <num1> <num2>")
        sys.exit(1)

    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    except ValueError:
        print("Error: Both arguments must be integers.")
        sys.exit(1)

    result = lcm(num1, num2)
    print(f"LCM of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()

