s = int(input())
x = int(str(s)[-1])
if x >= 5:
    x = 0
    string.replace(s, s[len(s) - 1], x)
elif x < 5:
    x = 10
    string.replace(s, s[len(s) - 1], x)

print(s)
