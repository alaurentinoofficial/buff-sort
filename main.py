def QuickSort(list, buffer = [], count = 0):

    if count == len(list):
        return buffer

    elif count == 0:
        buffer.append(list[0])

    else:
        for i in range(len(buffer)):
            if i == len(buffer) - 1:
                buffer.append(list[count])
            elif list[count] <= buffer[i-1]:
                buffer.insert(i, list[count])
                break

    return QuickSort(list, buffer, count + 1)



print(QuickSort([23, 50, 10, 56, 0, 100, -2]))