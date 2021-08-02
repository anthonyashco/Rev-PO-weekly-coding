from itertools import combinations


def longest_common_substring(string1: str, string2: str) -> str:
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


def longest_common_subsequence(string1: str, string2: str) -> str:
    """Compare two strings and return the longest common subsequence.

    Args:
        string1, string2 (str): The strings for comparison.

    Returns:
        str: The longest common subsequence.
    """

    def substringerizer(string: str) -> set():
        string = string.lower()
        cache = set()
        n = len(string)
        for i in range(1, n + 1):
            [cache.add(j) for j in combinations(string, i) if j not in cache]
        return cache

    set1 = substringerizer(string1)
    set2 = substringerizer(string2)

    matches = set1 & set2

    return "".join(sorted(matches, key=len, reverse=True)[0])


if __name__ == "__main__":
    lc_substring = longest_common_substring("Minneapolis", "Minnesota")
    print("Longest substring: " + lc_substring)

    lc_subsequence = longest_common_subsequence("Minneapolis", "Minnesota")
    print("Longest subsequence: " + lc_subsequence)
