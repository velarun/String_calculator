import re


def Add(nums: str) -> int:
    # Check is empty or any
    if not nums:
        return 0

    # Convert string to list of nums and sum it
    num_list = re.split(",", nums)
    num_list = [int(num) for num in num_list]

    # Checking negative nums
    negatives = [num for num in num_list if num < 0]
    if negatives:
        raise ValueError(
            f"negatives not allowed: {', '.join(map(str, negatives))}")

    return sum(num_list)
