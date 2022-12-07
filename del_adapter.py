#!/bin/env python3
# 模拟 fastp 去接头
# python del_adapter.py -i test.fq --adapter_sequence CAACTGGTTCCATG -o py_del_adapter.fq
import argparse
parser = argparse.ArgumentParser()

parser.add_argument('-i', help='input *.fastq rawdata', required=True)
parser.add_argument('-o', help='output *.fastq  cleandata', required=True)
parser.add_argument('--adapter_sequence', help='adapter  seq', required=True)
args = parser.parse_args()

matchReq = 4
allowOneMismatchForEach = 8
adata = args.adapter_sequence
rlen = 150
alen = len(adata)
input = args.i
output = args.o
if alen < matchReq:
    print("错误 ，接头序列必须大于3！")
    exit(1)


fi = open(input, "r")
fo = open(output, 'w')
counts = 0
while True:  # 每次循环是一个 reads
    r_name = fi.readline().strip().replace('\n','')
    if not r_name:
        break
    r_seq = fi.readline().strip().replace('\n','')
    r_anno = fi.readline().strip().replace('\n','')
    r_qual = fi.readline().replace('\n','')
    pos = 0
    start = -3
    for pos in range(start,rlen-matchReq):  # 每次循环 adapter 与 read aligment 后移一位
        cmplen = min(rlen - pos, alen)
        allowedMismatch = int(cmplen/allowOneMismatchForEach)
        mismatch = 0
        mismatched = True
        rm_pos = (max(0, -pos) + pos)
        for i in range(max(0, -pos),cmplen):  # 每次循环 统计一次碱基是否错配
            if adata[i] != r_seq[i+pos]:
                mismatch += 1
                if mismatch > allowedMismatch:
                    mismatched = False
                    break
        if mismatched == True:
            break
    if mismatched == False:
        print(r_name,file=fo)
        print(r_seq,file=fo)
        print(r_anno,file=fo)
        print(r_qual,file=fo)
    elif rm_pos == 0:
        None
    else:
        print(r_name,file=fo)
        print(r_seq[:(rm_pos)],file=fo)
        print(r_anno,file=fo)
        print(r_qual[:(rm_pos)],file=fo)      






fo.close
fi.close
