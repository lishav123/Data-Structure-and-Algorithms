from typing import List

class Sorting:
    """
    A class containing sorting algorithms.
    """

    @staticmethod
    def insertion_sort(items: List[int]) -> None:
        """
        Sorts a list of integers in-place using the classic insertion sort algorithm.

        Args:
            items (List[int]): The list of integers to be sorted.

        This method iterates through the list, and for each element, it moves it leftward
        until it is in the correct position among the sorted part of the list.
        """
        for i in range(1, len(items)):
            temp_index = i
            # Move the current element leftward until it's in the correct position
            while temp_index > 0 and items[temp_index] < items[temp_index - 1]:
                items[temp_index], items[temp_index - 1] = items[temp_index - 1], items[temp_index]
                temp_index -= 1

if __name__ == '__main__':
    items = [23, 200000, -34, -43434343, 0]
    print(f"Before (Insertion Sort): {items}")
    Sorting.insertion_sort(items)
    print(f"After  (Insertion Sort): {items}")
