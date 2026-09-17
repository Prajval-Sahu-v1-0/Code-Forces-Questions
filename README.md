# Codeforces Questions

Personal repository for solving and practicing Codeforces problems.

## Structure

Each problem has its own directory:

``` text
Codeforces Questions/
├── P1933B/
│   ├── P1933B_test_case_1.txt
│   └── P1933B.py
├── PxxxxX/
│   ├── PxxxxX_test_case_1.txt
│   └── PxxxxX.py
└── ...
```

### Files

-   `PxxxxX.py` --- solution to the problem
-   `PxxxxX_test_case_*.txt` --- local test cases

## Running Solutions

### Linux

Navigate to the repository:

``` bash
cd "Codeforces Questions"
```

Run a solution normally:

``` bash
python3 P1933B/P1933B.py
```

Run with a test case:

``` bash
python3 P1933B/P1933B.py < P1933B/P1933B_test_case_1.txt
```

### Windows PowerShell

Navigate to the repository:

``` powershell
cd "Codeforces Questions"
```

Run a solution normally:

``` powershell
python .\P1933B\P1933B.py
```

Run with a test case:

``` powershell
Get-Content .\P1933B\P1933B_test_case_1.txt | python .\P1933B\P1933B.py
```

> PowerShell does not support the `<` stdin redirection operator used by
> Linux shells.

## Purpose

-   Practice competitive programming
-   Improve DSA and algorithmic problem solving
-   Keep solutions and test cases organized
-   Track progress across Codeforces problems

## Language

Solutions are primarily written in Python.
