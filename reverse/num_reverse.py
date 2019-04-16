def solution(num_list):
    """
    Complete the function such that:

    Given a list of digits LD, reverse all the digits in LD to a new list LR.
    Return the LR and largest element in LR in a tuple such that:

        - [123] -> ([321], 321)
        - [-789, 10] -> ([-987, 1], 1)
        - [11020, 3512] -> ([2011, 2153], 2153)

    Constraints:
    Eliminate leading zeros.
    Note the position of the negative operator after the reversal.

    """
    reversed_list = []
    for i in num_list:
        num = str(i)[::-1].strip('0')
        if num.endswith('-'):
            num = int(num.strip('-')) * -1

        reversed_list.append(int(num))

    return (reversed_list, max(reversed_list))


print(solution([123]))