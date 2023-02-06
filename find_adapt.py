#!/public/store5/DNA/Test/zhengfuxing/conda/bin/python
import read_fq
fq = './test.fq'
fo = open('adapt_ID.xls', 'w')
reads = read_fq.Fq_read().fq_read(fq)
adapt = 'CCTGTAATCCCA'
for read in reads:
    if adapt in reads[read]['sequence']:
        print(read,file=fo)

fo.close
