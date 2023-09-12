array = [-10, 10, -1, 1]


def sumRealNumbers(arr):
    answer = 0
    for i in range(0, len(array)):
        answer = answer + arr[i]
    return answer

a = sumRealNumbers(array)
print(a)


def productRealNumbers(arr):
    answer = 1
    for i in range(0, len(array)):
        answer = answer * arr[i]
    return answer

a = productRealNumbers(array)
print(a)


