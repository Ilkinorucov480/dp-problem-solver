# Dynamic Programming Problem Solver

Bu layihə 5 klassik dinamik proqramlaşdırma problemini vahid framework daxilində həll etmək üçün hazırlanmışdır.

Layihədə hər problem üçün 3 fərqli yanaşma tətbiq olunur:

1. Memoization
2. Tabulation
3. Space Optimized Approach

## Layihənin məqsədi

Layihənin əsas məqsədi dinamik proqramlaşdırma problemlərini yalnız həll etmək deyil, həm də müxtəlif yanaşmaların işləmə vaxtı və yaddaş istifadəsi baxımından müqayisəsini aparmaqdır.

Bu layihə aşağıdakıları əhatə edir:

- 5 klassik DP probleminin realizasiyası
- Ümumi solver framework arxitekturası
- Memoization və tabulation müqayisəsi
- Space optimization yanaşmaları
- Benchmark ölçmələri
- CSV nəticələri
- Qrafiklərlə vizual analiz

## Həll olunan problemlər

1. 0/1 Knapsack
2. Longest Common Subsequence
3. Longest Increasing Subsequence
4. Edit Distance
5. Matrix Chain Multiplication

## Layihə strukturu

```text
dp-problem-solver/
│
├── main.py
├── requirements.txt
├── README.md
│
├── framework/
│   ├── base_solver.py
│   ├── benchmark.py
│   └── memory_tracker.py
│
├── problems/
│   ├── knapsack.py
│   ├── lcs.py
│   ├── lis.py
│   ├── edit_distance.py
│   └── matrix_chain.py
│
├── data/
│   └── test_cases.json
│
└── results/
    ├── benchmark_results.csv
    └── charts/
        ├── execution_time_comparison.png
        └── memory_usage_comparison.png