fibonacciList = [0, 1]
# finding 10 terms of the series starting from 3rd term
N = 11
for term in range(3, N + 1):
    value = fibonacciList[term - 2] + fibonacciList[term - 3]
    fibonacciList.append(value)
print("Fibonacci List from 1 to 55:")
print(fibonacciList)