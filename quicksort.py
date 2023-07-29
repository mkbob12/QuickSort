import time 

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # 리스트의 중간값을 피벗으로 선택
    left = [x for x in arr if x < pivot]  # 피벗보다 작은 값들을 모은 리스트
    middle = [x for x in arr if x == pivot]  # 피벗과 같은 값들을 모은 리스트
    right = [x for x in arr if x > pivot]  # 피벗보다 큰 값들을 모은 리스트

    # 왼쪽, 가운데, 오른쪽 부분 리스트를 재귀적으로 정렬하고 병합
    return quicksort(left) + middle + quicksort(right)

# 테스트
if __name__ == "__main__":
   # 파일에 정수 저장
    with open('./result/random_numbers.txt', 'r') as file:
        contents = file.read()

    # 숫자 추출 
    numbers = contents.split(',')


    numbers_list = []
    for num in numbers[:-1]:
        numbers_list.append(int(num))
    
    start = time.time()
    arr = quicksort(numbers_list)
    end = time.time()
    print(end - start)




