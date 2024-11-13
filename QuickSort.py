import random


def swap(arr, left, right):
    arr[left], arr[right] = arr[right], arr[left]

def partition(arr, i, j, key):
    left = i
    right = j
    half = (i + j) // 2
    pivot = arr[half][key]

    while True:
        # Move left and right pointers to the correct positions
        while arr[left][key] < pivot:
            left += 1
        while arr[right][key] > pivot:
            right -= 1

        # Check if pointers have crossed
        if left >= right:
            return right

        # Swap elements at left and right
        swap(arr, left, right)

        # Move pointers inward
        left += 1
        right -= 1

def quick_sort(arr, i, j, key):
    if i < j:
        p = partition(arr, i, j, key)
        quick_sort(arr, i, p, key)
        quick_sort(arr, p + 1, j, key)

def test_quick_sort():
    numbers = []
    n = input("Enter the number of elements to generate (between 0 and 100): ")

    try:
        n = int(n)
        if n <= 0:
            print("Please enter a positive integer.")
            return

        for i in range(n):
            numbers.append(random.randint(0, 100))

        print("\nUnsorted list:", numbers)
        quick_sort(numbers, 0, len(numbers) - 1)
        print("Sorted list:", numbers)

    except ValueError:
        print("Invalid input. Please enter a valid integer.")


