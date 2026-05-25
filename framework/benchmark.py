import time
import tracemalloc


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