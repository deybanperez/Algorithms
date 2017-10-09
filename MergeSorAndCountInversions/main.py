def mergeAndCountInversions(l_list, r_list, count):
    if len(l_list) == 0:
        return r_list, count
    if len(r_list) == 0:
        return l_list, count

    f_list = []
    i = 0
    j = 0
    for k in range(0, len(l_list) + len(r_list)):
        if l_list[i] < r_list[j]:
            f_list.append(l_list[i])
            i += 1
        else:
            f_list.append(r_list[j])
            j += 1
            count += len(l_list) - i

        if i == len(l_list):
            f_list.extend(r_list[j:])
            break

        if j == len(r_list):
            f_list.extend(l_list[i:])
            break
    return f_list, count


def mergeSortAndCountInversions(i_list, count):
    if len(i_list) == 1:
        return i_list, count

    m = len(i_list) // 2
    l_list = mergeSortAndCountInversions(i_list[:m], count)
    r_list = mergeSortAndCountInversions(i_list[m:], count)

    return mergeAndCountInversions(l_list[0], r_list[0], (l_list[1] + r_list[1]))


array = []
# f = open('test.txt', 'r')
f = open('IntegerArray.txt', 'r')
for line in f:
    array.append(int(line))
f.close()
result = mergeSortAndCountInversions(array, 0)
print(result)