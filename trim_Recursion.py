#!/public/store5/DNA/Test/zhengfuxing/conda/bin/python
import read_fq
import time
time1 = time.time()
f = open('trim_Recursion.fq', 'w')
def maxsubsum(a,left,right):
    if (left == right):
        return [a[left],0,0]

    center = int((left+right) / 2)
    maxleftsum_list = maxsubsum(a, left, center)
    maxleftsum = maxleftsum_list[0]


    maxrightsum_list = maxsubsum(a, center+1, right)
    maxrightsum = maxrightsum_list[0]
    # 算左侧元素最大值
    leftbordersum = 0
    maxleftbordersum = a[center]
    i = center
    while i >= left:
        leftbordersum += a[i]
        if leftbordersum >= maxleftbordersum:
            maxleftbordersum = leftbordersum
            L = i
        i -= 1
    # 算右侧元素最大值
    rightbordersum = 0
    maxrightbordersum = a[center+1]
    i = center+1
    while i <= right:
        rightbordersum += a[i]
        if rightbordersum >= maxrightbordersum:
            maxrightbordersum = rightbordersum
            R = i
        i += 1

    if maxleftbordersum+maxrightbordersum > maxleftsum and maxleftbordersum+maxrightbordersum > maxrightsum:
        return [maxleftbordersum+maxrightbordersum, L, R]
    elif maxleftsum > maxleftbordersum+maxrightbordersum and maxleftsum > maxrightsum:
        return [maxleftsum, left, center]
    else:
        return [maxrightsum,center+1,right]
fq = 'test.fq'
q_int2real = {}

for i in range(0, 128):
    q_int2real[i] = 10**(-(i-33)/10)


reads = read_fq.Fq_read().fq_read(fq)
for read in reads:
    list = []
    for i in reads[read]['quality']:
        list.append(0.05 - q_int2real[ord(i)])
    v,read_l,read_r = maxsubsum(list,0,len(list)-1)
    print(reads[read]['name'], reads[read]['sequence'][read_l:read_r+1], reads[read]['description'], reads[read]['quality'][read_l:read_r+1], sep='\n', file=f)


f.close
time2 = time.time()
run_time = time2 - time1
print(' 耗时 %f 秒' %( run_time))
