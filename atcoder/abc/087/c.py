#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
    n = int(input())
    a = tuple(tuple(e for e in map(int, input().split())) for _ in range(2))
    dp = [[None] * n for _ in range(2)]
    dp[0][0] = a[0][0]
    dp[1][0] = a[1][i]
    for i in range(1, n):
        dp[0][i] = dp[0][i - 1] + a[0][i]
        dp[1][i] = max(dp[0][i], dp[1][i - 1]) + a[1][i]
    print(dp[1][n - 1])

if __name__ == '__main__':
    main()
