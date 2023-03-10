#!/public/store5/DNA/Test/zhengfuxing/conda/bin/python
with open('./align.fa','r') as f:
    tmp = f.readlines()
s1 = tmp[0].replace("\n","")
s2 = tmp[1].replace("\n","")
del(tmp)
# 获取每个格子的得分最高值
def getScore(ScoreMatirx,seq1,seq2,J,K,InDel,match,mismatch):
    l_id = ScoreMatirx[J][K-1] + InDel
    t_id = ScoreMatirx[J-1][K] + InDel
    if seq1[K] == seq2[J]:
        RET = match
    else:
        RET = mismatch
    lt_m = ScoreMatirx[J-1][K-1] + RET
    return max([l_id,t_id,lt_m])


""" J
      - A A C G T A G C T A C G T T A C
    - 0
    A
    G
    C
    T
    T
    A
    G
    G
    T
    T
K
"""

# 各项打分参数
InDel = -1
match = 2
mismatch = -2
# 两端序列

seq1 = '-' + s1
seq2 = '-' + s2
# 打分矩阵
print('#######################################################################################')
print('#################################    打分矩阵如下    ##################################')
print('#######################################################################################')
ScoreMatirx = []

for j in range(0,len(seq2)):
    # 每次新加一个空列
    ScoreMatirx.append([])
    for k in range(0,len(seq1)):
        if j == 0 and k == 0:
            col = 'col' + str(k)
            row = 'row' + str(j)
            ScoreMatirx[j].append(0)
            print(0,end='\t')
        else:
            if k == 0:
                ret = InDel * j
                print(ret,end='\t')
                ScoreMatirx[j].append(ret)
            elif j == 0:
                ret = InDel * k
                print(ret,end='\t')
                ScoreMatirx[j].append(ret)
            else:
                # 调用打分函数
                ret = getScore(ScoreMatirx,seq1,seq2,j,k,InDel,match,mismatch)
                print(ret,end='\t')
                ScoreMatirx[j].append(ret)
    print()

# 查看二维列表可放开
# for i in ScoreMatirx:
#     print(i)

# 回溯
#def back2start(ScoreMatirx,seq1,seq2,J,K,InDel,match,mismatch):



j = len(seq2) - 1
k = len(seq1) - 1

align1 = []
align2 = []
while j > 0 and k > 0:
    Score = ScoreMatirx[j][k]
    if seq1[k] == seq2[j]:
        RET = match
    else:
        RET = mismatch

    if (ScoreMatirx[j-1][k-1] + RET) == Score:

        align1.append(seq1[k])
        align2.append(seq2[j])
        j -= 1
        k -= 1
    elif (ScoreMatirx[j-1][k] + InDel) == Score:

        align1.append('-')
        align2.append(seq2[j])
        j -= 1
    elif (ScoreMatirx[j][k-1] + InDel) == Score:

        align1.append(seq1[k])
        align2.append('-')
        k -= 1
    else:
        print('error!!!!!!!!!')
        exit()




align1.reverse()
align2.reverse()
#############################

counts = 0
for i in align1:
    if i != '-':
        counts += 1
if counts < len(seq1)-1:
    align1_bc = []
    align2_bc = []
    for i in range(1,len(seq1)-counts):
        align1_bc.append(seq1[i])
        align2_bc.append('-')
    align1 = align1_bc + align1
    align2 = align2_bc + align2
#############################

counts = 0
for i in align2:
    if i != '-':
        counts += 1
if counts < len(seq2)-1:
    align1_bc = []
    align2_bc = []
    for i in range(1,len(seq1)-counts):
        align1_bc.append('-')
        align2_bc.append(seq2[i])
    align1 = align1_bc + align1
    align2 = align2_bc + align2
#############################
# seq1 = '-' + 'AACGTAGCTACGTTAC'
# seq2 = '-' + 'AGCTTAGGTT'


# 最终比对结果
print('#######################################################################################')
print('#################################    最终比对结果    ##################################')
print('#######################################################################################')

l = len(align1)

E = '\t'

for i in range(0,l):
    print(align1[i],end=E)
print()

for i in range(0,l):
    if align1[i] == align2[i] and align2[i] != '-':
        print("|",end=E)
    else:
        print("",end=E)

print()

for i in range(0,l):
    print(align2[i],end=E)
print()
