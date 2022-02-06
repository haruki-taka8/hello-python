# 009-LargeRepresentation.py

# Given two integers n and m,
# where n is the maximum value of a certain integer data type.

# Express m in terms of k * n + c

n, m = map(int, input().split())

k = m // n
c = m % n

print(k, '*', n, '+', c)