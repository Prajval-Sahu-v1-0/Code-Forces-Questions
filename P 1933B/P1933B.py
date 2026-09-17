import sys
input = sys.stdin.readline

result = []
test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    list_a  = list(map(int, input().split()))

    remainder = sum(list_a) % 3

    if remainder == 0:
        result.append(0)
    elif remainder == 1:
       if any(x % 3 == 1 for x in list_a):
            result.append(1)
       else:
            result.append(2)
    elif remainder == 2:
        result.append(1)
print('\n'.join(map(str, result)))
