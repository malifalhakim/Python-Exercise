def fibonacci(n):
    a,b = 0,1
    list_fib = [a]
    while len(list_fib) <= n :
        a,b = b , a + b
        list_fib.append(a)
    print(f"Fibonacci ke - {n} = {list_fib[n-1]}")

fibonacci(7)