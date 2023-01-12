#!/bin/env python3
fi = open('test.fq', 'r')
fq = fi.readlines()
fi.close

counts = 0
data = []
for line in fq:
    counts += 1
    if counts % 4 != 0 and counts %2 ==0:
        quality = line.strip().replace('\n', '')
        while len(quality) < 150:  # 考虑到实际情况，许多 reads 无法达到 150 bp 对 reads 进行补齐 ‘~’ 对应了 最大 ascii 值 
            quality += '~'
        data.append(quality)


del quality

fo = open('stat.xls', 'w')
print('pos','A','T', 'C', 'G', 'N',sep='\t', file=fo)

for i in range(0,150):
    A,T,C,G,N = 0,0,0,0,0
    for read in data: # 每次循环是一个 read
        if read[i] == '~':
            continue
        elif read[i] == 'A':
            A += 1
        elif read[i] == 'T':
            T += 1
        elif read[i] == 'C':
            C += 1
        elif read[i] == 'G':
            G += 1
        elif read[i] == 'N':
            N += 1
    All = A + T + C + G + N
    print(i+1,"%.2f" %(A/All),"%.2f" %(T/All),"%.2f" %(C/All),"%.2f" %(G/All),"%.2f" %(N/All),sep='\t',file=fo)
    
fo.close

print("#########################################################################################")
print("########################    脚本执行成功，请查看文件 stat.xls    ########################")
print("#########################################################################################")
