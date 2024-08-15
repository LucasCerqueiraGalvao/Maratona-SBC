n, h = input().split()
n = int(n)
h = int(h)
a = [int (i) for i in input().split()]
n = 0
for i in a:
    if i <= h:
        n = n + 1

print (n)        