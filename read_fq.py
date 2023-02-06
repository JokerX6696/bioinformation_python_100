#!/public/store5/DNA/Test/zhengfuxing/conda/bin/python
class Fq_read:

    def fq_read(self,fastq):
        f = open(fastq,'r')
        lines = f.readlines()
        f.close
        line_num = len(lines)
        if line_num % 4 != 0:
            print("Error: Please check the format of fastq!\nThe number of fastq lines is not divisible by 4!")
            exit(1)

        reads = {}
        l = 0
        while l < (line_num - 1):
            line1 = lines[l].replace('\n', '')
            l += 1
            line2 = lines[l].replace('\n', '')
            l += 1
            line3 = lines[l].replace('\n', '')
            l += 1
            line4 = lines[l].replace('\n', '')
            l += 1
            reads[line1] = {'name' : line1, 'sequence': line2, 'description': line3, 'quality' : line4}

        return reads


