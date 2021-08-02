def lcs(string1: str, string2: str) -> str:
    """Compare two strings and return the longest common substring.

    Args:
        string1, string2 (str): The strings for comparison.

    Returns:
        str: The longest common substring.
    """
    cache = set()
    matching = set()
    small = string1.lower() if len(string1) <= len(string2) else string2.lower()
    large = string2.lower() if small == string1 else string1.lower()
    n = len(small)

    for i in range(n):
        for j in range(n - i):
            sub = small[i:n - j]
            if sub not in cache:
                cache.add(sub)
                if small[i:n - j] in large:
                    matching.add(sub)

    return max(matching, key=len)


if __name__ == "__main__":
    longest_common_sequence = lcs("Minneapolis", "Minnesota")
    print(longest_common_sequence)
