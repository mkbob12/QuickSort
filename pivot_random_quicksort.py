# pivot을 random으로 설정 
import random
import time


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    # pivot 을 random 하게 설정 
    pivot = arr[random.randint(0,len(arr)-1)]  
    left = [x for x in arr if x < pivot] 
    middle = [x for x in arr if x == pivot]  
    right = [x for x in arr if x > pivot]  

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




