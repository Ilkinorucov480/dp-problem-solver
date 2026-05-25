from abc import ABC, abstractmethod
from framework.benchmark import Benchmark


class BaseSolver(ABC):
    """
    BaseSolver bütün DP problemləri üçün ümumi baza class-dır.
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
        Bu metod eyni problem üçün bütün yanaşmaları benchmark ilə işlədir.
        """

        print(f"\nProblem: {self.name}")
        print("-" * 40)

        memo = Benchmark.measure(self.solve_memoization)
        tab = Benchmark.measure(self.solve_tabulation)
        opt = Benchmark.measure(self.solve_optimized)

        print(
            f"Memoization result: {memo['result']} | "
            f"Time: {memo['time']:.6f}s | "
            f"Memory: {memo['memory_kb']:.2f} KB"
        )

        print(
            f"Tabulation result: {tab['result']} | "
            f"Time: {tab['time']:.6f}s | "
            f"Memory: {tab['memory_kb']:.2f} KB"
        )

        print(
            f"Optimized result: {opt['result']} | "
            f"Time: {opt['time']:.6f}s | "
            f"Memory: {opt['memory_kb']:.2f} KB"
        )

        return {
            "problem": self.name,
            "memoization": memo,
            "tabulation": tab,
            "optimized": opt
        }