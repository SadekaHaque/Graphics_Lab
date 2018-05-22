# def sum(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum = sum + i
#     return sum
#
#
# print(sum(10))


import time
# def sum_of_n_2(n):
#     start = time.time()
#
#     the_sum = 0
#     for i in range(1, n + 1):
#         the_sum = the_sum + i
#     end = time.time()
#     return the_sum, end - start
#
# for i in range(5):
#     print("Sum is %d required %10.7f seconds" % sum_of_n_2(10000))
# def sum3(n):
#      start = time.time()
#      sum = (n*(n+1))/2
#      end = time.time()
#      return sum, end - start
# print("sum is %d and time %10.7f sec" % sum3(1000))

def sum4(n):
    x = 0
    a = 0
    for i in range(n):
        for j in range(n+1):
            x = i*j
    print (x)
    for k in range(1, n, 2):
        a = a + k
    print(a)
    return x, a

print(sum4(20))





