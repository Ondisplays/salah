import random
import time

def generate_list(n):
    batas_atas = n * 100
    randomlist = random.sample(range(0, batas_atas), n)
    randomlist.sort()
    return randomlist

def cari_pasangan(data, target):
    for i in range(0, len(data)-1):
        for j in range(i, len(data)):
            if data[i]+data[j] == target:
                print(data[i], '+', data[j], '=', target)
                return True
    return False

data = generate_list(10000)
print(data)

start = time.time()
hasil = cari_pasangan(data, -1)
end = time.time()
print('Waktu', '=',end-start)

hasil = cari_pasangan(data, 154)
print(hasil)