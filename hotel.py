def get_price(d: int, a: int, n: int) -> int:
    days = 32 - n
    diaria = d + (a * (min(n, 15) - 1))

    return diaria * days


D = int(input())
A = int(input())
N = int(input())

print(get_price(D, A, N))
