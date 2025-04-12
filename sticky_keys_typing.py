def isLongPressed(original: str, typed: str) -> bool:
    """
    Determines if the typed string could have been formed from the original 
    string by potentially pressing keys longer (sticky keys).

    Args:
        original: The intended string.
        typed: The string actually typed, potentially with long presses.

    Returns:
        True if typed could be formed from original, False otherwise.
    """
    i = 0  # Pointer for original string
    j = 0  # Pointer for typed string

    while j < len(typed):
        # If characters match, advance both pointers
        if i < len(original) and original[i] == typed[j]:
            i += 1
            j += 1
        # If characters don't match, check if it's a long press 
        # of the *previous* character in the typed string.
        # Note: We check typed[j-1] because the long press must be 
        # of the character that was just matched from 'original'.
        elif j > 0 and typed[j] == typed[j-1]:
            j += 1
        # If characters don't match and it's not a long press, it's invalid
        else:
            return False

    # After iterating through the typed string, check if all characters
    # in the original string were consumed.
    return i == len(original)

# Example Usage:
print(f'isLongPressed("alex", "aaleex") -> {isLongPressed("alex", "aaleex")}')
print(f'isLongPressed("saeed", "ssaaedd") -> {isLongPressed("saeed", "ssaaedd")}')
print(f'isLongPressed("leelee", "lleeelee") -> {isLongPressed("leelee", "lleeelee")}')
print(f'isLongPressed("Tokyo", "TTokkyoh") -> {isLongPressed("Tokyo", "TTokkyoh")}')
print(f'isLongPressed("laiden", "laiden") -> {isLongPressed("laiden", "laiden")}')
print(f'isLongPressed("pyplrz", "ppyypllr") -> {isLongPressed("pyplrz", "ppyypllr")}') 
print(f'isLongPressed("alex", "aaleexa") -> {isLongPressed("alex", "aaleexa")}')
print(f'isLongPressed("a", "aaaa") -> {isLongPressed("a", "aaaa")}')
print(f'isLongPressed("aaaa", "a") -> {isLongPressed("aaaa", "a")}')


from itertools import groupby

def group_string(s: str) -> list[tuple[str, int]]:
    """Helper function to group consecutive identical characters and their counts."""
    return [(char, len(list(group))) for char, group in groupby(s)]

def isLongPressed(original: str, typed: str) -> bool:
    """
    Determines if the typed string could have been formed from the original 
    string using sticky keys, implemented using itertools.groupby.

    Args:
        original: The intended string.
        typed: The string actually typed, potentially with long presses.

    Returns:
        True if typed could be formed from original, False otherwise.
    """
    grouped_original = group_string(original)
    grouped_typed = group_string(typed)

    # 1. Check if the number of character groups is the same.
    #    If "alex" has groups ('a', 'l', 'e', 'x') and typed has ('a', 'l', 'x'),
    #    they can't match.
    if len(grouped_original) != len(grouped_typed):
        return False

    # 2. Iterate through the groups of both strings simultaneously.
    for (o_char, o_count), (t_char, t_count) in zip(grouped_original, grouped_typed):
        # 2a. The character in each corresponding group must be the same.
        if o_char != t_char:
            return False
        # 2b. The count of characters in the typed group must be
        #     at least the count in the original group (it can be more due to long press).
        if t_count < o_count:
            return False

    # If all groups match according to the rules, return True.
    return True

# Example Usage:
print(f'isLongPressed("alex", "aaleex") -> {isLongPressed("alex", "aaleex")}')
print(f'isLongPressed("saeed", "ssaaedd") -> {isLongPressed("saeed", "ssaaedd")}')
print(f'isLongPressed("leelee", "lleeelee") -> {isLongPressed("leelee", "lleeelee")}')
print(f'isLongPressed("Tokyo", "TTokkyoh") -> {isLongPressed("Tokyo", "TTokkyoh")}')
print(f'isLongPressed("laiden", "laiden") -> {isLongPressed("laiden", "laiden")}')
print(f'isLongPressed("pyplrz", "ppyypllr") -> {isLongPressed("pyplrz", "ppyypllr")}')