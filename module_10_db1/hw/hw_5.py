

def find_insert_position(A, x):
    for i, v in enumerate(A):
        if A[i - 1] < x < A[i + 1]:
            print(f'Позиция: {i+1}')
            return i+1


if __name__ == '__main__':
    A = [1, 2, 3, 3, 3, 5]
    x = 4
    assert find_insert_position(A, x) == 5