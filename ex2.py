# analysh akeraioy ex.2


def factor(n):
    if n==1:
        return []
    b=2
    while b<= n:
        while not n% b:
            return [b] + factor(n // b)
        b += 1


print('Enter an integer:')
x = int(input())
print(*factor(x), sep="*")