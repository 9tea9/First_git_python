class squaresofsortedarray:
    def sortedSquares(self, nums):
        """
        Given an array of integers nums sorted in non-decreasing order,
        return an array of the squares of each number sorted in non-decreasing order.
        """
        return sorted(x * x for x in nums)