import time
import tracemalloc
import csv
import os
import pandas as pd
import matplotlib.pyplot as plt


class Benchmark:
    """
    Benchmark class-ı DP metodlarının işləmə vaxtını, yaddaş istifadəsini ölçür,
    nəticələri CSV faylına yazır və qrafiklər yaradır.
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

    @staticmethod
    def generate_charts(
        csv_path="results/benchmark_results.csv",
        output_dir="results/charts"
    ):
        """
        CSV faylındakı benchmark nəticələrinə əsasən
        işləmə vaxtı və yaddaş istifadəsi üçün müqayisə qrafikləri yaradır.
        """

        os.makedirs(output_dir, exist_ok=True)

        data = pd.read_csv(csv_path)

        # Time_Seconds və Memory_KB sütunlarını rəqəmə çeviririk
        data["Time_Seconds"] = pd.to_numeric(data["Time_Seconds"])
        data["Memory_KB"] = pd.to_numeric(data["Memory_KB"])

        # 1. Execution Time Comparison Chart
        plt.figure(figsize=(12, 6))

        for method in data["Method"].unique():
            method_data = data[data["Method"] == method]

            plt.plot(
                method_data["Problem"],
                method_data["Time_Seconds"],
                marker="o",
                label=method
            )

        plt.title("Execution Time Comparison")
        plt.xlabel("DP Problems")
        plt.ylabel("Time (seconds)")
        plt.xticks(rotation=30, ha="right")
        plt.legend()
        plt.tight_layout()

        time_chart_path = os.path.join(output_dir, "execution_time_comparison.png")
        plt.savefig(time_chart_path)
        plt.close()

        # 2. Memory Usage Comparison Chart
        plt.figure(figsize=(12, 6))

        for method in data["Method"].unique():
            method_data = data[data["Method"] == method]

            plt.plot(
                method_data["Problem"],
                method_data["Memory_KB"],
                marker="o",
                label=method
            )

        plt.title("Memory Usage Comparison")
        plt.xlabel("DP Problems")
        plt.ylabel("Memory (KB)")
        plt.xticks(rotation=30, ha="right")
        plt.legend()
        plt.tight_layout()

        memory_chart_path = os.path.join(output_dir, "memory_usage_comparison.png")
        plt.savefig(memory_chart_path)
        plt.close()

        return {
            "time_chart": time_chart_path,
            "memory_chart": memory_chart_path
        }