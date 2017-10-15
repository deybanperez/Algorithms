def quicksort(array, lo, hi):
    total = 0
    if lo < hi:
        # swap(array, lo, lo) # first element as pivot 162085
        # swap(array, lo, hi) # last element as pivot 164123
        swap(array, lo, median(array, lo, lo + ((hi - lo) // 2), hi))  # median number as pivot 138382

        total = hi - lo
        p = partition(array, lo, hi)
        total += quicksort(array, lo, p - 1)
        total += quicksort(array, p + 1, hi)

    return total


def swap(array, a, b):
    c = array[a]
    array[a] = array[b]
    array[b] = c


def partition(array, lo, hi):
    p = array[lo]
    i = lo + 1
    j = i

    for j in range(lo + 1, hi + 1):
        if array[j] < p:
            swap(array, i, j)
            i += 1

    swap(array, i - 1, lo)
    return i - 1


def median(array, a, b, c):
    if array[b] >= array[a] >= array[c]:
        return a
    if array[c] >= array[a] >= array[b]:
        return a
    if array[a] >= array[b] >= array[c]:
        return b
    if array[c] >= array[b] >= array[a]:
        return b
    if array[a] >= array[c] >= array[b]:
        return c
    if array[b] >= array[c] >= array[a]:
        return c


array = []
# f = open('test.txt', 'r')
f = open('QuickSort.txt', 'r')
for line in f:
    array.append(int(line))
f.close()
# print(array)
total = quicksort(array, 0, len(array) - 1)
# print(array)
print(total)
