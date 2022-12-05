#!/bin/env python
# fastq 格式转为 fasta
# python phred33_2_64.py -i test.fq -o temp.fq

import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i', help='input *.fastq  (phred33)', required=True)
parser.add_argument('-o', help='output *.fastq  (phred64)', required=True)
args = parser.parse_args()

input = args.i
output = args.o
class fq_check:
    """检查文件完整性"""
    def __init__(self):
        print('正在检验 fq 文件完整性')

    def line_all(self):
        print("文件完整！")

    def line_2_err(self):
        print("文件行数错误! 请检查 fq 文件完整性！")
        print("最后一行为 reads 第一行！")
        exit(2)

    def line_3_err(self):
        print("文件行数错误! 请检查 fq 文件完整性！")
        print("最后一行为 reads 第二行！")
        exit(3)

    def line_4_err(self):
        print("文件行数错误! 请检查 fq 文件完整性！")
        print("最后一行为 reads 第三行！")
        exit(4)

CHECK = fq_check()
fi = open(input, 'r')
fo = open(output, 'w')
counts = 1
while True:
    reads_info = fi.readline()
    if counts == 1 and '@' not in reads_info:
        print('文件错误，第一行必须是reads 名称开头！')
        break
    elif not reads_info:
        CHECK.line_all()
        break
    else:
        fo.write(reads_info)
    reads_bases = fi.readline()
    if not reads_bases:
        CHECK.line_2_err()
    else:
        fo.write(reads_bases)
    reads_Anno = fi.readline()
    if not reads_Anno:
        CHECK.line_3_err()
    else:
        fo.write(reads_Anno)
    reads_quality = fi.readline()
    if not reads_quality:
        CHECK.line_4_err()
    else:
        reads_quality = reads_quality.strip().replace('\n', '')
        Q = ""
        for i in reads_quality:
            qc = ord(i) + 31
            Q += chr(qc)
        fo.write(Q + '\n')
    counts += 1
(base) zhengfx@local: /public/store5/DNA/Test/zhengfuxing/bioinformation_python_100/exercise_2 $ cat ../exercise_1/fq2fa.py
#!/bin/env python
# fastq 格式转为 fasta
# python fq2fa.py -i test.fq -o fq2fa.fa

import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('-i', help='input *.fastq', required=True)
parser.add_argument('-o', help='output *.fasta', required=True)
args = parser.parse_args()

input = args.i
output = args.o

output1 = "seqtk_" + output
os.system('module purge && module load seqtk && seqtk seq -A %s > %s' %(input,output1))

output2 = "py_" + output

fi = open(input, 'r')
fo = open(output2,'w')
counts = 0
for line in fi.readlines():
    counts += 1
    if counts % 4 == 1:
        line2 = line.replace("@", ">")
        fo.write(line2)
    elif counts % 4 == 2:
        fo.write(line)
    else:
        continue
fi.close
fo.close


print("完成，请检验两种转换方式结果是否一致 \n可使用如下命令检验 \n################################################# \nmd5sum %s %s \n################################################# " %(output1,output2))


