#!/usr/bin/python3
# -*- coding: utf-8 -*-

a = tuple(i for _ in range(2) for i in map(int, input().split()))
s = input()

print(sum(a), s)
