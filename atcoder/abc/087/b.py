#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())
    cnt = 0
    for i in range(a + 1):
        y = x - 500 * i
        if y <= 0:
            if y == 0:
                cnt += 1
            break
        for j in range(b + 1):
            z = y - 100 * j
            if z <= 0:
                if z == 0:
                    cnt += 1
                break
            if z // 50 <= c:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
