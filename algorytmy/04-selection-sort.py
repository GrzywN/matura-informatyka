def find_smallest(arr: list[int]) -> int:
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def find_highest(arr: list[int]) -> int:
    highest = arr[0]
    highest_index = 0

    for i in range(1, len(arr)):
        if arr[i] > highest:
            highest = arr[i]
            highest_index = i
    return highest_index


def selection_sort(arr: list[int]) -> list[int]:
  new_arr = []
  for i in range(len(arr)):
      smallest = find_smallest(arr)
      new_arr.append(arr.pop(smallest))
  return new_arr


print(selection_sort([5, 3, 6, 2, 10]))
