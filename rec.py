# modul
import random
from re import S
import timeit

# generate list
def generate_list(n):
    batas_atas = n * 100
    randomlist = random.sample (range(0, batas_atas),n)
    randomlist.sort()
    return randomlist

def cari_pasangan(data,target):
    for i in range(0, len(data)-1):
        for j in range(i,len(data)):
            if data[i] + data[j] == target:
                print(f"{data[i]} + {data[j]} = {target}")
                return True
    return False

for i in range(5000,55000,5000):
    data = generate_list(i)
    # target dibuat menjadi worst case
    target = -100

    # catat waktu mulai
    start = timeit.default_timer()

    # catat pasangan apakah memenuhi target
    hasil = cari_pasangan(data,target)

    # catat waktu hasil didapat
    end = timeit.default_timer()

    # output
    print(f"Ukuran {i} : {end-start} second")