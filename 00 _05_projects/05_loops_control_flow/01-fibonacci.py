"""
This program generates the Fibonacci sequence starting from 0 and 1.
It continues generating terms until reaching the maximum value of 10,000.
"""

max_value = 10000

Fterm_a = 0
Fterm_b = 1

print(Fterm_a, end= " ")

while Fterm_b < max_value:
    print(Fterm_b, end= " ")
    Fterm_a, Fterm_b = Fterm_b, Fterm_a + Fterm_b