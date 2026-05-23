from abc import ABC, abstractmethod


class BaseSolver(ABC):
    """
    BaseSolver bütün DP problemləri üçün ümumi baza class-dır.

    Hər problem bu class-dan miras alacaq və 3 əsas metodu yazacaq:
    1. solve_memoization()
    2. solve_tabulation()
    3. solve_optimized()
    """

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def solve_memoization(self):
        pass

    @abstractmethod
    def solve_tabulation(self):
        pass

    @abstractmethod
    def solve_optimized(self):
        pass

    def run_all(self):
        """
        Bu metod eyni problem üçün bütün yanaşmaları işlədir.
        """
        print(f"\nProblem: {self.name}")
        print("-" * 40)

        memo_result = self.solve_memoization()
        tab_result = self.solve_tabulation()
        opt_result = self.solve_optimized()

        print(f"Memoization result: {memo_result}")
        print(f"Tabulation result: {tab_result}")
        print(f"Optimized result: {opt_result}")

        return {
            "problem": self.name,
            "memoization": memo_result,
            "tabulation": tab_result,
            "optimized": opt_result
        }