import time
#rekursif
def fib_rekur(n):
    if n < 2:
        return n
    return fib_rekur(n-2) + fib_rekur(n-1)
for i in range (100):
    starttime=time.time()
    hasil = fib_rekur(i)
    endtime = time.time()
    print (hasil,":",endtime-starttime)


#iteratif
def fib_iter(n):
    fibs = [0, 1, 1]
    for f in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[n]
for i in range (100):
    starttime=time.time()
    hasil = fib_iter(i)
    endtime = time.time()
    print (hasil,":",endtime-starttime)