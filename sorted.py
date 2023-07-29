
# 파일에 정수 저장
with open('./result/random_numbers.txt', 'r') as file:
    contents = file.read()

# 숫자 추출 
numbers = contents.split(',')

# 숫자로 변환 
numbers_list = []
for num in numbers[:-1]:
    numbers_list.append(int(num))

# 정렬된 리스트 출력
numbers_list = sorted(numbers_list)

# 파일 열기 
with open('./result/use_sorted_numbers.txt','w') as sorted_file:
    #파일 내용 읽기 
    for number in numbers_list:
        sorted_file.write(str(number)+',')

