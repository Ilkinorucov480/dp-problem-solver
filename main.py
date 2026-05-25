from problems.knapsack import KnapsackSolver
from problems.lcs import LCSSolver
from problems.lis import LISSolver
from problems.edit_distance import EditDistanceSolver
from problems.matrix_chain import MatrixChainSolver
from framework.benchmark import Benchmark


def run_knapsack():
    solver = KnapsackSolver(
        weights=[10, 20, 30],
        values=[60, 100, 120],
        capacity=50
    )
    return solver.run_all()


def run_lcs():
    solver = LCSSolver(
        text1="ABCBDAB",
        text2="BDCABA"
    )
    return solver.run_all()


def run_lis():
    solver = LISSolver(
        nums=[10, 9, 2, 5, 3, 7, 101, 18]
    )
    return solver.run_all()


def run_edit_distance():
    solver = EditDistanceSolver(
        word1="horse",
        word2="ros"
    )
    return solver.run_all()


def run_matrix_chain():
    solver = MatrixChainSolver(
        dimensions=[10, 30, 5, 60]
    )
    return solver.run_all()


def run_all_benchmarks():
    all_results = []

    all_results.append(run_knapsack())
    all_results.append(run_lcs())
    all_results.append(run_lis())
    all_results.append(run_edit_distance())
    all_results.append(run_matrix_chain())

    Benchmark.save_to_csv(all_results)
    Benchmark.generate_charts()

    print("\nBenchmark results saved to results/benchmark_results.csv")
    print("Charts saved to results/charts/")


def show_menu():
    print("\nDynamic Programming Problem Solver")
    print("=" * 45)
    print("1. Run 0/1 Knapsack")
    print("2. Run Longest Common Subsequence")
    print("3. Run Longest Increasing Subsequence")
    print("4. Run Edit Distance")
    print("5. Run Matrix Chain Multiplication")
    print("6. Run All Benchmarks")
    print("0. Exit")
    print("=" * 45)


def main():
    while True:
        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            run_knapsack()

        elif choice == "2":
            run_lcs()

        elif choice == "3":
            run_lis()

        elif choice == "4":
            run_edit_distance()

        elif choice == "5":
            run_matrix_chain()

        elif choice == "6":
            run_all_benchmarks()

        elif choice == "0":
            print("Program finished.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()