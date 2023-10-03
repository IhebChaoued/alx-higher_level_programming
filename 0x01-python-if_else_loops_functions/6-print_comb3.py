#!/usr/bin/python3
for i in range(0, 10):
    for j in range(1, 10):
        if i != j:
            print("{:02d}, ".format(int(str(i) + str(j))), end="")
