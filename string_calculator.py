import re


def Add(nums: str) -> int:
    # Check is empty or any
    if not nums:
        return 0

    # Convert string to list of nums and sum it
    num_list = re.split(",", nums)
    num_list = [int(num) for num in num_list]

    return sum(num_list)
