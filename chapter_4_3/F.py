def merge(left: list, right: list) -> list:
    i = j = 0
    len_left: int = len(left)
    len_right: int = len(right)
    temp = []

    while i < len_left and j < len_right:
        if left[i] < right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1

    temp += left[i:]
    temp += right[j:]

    return temp


def merge_sort(arr: list):
    # Базовый случай
    length: int = len(arr)
    if length <= 1:
        return arr

    middle: int = length // 2
    left: list = arr[:middle]
    right: list = arr[middle:]

    left: list = merge_sort(left)
    right: list = merge_sort(right)

    return merge(left, right)


if __name__ == '__main__':
    print(merge_sort([3, 1, 5, 3]))
    # print(merge([6], [2]))  # [2, 6]
