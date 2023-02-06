#!/public/store5/DNA/Test/zhengfuxing/conda/bin/python
fa = './test.fa'
f = open(fa, 'r')
chr = f.readline().replace('\n','')
Seq = f.read().replace('\n','').upper()
f.close
d = {}
kmer_l = 0
kmer_r = 26
while kmer_r + 1 <= len(Seq):
    kmer = Seq[kmer_l:(kmer_r + 1)]
    if kmer in d:
        d[kmer] += 1
    else:
        d[kmer] = 1
    kmer_l += 1
    kmer_r += 1

stat = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
with open('kmer_stat.xls', 'w') as f:
    print('kmer','Counts',sep='\t',file=f)
    for i in stat:
        print(i,stat[i],sep='\t',file=f)

