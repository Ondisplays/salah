def info(n):
    if n == 1:
        print("1")
    else:
        info(n-1)
        print(n)

info(9)