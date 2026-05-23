from functools import lru_cache
from framework.base_solver import BaseSolver


class EditDistanceSolver(BaseSolver):
    """
    Edit Distance problemi.

    Məqsəd:
    İki söz arasında minimum çevrilmə əməliyyatlarının sayını tapmaq.

    İcazəli əməliyyatlar:
    1. Insert  - simvol əlavə etmək
    2. Delete  - simvol silmək
    3. Replace - simvol dəyişmək
    """

    def __init__(self, word1, word2):
        super().__init__("Edit Distance")
        self.word1 = word1
        self.word2 = word2
        self.n = len(word1)
        self.m = len(word2)

    def solve_memoization(self):
        """
        Memoization yanaşması:
        Recursive funksiya ilə alt problemlər həll olunur.
        Eyni vəziyyət təkrar hesablanmasın deyə nəticələr cache-də saxlanılır.
        """

        @lru_cache(None)
        def dp(i, j):
            # Əgər word1 bitibsə, qalan word2 simvollarını əlavə etməliyik
            if i == self.n:
                return self.m - j

            # Əgər word2 bitibsə, qalan word1 simvollarını silməliyik
            if j == self.m:
                return self.n - i

            # Əgər simvollar eynidirsə, əməliyyat lazım deyil
            if self.word1[i] == self.word2[j]:
                return dp(i + 1, j + 1)

            # 3 seçim:
            # Insert: word2[j] simvolunu word1-ə əlavə edirik
            insert_op = dp(i, j + 1)

            # Delete: word1[i] simvolunu silirik
            delete_op = dp(i + 1, j)

            # Replace: word1[i] simvolunu word2[j] ilə dəyişirik
            replace_op = dp(i + 1, j + 1)

            return 1 + min(insert_op, delete_op, replace_op)

        return dp(0, 0)

    def solve_tabulation(self):
        """
        Tabulation yanaşması:
        2D DP cədvəli qurulur.

        dp[i][j] =
        word1-in ilk i simvolunu word2-nin ilk j simvoluna çevirmək üçün
        lazım olan minimum əməliyyat sayı.
        """

        dp = [[0 for _ in range(self.m + 1)] for _ in range(self.n + 1)]

        # word2 boşdursa, word1-dən simvollar silinir
        for i in range(self.n + 1):
            dp[i][0] = i

        # word1 boşdursa, word2 simvolları əlavə olunur
        for j in range(self.m + 1):
            dp[0][j] = j

        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                if self.word1[i - 1] == self.word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    insert_op = dp[i][j - 1]
                    delete_op = dp[i - 1][j]
                    replace_op = dp[i - 1][j - 1]

                    dp[i][j] = 1 + min(insert_op, delete_op, replace_op)

        return dp[self.n][self.m]

    def solve_optimized(self):
        """
        Space optimized yanaşma:
        Tam 2D cədvəl əvəzinə yalnız iki sətir saxlanılır.

        Adi tabulation yaddaşı:
        O(n * m)

        Optimized yaddaş:
        O(m)
        """

        previous = [j for j in range(self.m + 1)]

        for i in range(1, self.n + 1):
            current = [0 for _ in range(self.m + 1)]
            current[0] = i

            for j in range(1, self.m + 1):
                if self.word1[i - 1] == self.word2[j - 1]:
                    current[j] = previous[j - 1]
                else:
                    insert_op = current[j - 1]
                    delete_op = previous[j]
                    replace_op = previous[j - 1]

                    current[j] = 1 + min(insert_op, delete_op, replace_op)

            previous = current

        return previous[self.m]