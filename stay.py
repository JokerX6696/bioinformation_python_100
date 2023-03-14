#!/public/store5/DNA/Test/zhengfuxing/conda/bin/python
file = open('./blast.out.txt','r')
lines = file.readlines()
file.close
f = open('./result.xls','w')
list = []
for line in lines:
    identity = float(line.split('\t')[2])
    evalue = float(line.split('\t')[-2])
    if identity >= 90 and evalue <= 1e-5:
        list.append(line)

seq = 'null'
last_seq = 'null'
list_2 = {}
f_b = open('result_raw.txt','w')
for i in list:
    print(i,end='',file=f_b)
    seq = i.split('\t')[0]
    if seq == last_seq or last_seq == 'null':
        list_2[i] = float(i.split('\t')[-1])

    else:
        temp = dict(sorted(list_2.items(), key=lambda x:x[1], reverse=True))
        counts = 0
        for k in temp:
            print(k, end='',file=f)
            counts += 1
            if counts == 10:
                break
        list_2 = {}
        temp = {}
        list_2[i] = float(i.split('\t')[-1])
    last_seq = seq


temp = dict(sorted(list_2.items(), key=lambda x: x[1], reverse=True))
counts = 0
for k in temp:
    print(k, end='',file=f)
    counts += 1
    if counts == 10:
        break
f.close
f_b.close
