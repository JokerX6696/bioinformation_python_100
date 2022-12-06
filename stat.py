#!/bin/env python3
# python stat.py -i test.fq -o stat.txt
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i', help='input *.fastq  待统计文件', required=True)
parser.add_argument('-o', help='output stat.txt 统计结果', required=True)
args = parser.parse_args()

input = args.i
output = args.o
fi = open(input, 'r')
fo = open(output, 'w')
print("数据量(bp)",file=fo)
counts = 0
num = 0
for i in fi.readlines():
    counts += 1
    if counts % 4 == 2:
        num += (len(i) - 1)

print(num,file = fo)
fi.close
fo.close

print('统计完成！ 请查看输出的统计文件 %s' %output)
print('########################################################################\n              或者使用 ./stat.pl test.fq 命令验证\n########################################################################\n')
