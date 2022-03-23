x = input().split()

for i in range(len(x)):
    x[i] = int(x[i])
x.sort()
if len(x) % 2 != 0:
    med = int(len(x)/2)
    print(x[med])
else:
    med = int(len(x) / 2)
    med1 = (x[med] + x[med-1])/2
    print(med1)

print(x)
