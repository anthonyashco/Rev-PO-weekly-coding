import random


def coder(query: str) -> str:
    """encode alphabetic strings based on their place value factors.

    Encoding is non-deterministic and can produce a variety of outputs.

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
        length = len(factors)
        # prefer 1 if prime
        if length <= 2:
            values = factors[length - 1]
        # avoid factors of 1 if not prime
        elif length == 3:
            values = factors[1]
        else:
            factors.pop(length - 1)
            factors.pop(0)
            values = random.choice(factors)
        result.append(f"{alpha[values[0]-1]}{values[1]}")

    return "".join(result)


if __name__ == "__main__":
    encoded = coder("QUADRANT")
    print(encoded.upper())
