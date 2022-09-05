def faktorial_iteratif(n): # fungsi iteratif (non-rekursif)
    hasil = 1
    for i in range(n, 0, -1):
        hasil = hasil * i
    return hasil

def faktorial_rekursif(n): # fungsi rekursif
    if n == 1:
        return 1
    else:
        return n * faktorial_rekursif(n-1)

hasil1 = faktorial_iteratif(10)
print('Faktorial 20 dengan cara iteratif: ', hasil1)
hasil2 = faktorial_rekursif(10)
print('Faktorial 20 dengan cara rekursif: ', hasil2)