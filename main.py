from problems.knapsack import KnapsackSolver
from problems.lcs import LCSSolver


def main():
    print("Dynamic Programming Problem Solver")
    print("=" * 40)

    knapsack_solver = KnapsackSolver(
        weights=[10, 20, 30],
        values=[60, 100, 120],
        capacity=50
    )
    knapsack_solver.run_all()

    lcs_solver = LCSSolver(
        text1="ABCBDAB",
        text2="BDCABA"
    )
    lcs_solver.run_all()


if __name__ == "__main__":
    main()