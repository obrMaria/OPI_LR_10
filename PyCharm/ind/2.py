#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    # Определим универсальное множество
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"c", "g", "h", "k", "y"}
    b = {"a", "b", "k", "n", "u"}
    c = {"i", "j", "o", "y", "z"}
    d = {"a", "b", "f", "g", "y", "z"}

    x = (a.union(b)).intersection(d)

    print(f"x = {x}")

    na = u.difference(a)
    nb = u.difference(b)
    nc = u.difference(c)
    y = (na.intersection(d)).union(nc.difference(nb))
    print(f"y = {y}")