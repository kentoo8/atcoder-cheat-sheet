def count_subarrays(nums: list[int], target_val: int) -> int:
    """和がちょうど target_val である連続部分列の個数を返す。

    nums は非負整数列を想定する。
    """

    if target_val < 0:
        return 0

    if target_val == 0:
        ans = 0
        zero_run = 0

        for x in nums:
            if x == 0:
                zero_run += 1
                ans += zero_run
            else:
                zero_run = 0

        return ans

    ans = 0

    left_target = 0
    left_smaller = 0

    sum_target = 0
    sum_smaller = 0

    for right in range(len(nums)):
        x = nums[right]

        sum_target += x
        sum_smaller += x

        # 和を target_val 以下にする最小の左端
        while sum_target > target_val:
            sum_target -= nums[left_target]
            left_target += 1

        # 和を target_val - 1 以下にする最小の左端
        while sum_smaller >= target_val:
            sum_smaller -= nums[left_smaller]
            left_smaller += 1

        # right を右端として、
        # 和がちょうど target_val になる左端の個数
        ans += left_smaller - left_target

    return ans
