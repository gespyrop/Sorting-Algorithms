def quick_sort(A):
    if len(A) <= 1:
        return A
    else:
        pivot = A.pop()
        left = []
        right = []

        for i in A:
            if i <= pivot:
                left.append(i)
            else:
                right.append(i)

        return quick_sort(left) + [pivot] + quicksort(right)