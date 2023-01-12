#!/bin/env python3
fi = open('test.fq', 'r')
seq = []
name = []
while True:
    fq_1 = fi.readline()
    if not fq_1:
        break
    name.append(fq_1.strip().replace('\n','').split(' ')[0].replace('@',''))
    fq_2 = fi.readline()
    seq.append(fq_2.strip().replace('\n',''))
    fq_3 = fi.readline()
    fq_4 = fi.readline()
fi.close

fo = open('stat.xls','w')
print('fq_name','GC%',sep='\t',file=fo)

GC_all = 0
length_all = 0
counts = 0
for j in seq:
    GC = 0
    length = len(seq)
    length_all += length
    for k in j:
        if k == 'G' or k == 'C':
            GC += 1
    GC_all += GC
    print(name[counts],"%.2f" %(GC/length*100),sep='\t',file=fo)
    counts += 1
print('total',"%.2f" %(GC_all/length_all*100),sep='\t',file=fo)

print("#########################################################################################")
print("########################    脚本执行成功，请查看文件 stat.xls    ########################")
print("#########################################################################################")
