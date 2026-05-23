from functools import lru_cache
from framework.base_solver import BaseSolver


class KnapsackSolver(BaseSolver):
    """
    0/1 Knapsack problemi.

    Verilir:
    - weights: əşyaların çəkiləri
    - values: əşyaların dəyərləri
    - capacity: çantanın maksimum tutumu

    Məqsəd:
    Çantanın tutumunu aşmadan maksimum dəyər əldə etmək.
    """

    def __init__(self, weights, values, capacity):
        super().__init__("0/1 Knapsack")
        self.weights = weights
        self.values = values
        self.capacity = capacity
        self.n = len(weights)

    def solve_memoization(self):
        """
        Memoization yanaşması:
        Recursive funksiya istifadə olunur və əvvəl hesablanmış nəticələr cache-də saxlanılır.
        """

        @lru_cache(None)
        def dp(index, remaining_capacity):
            # Əgər bütün əşyalar yoxlanılıbsa və ya tutum qalmayıbsa
            if index == self.n or remaining_capacity == 0:
                return 0

            # Əgər cari əşya çantaya sığmırsa, onu götürmürük
            if self.weights[index] > remaining_capacity:
                return dp(index + 1, remaining_capacity)

            # İki seçim var:
            # 1. Əşyanı götürməmək
            not_take = dp(index + 1, remaining_capacity)

            # 2. Əşyanı götürmək
            take = self.values[index] + dp(
                index + 1,
                remaining_capacity - self.weights[index]
            )

            return max(take, not_take)

        return dp(0, self.capacity)

    def solve_tabulation(self):
        """
        Tabulation yanaşması:
        2D cədvəl qurulur.
        dp[i][w] = ilk i əşya ilə w tutumunda maksimum dəyər.
        """

        dp = [[0 for _ in range(self.capacity + 1)] for _ in range(self.n + 1)]

        for i in range(1, self.n + 1):
            current_weight = self.weights[i - 1]
            current_value = self.values[i - 1]

            for w in range(self.capacity + 1):
                # Əşyanı götürmədən əvvəlki nəticə
                dp[i][w] = dp[i - 1][w]

                # Əgər əşya çantaya sığırsa, götürmək variantını yoxlayırıq
                if current_weight <= w:
                    dp[i][w] = max(
                        dp[i][w],
                        current_value + dp[i - 1][w - current_weight]
                    )

        return dp[self.n][self.capacity]

    def solve_optimized(self):
        """
        Space optimized yanaşma:
        2D cədvəl əvəzinə 1D massiv istifadə olunur.

        Əvvəlki yanaşmada yaddaş:
        O(n * capacity)

        Optimallaşdırılmış yanaşmada yaddaş:
        O(capacity)
        """

        dp = [0 for _ in range(self.capacity + 1)]

        for i in range(self.n):
            current_weight = self.weights[i]
            current_value = self.values[i]

            # Geriyə doğru gedirik ki, eyni əşya bir neçə dəfə seçilməsin
            for w in range(self.capacity, current_weight - 1, -1):
                dp[w] = max(dp[w], current_value + dp[w - current_weight])

        return dp[self.capacity]