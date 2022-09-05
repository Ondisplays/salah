import time

#waktu mulai
start = time.time()

#ON^2
n = 10000
for i in range(1,n):
    for j in range(1,n):
        print(end="")

#waktu selesai
end = time.time()

print('n =',n,end-start,"detik")