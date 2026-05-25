import time
import tracemalloc
import csv
import os


class Benchmark:
    """
    Benchmark class-ı hər DP metodunun işləmə vaxtını və yaddaş istifadəsini ölçür.
    """

    @staticmethod
    def measure(function):
        """
        Verilmiş funksiyanın:
        - nəticəsini
        - işləmə vaxtını
        - yaddaş istifadəsini ölçür.
        """

        tracemalloc.start()

        start_time = time.perf_counter()
        result = function()
        end_time = time.perf_counter()

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        execution_time = end_time - start_time
        memory_usage_kb = peak / 1024

        return {
            "result": result,
            "time": execution_time,
            "memory_kb": memory_usage_kb
        }

    @staticmethod
    def save_to_csv(results, file_path="results/benchmark_results.csv"):
        """
        Benchmark nəticələrini CSV faylına yazır.
        """

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Problem",
                "Method",
                "Result",
                "Time_Seconds",
                "Memory_KB"
            ])

            for item in results:
                problem_name = item["problem"]

                writer.writerow([
                    problem_name,
                    "Memoization",
                    item["memoization"]["result"],
                    f"{item['memoization']['time']:.6f}",
                    f"{item['memoization']['memory_kb']:.2f}"
                ])

                writer.writerow([
                    problem_name,
                    "Tabulation",
                    item["tabulation"]["result"],
                    f"{item['tabulation']['time']:.6f}",
                    f"{item['tabulation']['memory_kb']:.2f}"
                ])

                writer.writerow([
                    problem_name,
                    "Optimized",
                    item["optimized"]["result"],
                    f"{item['optimized']['time']:.6f}",
                    f"{item['optimized']['memory_kb']:.2f}"
                ])