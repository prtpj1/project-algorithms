def is_anagram(first_string: str, second_string: str):
    word1 = list(first_string.casefold())
    word2 = list(second_string.casefold())

    string1 = "".join(merge_sort(word1))
    string2 = "".join(merge_sort(word2))

    if not first_string or not second_string:
        anagram = False
        return (string1, string2, anagram)
    elif string1 == string2:
        anagram = True
        return (string1, string2, anagram)
    else:
        anagram = False
        return (string1, string2, anagram)


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])

    return merge(left, right, array.copy())


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


if __name__ == "__main__":
    word1 = "pedra"
    word2 = "perdaa"
    print(is_anagram(word1, word2))
