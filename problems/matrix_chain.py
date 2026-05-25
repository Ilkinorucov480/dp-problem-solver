from functools import lru_cache
from framework.base_solver import BaseSolver


class MatrixChainSolver(BaseSolver):
    """
    Matrix Chain Multiplication problemi.

    Məqsəd:
    Verilmiş matrislər zəncirini ən az vurma əməliyyatı ilə hesablamaq.

    Məsələn:
    dimensions = [10, 30, 5, 60]

    Bu o deməkdir:
    A1 = 10 x 30
    A2 = 30 x 5
    A3 = 5 x 60
    """

    def __init__(self, dimensions):
        super().__init__("Matrix Chain Multiplication")
        self.dimensions = dimensions
        self.n = len(dimensions) - 1

    def solve_memoization(self):
        """
        Memoization yanaşması:
        Recursive formada bütün mümkün bölünmə nöqtələri yoxlanılır.
        Ən az əməliyyat sayı seçilir.
        """

        @lru_cache(None)
        def dp(i, j):
            # Əgər yalnız bir matris varsa, vurma əməliyyatı yoxdur
            if i == j:
                return 0

            min_cost = float("inf")

            # k bölünmə nöqtəsidir
            for k in range(i, j):
                cost = (
                    dp(i, k)
                    + dp(k + 1, j)
                    + self.dimensions[i - 1] * self.dimensions[k] * self.dimensions[j]
                )

                min_cost = min(min_cost, cost)

            return min_cost

        return dp(1, self.n)

    def solve_tabulation(self):
        """
        Tabulation yanaşması:
        2D DP cədvəli qurulur.

        dp[i][j] =
        i-ci matrisdən j-ci matrisə qədər minimum vurma əməliyyatı sayı.
        """

        dp = [[0 for _ in range(self.n + 1)] for _ in range(self.n + 1)]

        # chain_length zəncirdə neçə matris olduğunu bildirir
        for chain_length in range(2, self.n + 1):
            for i in range(1, self.n - chain_length + 2):
                j = i + chain_length - 1
                dp[i][j] = float("inf")

                for k in range(i, j):
                    cost = (
                        dp[i][k]
                        + dp[k + 1][j]
                        + self.dimensions[i - 1] * self.dimensions[k] * self.dimensions[j]
                    )

                    dp[i][j] = min(dp[i][j], cost)

        return dp[1][self.n]

    def solve_optimized(self):
        """
        Matrix Chain Multiplication üçün klassik tam space optimization
        Knapsack və LCS kimi sadə deyil.

        Çünki burada dp[i][j] hesablanarkən müxtəlif aralıqların nəticələri lazımdır.
        Ona görə əsas optimallaşdırma kimi lazımsız əlavə struktur saxlamırıq
        və yalnız minimum cost cədvəlindən istifadə edirik.
        """

        return self.solve_tabulation()