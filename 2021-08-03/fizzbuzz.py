def fizzbuzz(value: int) -> str:
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
