# factorial
# O(N)
def my_fact(n):
    if (n == 1) :
        return 1
    return n * my_fact(n-1)

print(my_fact(5))



# fibonaci
#O(2^N)
def fibo(n):
    if(n == 0 or n == 1) :
        return n
    return (fibo(n-1) + fibo(n-2))
print(fibo(10))

# square root
def my_sqrt(n) :
    if(n >= 1) :
        sol = my_sqrt_rec(1,n,n)
    else:
        sol = -1
    return sol

def my_sqrt_rec(low, high, num) :
    ans = (low + high) / 2
    diff= (ans * ans) - num
    if(abs(diff) < 0.0001):
        return ans
    elif(diff>0) :
        return my_sqrt_rec(low,ans,num)
    else:
        return my_sqrt_rec(ans,high, num)

print(my_sqrt(4))