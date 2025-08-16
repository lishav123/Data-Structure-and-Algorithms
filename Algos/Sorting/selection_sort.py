from typing import List

class Sorting:
    """
    A class containing different implementations of the selection sort algorithm.
    """

    @staticmethod
    def selection_sort(items: List[int]) -> None:
        """
        Sorts a list of integers in-place using the classic selection sort algorithm.

        Args:
            items (List[int]): The list of integers to be sorted.

        This method iterates through the list, finds the minimum element in the unsorted part,
        and swaps it with the first unsorted element.
        """
        for i_idx in range(len(items) - 1):
            min_value, min_index = items[i_idx], i_idx 

            for j_idx in range(i_idx, len(items)):
                if min_value > items[j_idx]: # finding the minimum value
                    min_value, min_index = items[j_idx], j_idx

            items[i_idx], items[min_index] = items[min_index], items[i_idx] # swapping the current ith index with the minimun value in list

    @staticmethod
    def selection_sort_pythonic(items: List[int]) -> None:
        """
        Sorts a list of integers in-place using a more Pythonic approach to selection sort.

        Args:
            items (List[int]): The list of integers to be sorted.

        This method uses Python's min() function with a key to find the index of the minimum
        element in the unsorted part and swaps it with the first unsorted element.
        """
        for i in range(len(items) - 1):
            min_idx = min(range(i, len(items)), key=lambda x: items[x])
            items[i], items[min_idx] = items[min_idx], items[i]

if __name__ == '__main__':
    # Example usage of classic selection sort
    items = [100002, -23, 3433, 5655, 0]
    print(f'Before(Selection sort): {items}')
    Sorting.selection_sort(items)
    print(f'After (Selection sort): {items}')

    # Example usage of Pythonic selection sort
    items2 = [100002, -23, 3433, 5655, 0]
    print(f'Before(Pythonic Selection sort): {items2}')
    Sorting.selection_sort_pythonic(items2)
    print(f'After (Pythonic Selection sort): {items2}')


