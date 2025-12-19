def second_largest(arr):
    first = second = None

    for num in arr:
        if first is None or num > first:
            second = first
            first = num
        elif num != first and (second is None or num > second):
            second = num

    if second is None:
        raise ValueError("No second largest element")

    return second


try:
    size = int(input("Enter size: "))
    if size < 2:
        raise ValueError("Size must be at least 2")

    arr = []
    for i in range(size):
        arr.append(int(input(f"Enter value [{i+1}]: ")))

    print("\nOriginal array:", arr)
    print("Second largest value:", second_largest(arr))

except ValueError as e:
    print("Invalid input:", e)