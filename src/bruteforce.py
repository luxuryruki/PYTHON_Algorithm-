print("test")


# 합계구하기
def cal_sum(N):
    sum = 0
    for num in range(1,N+1):
        sum = sum+num
    return sum

print(cal_sum(10))

# 최소값
list = [1, 2, 3, 4, 10]
def get_min(list):
    min = list[0]
    for num in list:
        if(min > num):
            min = num
    return min
print(get_min(list))

# 최대값찾기
def get_max(list):
    max = list[0]
    for num in list:
        if(max < num):
            max = num
    return max
print(get_max(list))

# # 약수의 개수
def count_divisor(N):
    count = 0;
    for num in range(1, N+1):
        if(N%num == 0):
            count += 1
    return count
print(count_divisor(11))
