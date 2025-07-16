h = int(input("Nhập chiều cao: "))
for i in range(1, h + 1):
    for j in range(1, h + 1):
        if j <= i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(1, h + 1):
    print("*" * i)

for i in range(1, h + 1):
    for j in range(1, 2 * h):
        if j >= h - i + 1 and j <= h + i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
