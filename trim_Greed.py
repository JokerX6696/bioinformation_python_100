#!/public/store5/DNA/Test/zhengfuxing/conda/bin/python
import read_fq
import time

time1 = time.time()
f = open('trim_Line.fq', 'w')

fq = 'test.fq'
q_int2real = {}

for i in range(0, 128):
    q_int2real[i] = 10**(-(i-33)/10)


reads = read_fq.Fq_read().fq_read(fq)

for read in reads:
    list = []
    for i in reads[read]['quality']:
        list.append(0.05 - q_int2real[ord(i)])

    ThisSum = MaxSum = 0
    begin = tmp = 0
    end = len(list) - 1
    counts = 0
    for i in list:
        counts += 1
        ThisSum += i
        if ThisSum > MaxSum:
            MaxSum = ThisSum
            begin = tmp
            end = counts
        elif ThisSum < 0:
            ThisSum = 0
            tmp = counts


    print(reads[read]['name'], reads[read]['sequence'][begin:end], reads[read]['description'], reads[read]['quality'][begin:end], sep='\n', file=f)

time2 = time.time()
run_time = time2 - time1
print(' 耗时 %f 秒' %( run_time))
f.close
