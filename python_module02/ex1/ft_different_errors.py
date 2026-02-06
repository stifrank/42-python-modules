"""
Module 02 - ex1: Different error types.

Demonstrates handling multiple built-in exception types using try/except.
"""


def garden_operations():
    """Trigger and catch different common Python exceptions."""

    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
        print()

    print("Testing ZeroDivisionError...")
    try:
        _ = 10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
        print()

    print("Testing FileNotFoundError...")
    try:
        open("missing.txt", "r")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
        print()

    print("Testing KeyError...")
    try:
        plants = {"tomato": 10, "lettuce": 5}
        _ = plants["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}")
        print()


def test_error_types():
    """Demonstrate individual and grouped exception handling."""

    print("=== Garden Error Types Demo ===")
    print()

    garden_operations()

    print("Testing multiple errors together...")
    try:
        int("abc")
        _ = 10 / 0
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
        print()

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
