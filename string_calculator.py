import re


def Add(nums: str) -> int:
    # Check is empty or any
    if not nums:
        return 0

    delimiter = ",|\n"

    # Checking new line with comma as prefix or suffix makes expression partial
    if re.search(r",\n|\n,", nums):
        raise ValueError(f"Invalid input format: {nums}")

    # Convert string to list of string
    num_list = re.split(delimiter, nums)

    # Checking num is less than 1000
    try:
        num_list = [int(num) for num in num_list if num and int(num) <= 1000]
    except ValueError:
        raise ValueError(f"Invalid input format: {nums}")

    # Checking negative nums
    negatives = [num for num in num_list if num < 0]
    if negatives:
        raise ValueError(
            f"negatives not allowed: {', '.join(map(str, negatives))}")

    return sum(num_list)
