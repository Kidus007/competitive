x = input()
y = input()
count1 = 0
count2 = 0
f, g, k, h = [0], [0], [0], [0]

for i in x:
    f.append(int(i))
    count1 += 1

for j in y:
    g.append(int(j))
    count2 += 1

if count2 >= count1:
    k_values = [0]
    h_values = []
    for i in range(count2):
        if f[count1 - i] >= g[count2 - i]:
            we = str(f[count1])
            k_values.append(we)
        else:
            wo = str(g[count2])
            h_values.append(wo)

if g == h or k_values == f:
    print("YODA")
    if k_values == f:
        k_values.reverse()
        print(k_values)
    else:
        h_values.reverse()
        print(h_values)
else:
    k_values.reverse()
    h_values.reverse()
    print(k_values)
    print(h_values)