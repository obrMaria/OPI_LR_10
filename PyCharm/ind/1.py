#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # 1
    s = input("Введите строку: ").lower()
    vowels = set("aeiouy")
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    print('Количество глассных в предложении = ', count)

    # 2
    a = input('\n\nВведите строку\n')
    s1 = set(a.replace(' ', ''))
    a = input('Введите строку\n')
    s2 = set(a.replace(' ', ''))
    print('общие символы = ', s1.intersection(s2))
    print('количесвто общих символов = ', len(s1.intersection(s2)))