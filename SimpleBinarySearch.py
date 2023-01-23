import time

def search(items, target):
    low = 0
    high = len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

items = range(1000000)

start = time.time()
search(items, 999999) # Procura pelo último item
stop = time.time()
print(stop-start)

start = time.time()
search(items, 499999) # Procura pelo item do meio
stop = time.time()
print(stop-start)

start = time.time()
search(items, 10) # Procura por um item no início
stop = time.time()
print(stop-start)