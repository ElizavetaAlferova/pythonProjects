def fib(n):
    my_list = [i for i in range(0, n + 1)]
    fib=[0, 1, 1]
    if n>2:
        for i in range(3, n+1):
            fib.append(fib[i-1]+fib[i-2])

    return fib[n]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()