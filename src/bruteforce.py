
# 합계구하기
def cal_sum(N):
    sum = 0
    for num in range(1,N+1):
        sum = sum+num
    return sum

print(cal_sum(10))

# 최소값

def get_min(list):
    min = list[0]
    for num in list:
        if(min > num):
            min = num
    return min
list = [1, 2, 3, 4, 10]
print(get_min(list))

# 최대값찾기
def get_max(list):
    max = list[0]
    for num in list:
        if(max < num):
            max = num
    return max
list = [1, 2, 3, 4, 10]
print(get_max(list))

# 약수의 개수
def count_divisor(N):
    count = 0
    for num in range(1, N+1):
        if(N%num == 0):
            count += 1
    return count
print(count_divisor(10))


# 특정 문자의 개수 찾기
def count_char(string):
    count = 0
    for ch in string:
        if(ch == 'a'):
            count += 1
    return count
string = "There is an apple in the table"
print(count_char(string))

# 선택 정렬


def sort_desc(list):
    sorted_list = []
    while (len(list) > 0 ):
        index = get_max_index(list)
        num = list.pop(index)
        sorted_list.append(num)
    return sorted_list

def get_max_index(list):
    max_index = 0
    for index in range(len(list)):
        if(list[max_index] < list[index]):
            max_index = index

    return max_index

def sort_asc(list):
    sorted_list = []
    while (len(list) > 0 ):
        index = get_min_index(list)
        num = list.pop(index)
        sorted_list.append(num)
    return sorted_list

def get_min_index(list):
    min_index = 0
    for index in range(len(list)):
        if(list[min_index] > list[index]):
            min_index = index

    return min_index
list =[3, 2, 1, 5, 7, 6]
print(sort_desc(list))
list =[3, 2, 1, 5, 7, 6]
print(sort_asc(list))
# 최근접 거리

def closest_dist(points):
    count = len(points)
    min = float("inf")
    for i in range(count-1):
        for j in range(i+1, count):
            dist = cal_dist(points[i],points[j])
            if(dist < min):
                min = dist
    return min

def cal_dist(p1, p2):
    x_dist = (p1[0] - p2[0])**2
    y_dist = (p1[1] - p2[1])**2
    dist = (x_dist + y_dist)**0.5
    return dist
points = [(2,3),(3,5),(8,10),(11,-1)]
print(closest_dist(points))
# 배낭 Knpsack 문제