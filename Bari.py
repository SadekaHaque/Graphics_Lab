# def minima(alist):
#     x = alist[0]
#     for i in alist:
#         if i < x:
#             x = i
#     return x
# print(minima([1,2, 3,4,5]))

s = int(input())
x = int(str(s)[-1])
if x >= 5:
    x = 0
    string.replace(s, s[len(s) - 1], x)
elif x < 5:
    x = 10
    string.replace(s, s[len(s) - 1], x)

print(s)