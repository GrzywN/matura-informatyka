def qs(arr: list[int], low: int, high: int) -> None:
    if low >= high:
        return

    pivot_index = partition(arr, low, high)

    qs(arr, low, pivot_index - 1)
    qs(arr, pivot_index + 1, high)


def partition(arr: list[int], low: int, high: int) -> int:
    pivot = arr[high]
    index = low - 1

    for i in range(low, high):
        if arr[i] <= pivot:
            index += 1
            tmp = arr[i]
            arr[i] = arr[index]
            arr[index] = tmp
    index += 1
    arr[high] = arr[index]
    arr[index] = pivot

    return index


def quick_sort(arr: list[int]) -> None:
    qs(arr, 0, len(arr) - 1)


tab = [1, 4, 2, 3, 4, 6, 787, 86, 0]
print(tab)
quick_sort(tab)
print(tab)

# Złożoność czasowa - O(n log(n)) - O(n^2)
# Złożoność pamięciowa - O(1)
