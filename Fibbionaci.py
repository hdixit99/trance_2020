def generate_fibonacci_series(total_numbers):
    """
    Generate a Fibonacci series with the given total number of elements.

    :param total_numbers: Total number of elements in the Fibonacci series.
    :return: A list containing the Fibonacci series.
    """
    if total_numbers <= 0:
        return []
    elif total_numbers == 1:
        return [0]
    elif total_numbers == 2:
        return [0, 1]

    fibonacci_series = [0, 1]
    for _ in range(2, total_numbers):
        next_number = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_number)

    return fibonacci_series

# Example usage
if __name__ == "__main__":
    total = int(input("Enter the total number of Fibonacci numbers to generate: "))
    print(generate_fibonacci_series(total))5
    