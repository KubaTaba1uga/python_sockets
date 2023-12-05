NUMBER_IN_SEQUENCE = 40


def count_fibbonaci(n):
    n -= 2
    start_value = 1

    def count(n):
        if n <= 0:
            return start_value

        return __count_fibbonaci(n - 1, start_value) + __count_fibbonaci(
            n - 2, start_value
        )

    return count(n)


def __count_fibbonaci(n, value):
    if n <= 0:
        return value

    return __count_fibbonaci(n - 1, value) + __count_fibbonaci(n - 2, value)


if __name__ == "__main__":
    print(count_fibbonaci(NUMBER_IN_SEQUENCE))
