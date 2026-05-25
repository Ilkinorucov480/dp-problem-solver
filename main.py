from problems.knapsack import KnapsackSolver
from problems.lcs import LCSSolver
from problems.lis import LISSolver
from problems.edit_distance import EditDistanceSolver
from problems.matrix_chain import MatrixChainSolver
from framework.benchmark import Benchmark


def main():
    print("Dynamic Programming Problem Solver")
    print("=" * 40)

    all_results = []

    knapsack_solver = KnapsackSolver(
        weights=[10, 20, 30],
        values=[60, 100, 120],
        capacity=50
    )
    all_results.append(knapsack_solver.run_all())

    lcs_solver = LCSSolver(
        text1="ABCBDAB",
        text2="BDCABA"
    )
    all_results.append(lcs_solver.run_all())

    lis_solver = LISSolver(
        nums=[10, 9, 2, 5, 3, 7, 101, 18]
    )
    all_results.append(lis_solver.run_all())

    edit_distance_solver = EditDistanceSolver(
        word1="horse",
        word2="ros"
    )
    all_results.append(edit_distance_solver.run_all())

    matrix_chain_solver = MatrixChainSolver(
        dimensions=[10, 30, 5, 60]
    )
    all_results.append(matrix_chain_solver.run_all())

    Benchmark.save_to_csv(all_results)
    Benchmark.generate_charts()

    print("\nBenchmark results saved to results/benchmark_results.csv")
    print("Charts saved to results/charts/")


if __name__ == "__main__":
    main()