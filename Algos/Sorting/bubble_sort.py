from typing import List

class Sorting:
    """
    A class containing sorting algorithms.
    """

    @staticmethod
    def bubble_sort(arr: List[int]) -> None:
        """
        Sorts a list of integers in-place using the bubble sort algorithm.

        Args:
            arr (List[int]): The list of integers to be sorted.

        This method repeatedly steps through the list, compares adjacent elements,
        and swaps them if they are in the wrong order. The process is repeated
        until the list is sorted.
        """
        for i in range(len(arr)):  # Outer loop for each pass
            for j in range(len(arr) - 1 - i):  # Inner loop for comparisons
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap if out of order

if __name__ == '__main__':
    # Example usage of bubble sort
    list_sample = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"List Sample (Before bubble sort): {list_sample}")
    Sorting.bubble_sort(list_sample)
    print(f"List Sample (After bubble sort): {list_sample}")
