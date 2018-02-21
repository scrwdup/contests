#!/usr/bin/python3
# -*- coding: utf-8 -*-

from decimal import Decimal, ROUND_HALF_UP

def main():
    a, b = map(int, input().split())
    print(Decimal((a + b) / 2).quantize(0, ROUND_HALF_UP))

if __name__ == '__main__':
    main()
