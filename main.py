def QuickSortRecursion(list, direction=1, buffer = [], count = 0):

    if count == len(list):
        return buffer

    elif count == 0:
        buffer.append(list[0])

    else:
        for i in range(len(buffer)):
            if i == len(buffer) - 1:
                buffer.append(list[count])
            elif list[count] < buffer[i-1] if direction == 1 else list[count] > buffer[i-1]:
                buffer.insert(i, list[count])
                break

    return QuickSortRecursion(list, direction, buffer, count + 1)

def QuickSortLoop(list, direction=1):
    buffer = [list[0]]

    for count in range(1, len(list)):
        for i in range(len(buffer)):
            if i == len(buffer) - 1:
                buffer.append(list[count])
            elif list[count] < buffer[i-1] if direction == 1 else list[count] > buffer[i-1]:
                buffer.insert(i, list[count])
                break

    return buffer



print(QuickSortRecursion([23, 50, 23, 10, 56, 0, 100, -2], 1))
print(QuickSortLoop([23, 50, 23, 10, 56, 0, 100, -2], -1))