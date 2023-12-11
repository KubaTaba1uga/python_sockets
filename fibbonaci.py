NUMBER_IN_SEQUENCE = 40


def count_fibbonaci(n):
    if n <= 1:
        return n

    return count_fibbonaci(n - 2) + count_fibbonaci(n - 1)


if __name__ == "__main__":
    print(count_fibbonaci(NUMBER_IN_SEQUENCE))
