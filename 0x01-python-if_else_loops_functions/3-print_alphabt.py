#!/usr/bin/python3
for alpha in range(97, 123):
    if alpha == 101 or alpha == 123:
        alpha = alpha + 1
    else:
        print("{}".format(chr(alpha)), end='')
    