# 003-Fibonacci.py
# List fibonacci numbers
# New concept: constant-like variables

a = 0
b = 1
c = a + b
UNTIL = 1000

print(0)
print(1)
while c < UNTIL:
    print(c)

    a = b
    b = c
    c = a + b