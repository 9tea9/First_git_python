class DigitCounter:
    """Utility class for digit-related operations."""

    @staticmethod
    def count_digits(num: int) -> int:
        """Return the number of digits in an integer."""
        return len(str(abs(num)))  # abs handles negatives
