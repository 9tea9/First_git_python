#from even_digit_numbers import EvenDigitNumbers
from squares_of_sorted_array import squaresofsortedarray

def main():
    # Example input
    
#    nums = [12, 345, 2, 6, 7896,12, -34, -5678]

#    processor = EvenDigitNumbers(nums)
#    result = processor.count_even_digit_numbers()

#    print(f"Input array: {nums}")
#    print(f"Count of numbers with even digits: {result}")
    
    nums = [-4, -1, 0, 3, 10]
    processor = squaresofsortedarray()
    result = processor.sortedSquares(nums)
    print(f"Input array: {nums}") 
    print(f"Sorted squares: {result}")
      

if __name__ == "__main__":
        main()
