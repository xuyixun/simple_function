def divisors(N: int):
    '''整数取中间约数（不包含1和自身）'''
    if N <= 1:
        return [1, 1]
    sqrt = N**0.5
    if (sqrt % 1) == 0:
        return [int(sqrt), int(sqrt)]
    res = [i for i in range(int(sqrt), 1, -1) if N % i == 0]
    if(len(res) > 0):
        return [res[0], N//res[0]]
    else:
        return divisors(N+1)
