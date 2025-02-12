from core import filter_even, square, double, filter_greater_than, sum_squares, compose

def main():
    numbers = list(range(1, 11))

    # Define a pipeline that applies transformations
    pipeline = compose(
        square,            # Square the numbers
        double,            # Double each number
        filter_even        # Keep only even numbers
    )

    transformed_numbers = pipeline(numbers)
    filtered_numbers = filter_greater_than(transformed_numbers, 50)
    total = sum_squares(filtered_numbers)

    print("Transformed Numbers:", transformed_numbers)
    print("Filtered Numbers:", filtered_numbers)
    print("Sum of Squares:", total)

if __name__ == "__main__":
    main()
