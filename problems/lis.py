from functools import lru_cache
from bisect import bisect_left
from framework.base_solver import BaseSolver


class LISSolver(BaseSolver):
    """
    LIS - Longest Increasing Subsequence problemi.

    Məqsəd:
    Verilmiş massivdə ən uzun artan alt ardıcıllığın uzunluğunu tapmaq.
    """

    def __init__(self, nums):
        super().__init__("Longest Increasing Subsequence")
        self.nums = nums
        self.n = len(nums)

    def solve_memoization(self):
        """
        Memoization yanaşması:
        Hər element üçün iki seçim var:
        1. Elementi götürmək
        2. Elementi götürməmək
        """

        @lru_cache(None)
        def dp(index, previous_index):
            if index == self.n:
                return 0

            not_take = dp(index + 1, previous_index)

            take = 0
            if previous_index == -1 or self.nums[index] > self.nums[previous_index]:
                take = 1 + dp(index + 1, index)

            return max(take, not_take)

        return dp(0, -1)

    def solve_tabulation(self):
        """
        Tabulation yanaşması:
        dp[i] = i-ci elementdə bitən ən uzun artan alt ardıcıllığın uzunluğu.
        """

        if self.n == 0:
            return 0

        dp = [1 for _ in range(self.n)]

        for i in range(1, self.n):
            for j in range(i):
                if self.nums[i] > self.nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def solve_optimized(self):
        """
        Optimized yanaşma:
        Binary search istifadə olunur.

        Adi DP vaxt mürəkkəbliyi: O(n^2)
        Optimized vaxt mürəkkəbliyi: O(n log n)
        """

        sub = []

        for num in self.nums:
            position = bisect_left(sub, num)

            if position == len(sub):
                sub.append(num)
            else:
                sub[position] = num

        return len(sub)