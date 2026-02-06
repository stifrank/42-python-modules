"""
Module 02 - ex0: First exception handling.

Introduces basic try/except to validate and handle invalid input safely.
"""


def check_temperature(temp_str: str):
    """Validate a temperature value and handle conversion and range errors."""

    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None

    if temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        return None
    if temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        return None

    print(f"Temperature {temp}°C is perfect for plants!")
    return temp


def test_temperature_input():
    """Demonstrate temperature validation with valid and invalid inputs."""

    print("=== Garden Temperature Checker ===")
    print()

    tests = ["25", "abc", "100", "-50"]
    for t in tests:
        print(f"Testing temperature: {t}")
        check_temperature(t)
        print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
