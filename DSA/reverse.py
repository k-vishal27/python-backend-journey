def reverse_array(lst):
    if len(lst) < 2:
        return lst

    left, right = 0, len(lst) - 1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

    return lst


try:
    size = int(input("Enter size: "))
    if size <= 0:
        raise ValueError("Size must be positive")

    lst = []
    for i in range(size):
        lst.append(int(input(f"Enter value [{i+1}]: ")))

    print("\nOriginal array:", lst)
    print("Reversed array:", reverse_array(lst))

except ValueError as e:
    print("Invalid input:", e)
