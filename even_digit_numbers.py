from digit_counter import DigitCounter


class EvenDigitNumbers:
    """Class to process arrays and find numbers with even digits."""

    def __init__(self, nums: list[int]):
        self.nums = nums

    def count_even_digit_numbers(self) -> int:
        """Return how many numbers in the array contain an even number of digits."""
        count = 0
        for num in self.nums:
            if DigitCounter.count_digits(num) % 2 == 0:
                count += 1
        return count
