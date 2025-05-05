
# recursion.py
# This file contains three recursive functions for:
# 1. Fibonacci sequence
# 2. Euclid's GCD algorithm
# 3. String comparison

# ------------------------------
# Part I - Fibonacci Sequence
# ------------------------------

def fibonacci(n):
    """
    Recursive function to calculate the nth Fibonacci number.
    The Fibonacci sequence is: 0, 1, 1, 2, 3, 5, 8, ...
    Each number is the sum of the two before it.
    """
    if n <= 0:
        return 0  # Base case: F(0) = 0
    elif n == 1:
        return 1  # Base case: F(1) = 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # Recursive step


# ------------------------------
# Part II - Euclid's GCD
# ------------------------------

def gcd(a, b):
    """
    Recursive function to find the Greatest Common Divisor (GCD) of two numbers using Euclid's Algorithm.
    The GCD is the largest number that divides both a and b with no remainder.
    """
    if b == 0:
        return a  # Base case: If b is 0, then GCD is a
    else:
        return gcd(b, a % b)  # Recursive step: gcd(a, b) = gcd(b, a % b)


# ------------------------------
# Part III - Recursive String Comparison
# ------------------------------

def compareTo(s1, s2):
    """
    Recursive function to compare two strings lexicographically.
    Returns:
    - negative number if s1 < s2
    - 0 if s1 == s2
    - positive number if s1 > s2
    """
    # Base case: if both strings are empty, they are equal
    if s1 == "" and s2 == "":
        return 0
    # If first characters are different, compare them
    if s1 == "":
        return -1  # s1 is shorter
    if s2 == "":
        return 1   # s2 is shorter

    if s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])  # Compare ASCII values of first characters

    # If first characters are same, compare rest of the string
    return compareTo(s1[1:], s2[1:])
