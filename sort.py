
# 파일에 정수 저장
with open('./result/random_numbers.txt', 'r') as file:
    contents = file.read()

# 숫자 추출 
numbers = contents.split(',')


numbers_list = []
for num in numbers[:-1]:
    numbers_list.append(int(num))

# sort로 정렬 
numbers_list.sort()

# 파일 열기 
with open('./result/use_sort_numbers.txt','w') as sorted_file:
    
    for number in numbers_list:
        sorted_file.write(str(number)+',')

