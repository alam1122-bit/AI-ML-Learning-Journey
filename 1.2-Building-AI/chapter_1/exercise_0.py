# =====================================================================
# 📚 Building AI - Exercise 0: Introduction to Exercises (Section - 01)
# Course: Building AI (University of Helsinki)
# Tracks: Beginner, Intermediate, & Advanced
# =====================================================================


# ---------------------------------------------------------------------
# 🔹 1. Beginner Track: Platform Workflow & Conceptual Setup
# ---------------------------------------------------------------------
"""
- Objective: Understand the platform submission workflow and environment setup.
- Concept: Verified environment pathways, Python execution flow, and input/output handling.
- Outcome: Successfully calibrated execution parameters for automated grading.
"""


# ---------------------------------------------------------------------
# 🔹 2. Intermediate Track: Python Functions and Execution Flow
# ---------------------------------------------------------------------
"""
- Objective: Manage function definitions, variable scope, and execution order in Python.
"""

def greet(name):
    # Print a welcome message concatenated with the passed name parameter
    print("Welcome " + name + "!")

def main():
    # Variable definition passed to function
    name = "to Building AI"
    greet(name)

# Run the main function
if __name__ == "__main__":
    print("--- Intermediate Track Output ---")
    main()


# ---------------------------------------------------------------------
# 🔹 3. Advanced Track: Recursive Factorial Function
# ---------------------------------------------------------------------
"""
- Objective: Implement a recursive algorithm to calculate the factorial of a number (n!).
- Mathematical Basis: 
    - Base Cases: 0! = 1, 1! = 1
    - Edge Case: Negative integers are invalid for standard factorials.
    - Recursive Step: n! = n * (n - 1)!
- Application: Sets up the mathematical foundation for permutation-based search space 
  calculations (e.g., Traveling Salesperson Problem / TSP).
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return "Give a positive integer"
    else:
        return n * factorial(n - 1)  # Recursive call

# Test Execution
if __name__ == "__main__":
    print("\n--- Advanced Track Output ---")
    test_number = 6
    result = factorial(test_number)
    print(f"Factorial of {test_number} ({test_number}!): {result}")  # Expected Output: 720
