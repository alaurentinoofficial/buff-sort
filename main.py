import time

def quicksort(array, start=0, end=-1, reverse=False, key=lambda p:p):
  if end == -1:
    end = len(array)-1
  
  if start >= end:
    return

  pivot = key(array[end])
  cnt = start

  for i in range(start, end+1):
    if key(array[i]) >= pivot if reverse else key(array[i]) <= pivot:
      array[cnt], array[i] = array[i], array[cnt]
      cnt += 1
  
  quicksort(array, start, cnt-2, reverse, key)
  quicksort(array, cnt, end, reverse, key)

if __name__ == "__main__":
  array = [{'x': 34}, {'x': -3}, {'x': 25}, {'x': 25}, {'x': -3}]

  start = time.time()
  quicksort(array, key=lambda p : p["x"], reverse=True)
  qs_time = time.time() - start

  print(array)
  print(qs_time)
