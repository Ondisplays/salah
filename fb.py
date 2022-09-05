import random
def generate_list(n):
    batas_atas = n + 100
    randomlist = random.sample(range(0, batas_atas), n)
    randomlist.sort()
    return randomlist

data = generate_list(100)
print(data)