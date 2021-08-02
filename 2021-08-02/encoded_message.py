import random


def coder(query: str) -> str:
    """encode alphabetic strings based on their place value factors.

    Args:
        query (str): The string to encode.

    Returns:
        str: The encoded result.
    """
    alpha = "abcdefghijklmnopqrstuvwxyz"
    result = []

    for i in query.lower():
        factors = []
        place = alpha.index(i) + 1
        for j in range(1, place + 1):
            if place % j == 0:
                factors.append((j, place // j))
        values = random.choice(factors)
        result.append(f"{alpha[values[0]-1]}{values[1]}")

    return "".join(result)


if __name__ == "__main__":
    encoded = coder("QUADRANT")
    print(encoded.upper())
