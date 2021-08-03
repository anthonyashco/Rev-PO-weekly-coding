# Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".
# - If the number is a multiple of 3 the output should be "Fizz".
# - If the number given is a multiple of 5, the output should be "Buzz".
# - If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
# - If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
# - The output should always be a string even if it is not a multiple of 3 or 5.


def fizzbuzz(value: int) -> str:
    """Return a fizzbuzz string or the number based on multiplicity.

    Args:
        value (int): The input integer.

    Returns:
        str: A fizzbuzz string or the number as a string.
    """
    three = value % 3 == 0
    five = value % 5 == 0
    result = []

    if three:
        result.append("Fizz")
    if five:
        result.append("Buzz")

    return "".join(result) if result else str(value)


if __name__ == "__main__":
    for i in range(21):
        print(f"{i}: {fizzbuzz(i)}")

    # Output
    # 0: FizzBuzz
    # 1: 1
    # 2: 2
    # 3: Fizz
    # 4: 4
    # 5: Buzz
    # 6: Fizz
    # 7: 7
    # 8: 8
    # 9: Fizz
    # 10: Buzz
    # 11: 11
    # 12: Fizz
    # 13: 13
    # 14: 14
    # 15: FizzBuzz
    # 16: 16
    # 17: 17
    # 18: Fizz
    # 19: 19
    # 20: Buzz
