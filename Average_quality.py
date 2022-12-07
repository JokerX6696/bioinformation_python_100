#!/bin/env python3
# python Average_quality.py
f = open('test.fq', 'r')
counts = 0
lines = 0
Q = 0
for line in f.readlines():
    counts += 1
    if counts % 4 == 0:
        line = line.strip().replace('\n','')
        lines += len(line)
        for i in line:
            Q += (ord(i) - 33)

f.close
mean = Q/lines
print('该文件碱基平均质量为 %.2f' %mean)
