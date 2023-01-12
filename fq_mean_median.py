#!/bin/env python3
# 考虑到实际文件 每个reads 长度并不相同，无法组成标准矩阵，在这里不适用 pandas


fi = open('test.fq', 'r')
fq = fi.readlines()
fi.close

counts = 0
data = []
for line in fq:
    counts += 1
    if counts % 4 == 0:
        quality = line.strip().replace('\n', '')
        while len(quality) < 150:  # 考虑到实际情况，许多 reads 无法达到 150 bp 对 reads 进行补齐 ‘~’ 对应了 最大 ascii 值 
            quality += '~'
        data.append(quality)

del quality

fo = open('stat.xls', 'w')
print('pos','mean','median',sep='\t', file=fo)

for i in range(0,150):
    quality = [] 
    for read in data: # 每次循环是一个 read
        if read[i] != '~':
            quality.append(int(ord(read[i])))
    quality.sort()
    mean = sum(quality)/len(quality) - 33
    if len(quality) % 2 == 0:
        num_1 = len(quality)/2
        num_2 = num_1 + 1
        median = (quality[num_1] + quality[num_2])/2 - 33
    else:
        num = int(len(quality)/2) + 1
        median = quality[num]
    print(i+1,"%.2f" %(mean),median,sep='\t',file=fo)
    
fo.close
