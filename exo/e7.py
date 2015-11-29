#! /usr/bin/env python

def zip_lists(l1, l2):
    out = []
    for i in range(max(len(l1), len(l2)):
        out.append([l1[i], l2[i]])
    return out


print zip_lists(["This", "is", "fun", "right", "?"], [1, 2, 3, 4])



