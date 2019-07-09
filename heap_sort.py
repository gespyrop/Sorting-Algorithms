def parent(i):
	return i / 2

def left(i):
	return 2 * i

def right(i):
	return 2 * i + 1

#Subtracting 1 from the index to use 1 to len(A) as indexes
def swap(A, i, j):
	A[i - 1], A[j - 1] = A[j - 1], A[i - 1]

def heapify(A ,i):
	l = left(i)
	r = right(i)

	if l <= len(A) and A[l - 1] > A[i - 1]:
		largest = l
	else:
		largest = i

	if r <= len(A) and A[r - 1] > A[largest - 1]:
		largest = r

	if largest != i:
		swap(A, i, largest)
		heapify(A, largest)

def buildHeap(A):
	for i in range(1,len(A)//2 + 1)[::-1]:
		heapify(A, i)


def heap_sort(A):
	buildHeap(A)

	sorted = []

	for i in range(2,len(A) + 1)[::-1]:
		swap(A, 1, i)
		sorted.insert(0, A.pop())
		heapify(A, 1)

	sorted.insert(0, A.pop())

	return sorted
