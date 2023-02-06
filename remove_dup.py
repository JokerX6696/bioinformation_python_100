#!/public/store5/DNA/Test/zhengfuxing/conda/bin/python
import read_fq
fo = open('rmdup_test.fq', 'w')
fo2 = open('dup_stat.xls', 'w')
fq = './test.fq'

reads = read_fq.Fq_read().fq_read(fq)

list = []
list_dup = {}

for name in reads:
    if reads[name]['sequence'] not in list:
        print(reads[name]['name'], file=fo)
        print(reads[name]['sequence'], file=fo)
        print(reads[name]['description'], file=fo)
        print(reads[name]['quality'], file=fo)
        list.append(reads[name]['sequence'])
    else:
        if reads[name]['sequence'] not in list_dup:
            # 第一次出现重复时 实际已经重复了第二次
            list_dup[reads[name]['sequence']] = 2
        else:
            list_dup[reads[name]['sequence']] += 1
# 对字典按 value 排序
dup = dict(sorted(list_dup.items(), key=lambda x: x[1], reverse=True))
print('Sequence','Counts',sep='\t',file=fo2)
for i in dup:
    print(i,dup[i],sep='\t',file=fo2)


fo.close
fo2.close
print('#######  去重文件：rmdup_test.fq  ##########################  统计重复文件：dup_stat.xls  #################################################')
