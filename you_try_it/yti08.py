#_______________the first you try it in the 8 lecture--------------#
def add(x,y):
    return x+y
def mult(x,y):
    print(x*y)

#add(1,2)
#print(add(2,3))
#mult(3,4)
#print(mult(4,5))

#--------------the second you try it in the 8 lecture--------------#
#topic:Fix the code that try to write is_triangular()
def is_triangular(n):
    total = 0
    for i in range(1,n+1):
        total = total + i
        if total == n:
            return True
    return False

#print(is_triangular(4))        
#--------------the third you try it in the 8 lecture---------------#
#topic:how many integers have a square root within epsilon of n
def bisection_root(x):
    low = 0 
    high = x
    tolerance = 0.1
    average = (high + low)/2
    
    while abs(average**2 - x) >= tolerance:
        if average**2 < x:
            low = average
        else:
            high = average
        average = (high + low)/2
    return average
def count_nums_with_sqrt_close_to(n, epsilon):
    count = 0
    for i in range(int((n-epsilon)**2),int((n+epsilon)**2)+1):
        approx = bisection_root(i)
        if abs(approx-n)<epsilon:
            count = count + 1
    return count
#print(count_nums_with_sqrt_close_to(20, 0.1))         
#------------the forth you try it in 8 lecture----------#
def calc(op, x, y):
    return op(x,y)
def div(a, b):
    if b!=0:
        return a/b
    print("Demon was 0.")
#res = calc(div,2 ,0)
#-------------the firth you try it in 8 lecture----------#
#topic:Returns how many ints from 0 to n match
def apply(criteria,n):
    count = 0
    for i in range(0,n+1):
        if criteria(i):
            count = count + 1
    return count

def is_even(x):
    return x%2==0

how_many = apply(is_even,10)
print(how_many)
