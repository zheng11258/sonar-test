# ==============================================
# HumanEval/2
# ==============================================
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number % 1.0

# ==============================================
# HumanEval/3
# ==============================================
from typing import List
def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False

# ==============================================
# HumanEval/4
# ==============================================
def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)

# ==============================================
# HumanEval/5
# ==============================================
def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []
    result = []
    for n in numbers[:-1]:
        result.append(n)
        result.append(delimiter)
    result.append(numbers[-1])
    return result

# ==============================================
# HumanEval/6
# ==============================================
def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def parse_paren_group(s):
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(depth, max_depth)
            else:
                depth -= 1
        return max_depth
    return [parse_paren_group(x) for x in paren_string.split(' ') if x]

# ==============================================
# HumanEval/7
# ==============================================
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [x for x in strings if substring in x]

# ==============================================
# HumanEval/8
# ==============================================
from typing import Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    sum_value = 0
    prod_value = 1
    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value

# ==============================================
# HumanEval/9
# ==============================================
def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    running_max = None
    result = []
    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)
        result.append(running_max)
    return result

# ===================== 全部自动测试（单独打印每题结果） =====================
if __name__ == "__main__":
    print("\n" + "="*50)
    print("📌 开始测试 HumanEval/2")
    print("示例1:", truncate_number(3.5))
    test_cases = [(3.5, 0.5), (1.33, 0.33), (123.456, 0.456)]
    for num, expected in test_cases:
        res = truncate_number(num)
        print(f"输入={num}, 结果={res:.6f}, 预期={expected}, ✅ 通过" if abs(res-expected)<1e-6 else f"输入={num}, 结果={res:.6f}, 预期={expected}, ❌ 失败")

    print("\n" + "="*50)
    print("📌 开始测试 HumanEval/3")
    print("示例1:", below_zero([1, 2, 3]))
    print("示例2:", below_zero([1, 2, -4, 5]))
    test_cases = [([], False), ([1,2,-4,5], True)]
    for i, (ops, expected) in enumerate(test_cases):
        res = below_zero(ops)
        print(f"测试{i+1}: 输入={ops}, 结果={res}, 预期={expected}, ✅ 通过" if res==expected else " ❌ 失败")

    print("\n" + "="*50)
    print("📌 开始测试 HumanEval/4")
    print("示例1:", mean_absolute_deviation([1.0,2.0,3.0,4.0]))
    test_cases = [([1.0,2.0,3.0], 2/3), ([1.0,2.0,3.0,4.0], 1.0)]
    for nums, expected in test_cases:
        res = mean_absolute_deviation(nums)
        print(f"输入={nums}, 结果={res:.6f}, 预期={expected:.6f}, ✅ 通过" if abs(res-expected)<1e-6 else " ❌ 失败")

    print("\n" + "="*50)
    print("📌 开始测试 HumanEval/5")
    print("示例1:", intersperse([], 4))
    print("示例2:", intersperse([1,2,3], 4))
    test_cases = [([],7,[]), ([5,6,3,2],8,[5,8,6,8,3,8,2])]
    for nums, d, expected in test_cases:
        res = intersperse(nums, d)
        print(f"输入={nums}, 分隔符={d}, 结果={res}, 预期={expected}, ✅ 通过" if res==expected else " ❌ 失败")

    print("\n" + "="*50)
    print("📌 开始测试 HumanEval/6")
    print("示例1:", parse_nested_parens('(()()) ((())) () ((())()())'))
    test_cases = [('(()()) ((())) () ((())()())', [2,3,1,3]), ('() (()) ((())) (((())))', [1,2,3,4])]
    for s, expected in test_cases:
        res = parse_nested_parens(s)
        print(f"输入={s}, 结果={res}, 预期={expected}, ✅ 通过" if res==expected else " ❌ 失败")

    print("\n" + "="*50)
    print("📌 开始测试 HumanEval/7")
    print("示例1:", filter_by_substring([], 'a'))
    print("示例2:", filter_by_substring(['abc','bacd','cde','array'], 'a'))
    test_cases = [([], 'john', []), (['xxx','asd','john doe'], 'xxx', ['xxx'])]
    for strs, sub, expected in test_cases:
        res = filter_by_substring(strs, sub)
        print(f"子串={sub}, 结果={res}, 预期={expected}, ✅ 通过" if res==expected else " ❌ 失败")

    print("\n" + "="*50)
    print("📌 开始测试 HumanEval/8")
    print("示例1:", sum_product([]))
    print("示例2:", sum_product([1,2,3,4]))
    test_cases = [([], (0,1)), ([1,1,1], (3,1)), ([10], (10,10))]
    for nums, expected in test_cases:
        res = sum_product(nums)
        print(f"输入={nums}, 结果={res}, 预期={expected}, ✅ 通过" if res==expected else " ❌ 失败")

    print("\n" + "="*50)
    print("📌 开始测试 HumanEval/9")
    print("示例1:", rolling_max([1,2,3,2,3,4,2]))
    test_cases = [([], []), ([4,3,2,1], [4,4,4,4]), ([3,2,3,100,3], [3,3,3,100,100])]
    for nums, expected in test_cases:
        res = rolling_max(nums)
        print(f"输入={nums}, 结果={res}, 预期={expected}, ✅ 通过" if res==expected else " ❌ 失败")

    print("\n" + "="*50)
    print("🎉 所有题目运行完成！")
