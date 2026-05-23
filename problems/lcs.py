from functools import lru_cache
from framework.base_solver import BaseSolver


class LCSSolver(BaseSolver):
    """
    LCS - Longest Common Subsequence problemi.

    Məqsəd:
    İki sətir arasında ən uzun ortaq alt ardıcıllığın uzunluğunu tapmaq.
    """

    def __init__(self, text1, text2):
        super().__init__("Longest Common Subsequence")
        self.text1 = text1
        self.text2 = text2
        self.n = len(text1)
        self.m = len(text2)

    def solve_memoization(self):
        """
        Memoization yanaşması:
        Recursive funksiya ilə alt problemlər həll olunur.
        Əvvəl hesablanmış nəticələr cache-də saxlanılır.
        """

        @lru_cache(None)
        def dp(i, j):
            # Əgər sətirlərdən birinin sonuna çatmışıqsa,
            # artıq ortaq ardıcıllıq qalmır.
            if i == self.n or j == self.m:
                return 0

            # Əgər cari simvollar eynidirsə,
            # bu simvol LCS-ə daxil edilir.
            if self.text1[i] == self.text2[j]:
                return 1 + dp(i + 1, j + 1)

            # Əgər simvollar fərqlidirsə,
            # iki seçim var:
            # 1. text1-də növbəti simvola keçmək
            # 2. text2-də növbəti simvola keçmək
            return max(dp(i + 1, j), dp(i, j + 1))

        return dp(0, 0)

    def solve_tabulation(self):
        """
        Tabulation yanaşması:
        2D DP cədvəli qurulur.

        dp[i][j] =
        text1-in ilk i simvolu və text2-nin ilk j simvolu üçün
        LCS uzunluğu.
        """

        dp = [[0 for _ in range(self.m + 1)] for _ in range(self.n + 1)]

        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                # Əgər simvollar eynidirsə,
                # əvvəlki diaqonal nəticənin üzərinə 1 gəlirik.
                if self.text1[i - 1] == self.text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]

                # Əgər simvollar fərqlidirsə,
                # yuxarı və soldakı nəticənin maksimumunu götürürük.
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[self.n][self.m]

    def solve_optimized(self):
        """
        Space optimized yanaşma:
        Tam 2D cədvəl saxlamaq əvəzinə yalnız 2 sətir saxlanılır.

        Adi tabulation yaddaşı:
        O(n * m)

        Optimallaşdırılmış yaddaş:
        O(m)
        """

        previous = [0 for _ in range(self.m + 1)]
        current = [0 for _ in range(self.m + 1)]

        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                if self.text1[i - 1] == self.text2[j - 1]:
                    current[j] = 1 + previous[j - 1]
                else:
                    current[j] = max(previous[j], current[j - 1])

            # Cari sətir növbəti addım üçün previous olur.
            previous = current
            current = [0 for _ in range(self.m + 1)]

        return previous[self.m]