def merge_sort(A):
	if len(A) == 1:
		return A

	A1 = A[:len(A) // 2]
	A2 = A[len(A) // 2:]

	A1 = merge_sort(A1)
	A2 = merge_sort(A2)

	return merge(A1,A2)

def merge(A, B):
	C = []

	while len(A) != 0 and len(B) != 0:
		if(A[0] > B[0]):
			C.append(B.pop(0))
		else:
			C.append(A.pop(0))

	while len(A) > 0:
		C.append(A.pop(0))

	while len(B) > 0:
		C.append(B.pop(0))

	return C