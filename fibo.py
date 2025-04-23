# fibonacci seq
def fibo(n:int):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
