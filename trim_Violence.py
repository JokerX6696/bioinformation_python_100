#!/public/store5/DNA/Test/zhengfuxing/conda/bin/python
import read_fq
import time
print('使用暴力求解算法，进行 fastq 修剪，大约消耗 2 分钟，请等待')
fq = 'test.fq'

reads = read_fq.Fq_read().fq_read(fq)

# 暴力求解法
# 第一层循环 每次循环为 一个  read
f = open('trim_Violence.fq', 'w')
counts = 0
time1 = time.time()
for read in reads:
    temp = reads[read]['quality']
    max = 0
    read_l, read_r = 0, 0
    # 左侧循环
    for j in range(0,len(temp)):

        # 右侧循环
        for k in reversed(range(0,len(temp))):
            # 当 右侧小于左侧时，循环结束
            if k < j:
                break
            S = 0
            for l in range(j,k+1):
                q_int2real = int(ord(temp[l]))
                if q_int2real < 36:
                    q_int2real = 36
                if q_int2real > 127:
                    q_int2real = 127
                # seqtk 算法 第一步 做归一化处理！ 这里的 0.05 为默认参数！
                q_int2real = float(10**(-(q_int2real-33)/10))
                S += 0.05 - q_int2real
                counts += 1
            # print(j,k,S)
            if S > max:
                max, read_l, read_r = S, j, k

    print(reads[read]['name'], reads[read]['sequence'][read_l:read_r+1], reads[read]['description'], reads[read]['quality'][read_l:read_r+1], sep='\n', file=f)
f.close
time2 = time.time()
run_time = time2 - time1
print('共经历 %d 次循环, 耗时 %f 秒' %(counts, run_time))
print('可使用 md5sum trim_Violence.fq stk.fq 命令查看结果，stk.fq 结果为使用 seqtk 修剪得到的结果！')

