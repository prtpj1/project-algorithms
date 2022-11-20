def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0 or word == "":
        return False

    if low_index >= high_index:
        return True
    elif word[low_index] != word[high_index]:
        return False
    else:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)


if __name__ == "__main__":
    print(is_palindrome_recursive("SOCOS", 0, 4))
