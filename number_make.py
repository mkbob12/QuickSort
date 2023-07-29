import random 

with open('./result/forward_sort_numbers.txt','w') as forward_sorted_file:
    #파일 내용 읽기 
    for number in range(1,1000000):
        forward_sorted_file.write(str(number)+',')
        

# 역방향으로 파일 읽기 
with open('./result/reverse_sort_numbers.txt','w') as reverse_sorted_file:
    #파일 내용 읽기 
    for number in range(1000000,1):
        reverse_sorted_file.write(str(number)+',')




# 100만 개의 임의의 정수 생성
numbers = [random.randint(1, 1000000) for _ in range(1000000)]



# 파일에 정수 저장
with open('./result/random_numbers.txt', 'w') as file:
    for number in numbers:
        file.write(str(number) + ',')
        