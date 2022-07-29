def get_maior_valor(n: int, m: int, s: int) -> int:
    for i in range(m, n - 1, -1):
        number = str(i)
        sum = 0

        for digit in number:
            sum += int(digit)

        if sum == s:
            return i

    return -1


N = int(input())
M = int(input())
S = int(input())

print(get_maior_valor(N, M, S))
