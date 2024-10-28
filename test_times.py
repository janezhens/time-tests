# Import the functions from times.py
from times import time_range, compute_overlap_time

def test_given_input():
    # Recreate the input conditions
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    
    # Calculate the result using the function
    result = compute_overlap_time(large, short)
    
    # Fill in the expected value (You can copy the output generated earlier)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:45:00'), ('2010-01-12 10:46:00', '2010-01-12 10:47:00')]
    
    # Assert that the result matches the expected value
    assert result == expected, f"Test failed! Expected: {expected}, but got: {result}"


def test_no_overlap():
    # Two time ranges that do not overlap
    range1 = time_range("2010-01-12 08:00:00", "2010-01-12 09:00:00")
    range2 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    
    # Calculate the result
    result = compute_overlap_time(range1, range2)
    
    # Expected result is an empty list because there is no overlap
    expected = []
    
    # Assert
    assert result == expected, f"Test failed! Expected: {expected}, but got: {result}"


def test_multiple_intervals():
    # Two time ranges that both contain several intervals each
    range1 = time_range("2010-01-12 08:00:00", "2010-01-12 12:00:00", 4, 300)
    range2 = time_range("2010-01-12 09:30:00", "2010-01-12 11:30:00", 3, 600)
    
    # Calculate the result
    result = compute_overlap_time(range1, range2)
    
    # Define the expected result (manual calculation based on your time intervals)
    expected = [
        ('2010-01-12 09:30:00', '2010-01-12 10:30:00'),
        ('2010-01-12 10:35:00', '2010-01-12 11:30:00')
    ]
    
    # Assert
    assert result == expected, f"Test failed! Expected: {expected}, but got: {result}"


def test_exactly_touching():
    # Two time ranges that end exactly at the same time when the other starts
    range1 = time_range("2010-01-12 08:00:00", "2010-01-12 09:00:00")
    range2 = time_range("2010-01-12 09:00:00", "2010-01-12 10:00:00")
    
    # Calculate the result
    result = compute_overlap_time(range1, range2)
    
    # Expected result should be empty because the ranges touch but do not overlap
    expected = []
    
    # Assert
    assert result == expected, f"Test failed! Expected: {expected}, but got: {result}"


# Call all the test functions if running this file directly
if __name__ == "__main__":
    test_given_input()
    print("Test given input passed!")
    
    test_no_overlap()
    print("Test no overlap passed!")
    
    test_multiple_intervals()
    print("Test multiple intervals passed!")
    
    test_exactly_touching()
    print("Test exactly touching passed!")
