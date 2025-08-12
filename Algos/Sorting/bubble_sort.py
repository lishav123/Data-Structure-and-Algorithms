
class Sorting:

    @staticmethod
    def bubble_sort(arr: list) -> None:
        """
        Sorts an array using the bubble sort algorithm.

        :param arr: List of elements to be sorted
        :return: Sorted list of elements
        """
        
        for i in range(len(arr)): # outerloop
            for j in range(len(arr) - 1 - i): # innerloop
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == '__main__':
    list_sample = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"List Sample(After bubble sort): {list_sample}")
    Sorting.bubble_sort(list_sample)
    print(f"List Sample(After bubble sort): {list_sample}")
