#!/usr/bin/python3
# -*- coding: utf-8 -*-

# WA in the test cases, (N, Q) = (5, 7).

import sys
import string

def main():
    nq = tuple(map(int, input().split()))
    n, q = nq
    a = list(string.ascii_uppercase[:n])

    # merge sort
    b = [None] * n
    step = 1
    while step < n:
        left = 0
        while left < n:
            right = min(left + step, n)
            end = min(left + step * 2, n)
            i = left
            j = right
            for k in range(left, end):
                flg = i < right
                if flg == True:
                    flg = j >= end
                    if flg == False:
                        if q <= 0:
                            c = b[:k] + [e for e in a[left:end] if e not in b[left:k]] + a[end:]
                            print('!', ''.join(c))
                            sys.exit()
                        q -= 1
                        print('?', a[i], a[j])
                        sys.stdout.flush()
                        flg = input() == '<'
                if flg == True:
                    b[k] = a[i]
                    i += 1
                else:
                    b[k] = a[j]
                    j += 1
            left += step * 2
        a, b = b, a
        step *= 2

    print('!', ''.join(a))

if __name__ == '__main__':
    main()
