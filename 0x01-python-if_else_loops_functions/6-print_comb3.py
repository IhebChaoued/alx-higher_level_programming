#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if i != j:
            if i == 8 and j == 9:
                print("{:02d}".format(int(str(i) + str(j)))
            else:
                print("{:02d}, ".format(int(str(i) + str(j))), end="")
