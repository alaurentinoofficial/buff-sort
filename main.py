import time

def quicksort(array, start, end):
  if start >= end:
    return
  
  pivot = array[end]
  cnt = start

  for i in range(start, end+1):
    if array[i] <= pivot:
      array[cnt], array[i] = array[i], array[cnt]
      cnt += 1

  quicksort(array, start, cnt-2) # left
  quicksort(array, cnt, end)     # right


if __name__ == "__main__":
  array = [7, 5, -3, 10, 11, 11, 2, 9, 5, 5, 8]
  array1 = [7, 5, -3, 10, 11, 11, 2, 9, 5, 5, 8]

  start = time.time()
  quicksort(array, 0, len(array)-1)
  qs_time = time.time() - start

  print(array)
  print(qs_time)
